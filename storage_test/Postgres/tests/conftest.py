import uuid

import pytest
from psycopg2 import connect as _pg_conn


@pytest.fixture(scope="session")
def films():
    films = [str(uuid.uuid4()) for _ in range(10000)]
    return films


@pytest.fixture(scope="session")
def users():
    users = [str(uuid.uuid4()) for _ in range(100000)]
    return users


@pytest.fixture(scope="session")
def postgres_connection():
    dsn = {
        "dbname": "db_test",
        "user": "test",
        "password": "123qwe",
        "host": "127.0.0.1"
    }
    with _pg_conn(**dsn) as pg_conn:
        yield pg_conn


@pytest.fixture(scope="session")
def random_film_id(postgres_connection):
    top_ratings = """
        SELECT film_id FROM film_likes
        ORDER BY random()
        LIMIT 1;
    """

    with postgres_connection.cursor() as cur:
        cur.execute(top_ratings)
        res = cur.fetchone()
        return res[0]
