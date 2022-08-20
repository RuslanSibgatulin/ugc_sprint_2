import logging
import logging.config
import traceback
from typing import List, NamedTuple

import db.clickhouse_client as chc
from config import settings
from db.kafka_consumer import Consumer
from models.models import ViewEvent


def transform(data: List[NamedTuple]) -> List[ViewEvent]:
    out = []
    for i in data:
        out.append(
            ViewEvent.parse_obj(i.value)
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
