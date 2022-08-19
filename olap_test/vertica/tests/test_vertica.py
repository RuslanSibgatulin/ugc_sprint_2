import pytest


@pytest.mark.parametrize(
    'batch_count', [1, 10, 100, 1000]
)
def test_1_insert(generate_data, vertica_cursor, batch_count):
    for _ in range(batch_count):
        vertica_cursor.executemany(
            "INSERT INTO views (user_id, movie_id, viewed_frame) VALUES (?,?,?)",
            generate_data,
            True
        )


@pytest.mark.parametrize(
    'size', [1000, 10000, 100000, 1000000]
)
def test_2_select(vertica_cursor, size):
    vertica_cursor.execute(f"SELECT * FROM views LIMIT {size}")
    assert len(vertica_cursor.fetchall()) == size


def test_3_count(vertica_cursor):
    vertica_cursor.execute("SELECT COUNT(*) FROM views WHERE viewed_frame > 3600")
    print('Rows stored', vertica_cursor.fetchone()[0])


def test_4_avg(vertica_cursor):
    vertica_cursor.execute(
        """
        SELECT user_id, movie_id, AVG(viewed_frame)
        FROM views
        WHERE viewed_frame > 3600
        GROUP BY movie_id, user_id
        """
    )
    print('Rows fetched', len(vertica_cursor.fetchall()))


def test_5_sum(vertica_cursor):
    vertica_cursor.execute(
        """
        SELECT user_id, movie_id, SUM(viewed_frame)
        FROM views
        WHERE viewed_frame > 7200
        GROUP BY movie_id, user_id
        """
    )
    print('Rows fetched', len(vertica_cursor.fetchall()))
