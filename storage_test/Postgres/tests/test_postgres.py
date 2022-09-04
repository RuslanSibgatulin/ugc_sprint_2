import random
from uuid import uuid4

import pytest
from faker import Faker
from psycopg2.extras import RealDictCursor, execute_batch


def gen_likes(postgres_connection, films, users):
    fake = Faker()
    table_fields = ["id", "user_id", "film_id", "rating", "created"]
    data = [
        (
            str(uuid4()),
            i,
            random.choice(users),
            random.randrange(0, 11),
            fake.date_time_this_year()
        ) for i in films
    ]
    with postgres_connection.cursor() as cur:
        fields = ", ".join(table_fields)
        values = ("%s, "*len(table_fields))[:-2]
        query = """INSERT INTO film_likes ({0}) VALUES ({1})
        ON CONFLICT (id) DO NOTHING;
        """.format(fields, values)
        execute_batch(cur, query, data)
        postgres_connection.commit()

    return len(films)


@pytest.mark.parametrize(
    'size', [10000, 100000, 1000000, 10000000]
)
def test_1_insert_likes(postgres_connection, films, users, size):
    n = 0
    while n < size:
        n += gen_likes(postgres_connection, films, users)

    print(f"Inserted {n} likes")


@pytest.mark.parametrize(
    'top_limit', [10, 100, 1000]
)
def test_2_top_ratings(postgres_connection, top_limit):
    top_ratings = """
        SELECT film_id, AVG(rating) FROM film_likes
        GROUP BY film_id
        ORDER BY avg DESC
        LIMIT {0}
    """.format(top_limit)

    with postgres_connection.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(top_ratings)
        res = cur.fetchall()
    return list(map(dict, res))


def test_3_film_rating(postgres_connection, random_film_id):
    film_rating = """
        SELECT film_id, AVG(rating), COUNT(*),
        COUNT(*) FILTER(where rating >= 5) AS likes,
        COUNT(*) FILTER(where rating < 5) AS dislikes
        FROM film_likes
        WHERE film_id = '{0}'
        GROUP BY film_id
    """.format(random_film_id)
    with postgres_connection.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(film_rating)
        res = cur.fetchall()

    return list(map(dict, res))
