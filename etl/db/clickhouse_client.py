from clickhouse_driver import Client

from backoff import backoff
from config import settings


client = Client(host=settings.CLICKHOUSE_SERVER)


@backoff('Clickhouse.insert')
def insert_views(data):
    SQL = "INSERT INTO ugc_data.user_movie_progress VALUES"
    client.execute(SQL, data)
