import logging
import logging.config
import traceback
from typing import List, NamedTuple

import clickhouse_client as chc
from config import settings
from kafka_consumer import Consumer
from models import ViewEvent


def transform(data: List[NamedTuple]) -> List[ViewEvent]:
    out = []
    for i in data:
        ids = str(i.key).split('+')
        val = str(i.value).split('+')

        obj = {
            'user_id': ids[0],
            'film_id': ids[1],
            'viewed_frame': val[0],
            'total_frames': 10800
        }
        out.append(
            ViewEvent.parse_obj(obj)
        )

    return out


def load(data: List[ViewEvent]):
    chc.insert_views(data)


def etl_loop():
    views = Consumer(
        settings.KAFKA_TOPIC,
        settings.KAFKA_BROKER
    )
    while True:
        try:
            data = views.messages(
                settings.BATCH_SIZE,
                settings.READ_TIMEOUT
            )
            if data:
                t_data = transform(data)
                load(t_data)
        except KeyboardInterrupt:
            logger.info('ETL interrupted')
            break
        except Exception:
            logger.error(traceback.format_exc())


if __name__ == "__main__":
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger('ETLUGC')
    logging.info('Started')
    etl_loop()
    logging.info('Finished')
