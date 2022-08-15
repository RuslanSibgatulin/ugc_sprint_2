from datetime import datetime
from random import choice, randint
from uuid import uuid4

from clickhouse_driver.errors import Error

from ch_client import client
from utils import timer


SQL = "INSERT INTO ugc_data.user_movie_progress VALUES"
MOVIES_ID = [str(uuid4()) for _ in range(1000)]
USERS_ID = [str(uuid4()) for _ in range(1000)]


@timer
def generate_ch_data() -> None:
    records_count = 1000000
    payload = list()
    for num in range(records_count):
        record = dict(
            id=num+1,
            user_id=choice(USERS_ID),
            movie_id=choice(MOVIES_ID),
            time=randint(1, 10800),
            percent=round(randint(1, 1000) / 1000, 3),
            event_time=datetime.now()
        )
        payload.append(record)
        if len(payload) == 1000:
            try:
                client.execute(SQL, payload)
            except Error as e:
                print(e.code, e.message)
            finally:
                payload.clear()


if __name__ == "__main__":
    generate_ch_data()
    # Without buffer excecute time: 25.986 sec. 1
    # Without buffer excecute time: 93.543 sec. 2
