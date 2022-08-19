import os
import random
import uuid

import pytest
import vertica_python


@pytest.fixture
def generate_data(scope="session"):
    users = [uuid.uuid4() for _ in range(10000)]
    films = [uuid.uuid4() for _ in range(100000)]

    return [
        (
            random.choice(users),
            random.choice(films),
            random.randrange(0, 2 * 3600)
        ) for _ in range(1000)
    ]


@pytest.fixture(scope="session")
def vertica_cursor():
    connection_info = {
        'host': os.environ['VERTICA_HOST'],
        'port': 5433,
        'user': 'dbadmin',
        'password': '',
        'database': 'docker',
        'autocommit': True,
    }
    with vertica_python.connect(**connection_info) as connection:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS views (
            id IDENTITY,
            user_id uuid NOT NULL,
            movie_id uuid NOT NULL,
            viewed_frame INTEGER NOT NULL,
            event_time TIMESTAMP NOT NULL DEFAULT NOW()
        );
        """)
        yield cursor
