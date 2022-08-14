from ch_client import client
from utils import timer

SQL_COUNT_ALL = "SELECT count(*) FROM ugc_data.user_movie_progress"
SQL_COUNT = "SELECT uniqExact({field}) FROM ugc_data.user_movie_progress"
SQL_AVG_PERCENT = "SELECT AVG(percent) FROM ugc_data.user_movie_progress"
SQL_ANALYTIC = "SELECT uniqExact(movie_id, user_id) FROM ugc_data.user_movie_progress WHERE percent >= 0.600"


@timer
def get_count():
    total_count = client.execute(SQL_COUNT_ALL)
    print(f"Total records: {total_count[0][0]}")


@timer
def get_uniq_movies_count():
    movies_count = client.execute(SQL_COUNT.format(field="movie_id"))
    print(f"Total unique movies: {movies_count[0][0]}")


@timer
def get_uniq_users_count():
    users_count = client.execute(SQL_COUNT.format(field="user_id"))
    print(f"Total unique users: {users_count[0][0]}")


@timer
def get_avg_percent():
    avg_ = client.execute(SQL_AVG_PERCENT)
    print(f"Avg db percent: {avg_[0][0]}")


@timer
def get_popular():
    result = client.execute(SQL_ANALYTIC)
    print(f"Result: {result[0][0]}")


if __name__ == "__main__":
    get_count()  # Excecute time: 0.231 sec.
    get_uniq_movies_count()  # Excecute time: 0.66 sec.
    get_uniq_users_count()  # Excecute time: 0.998 sec.
    get_avg_percent()  # Excecute time: 0.243 sec.
    get_popular()  # Excecute time: 1.519 sec.
