import logging
import logging.config
import traceback
from typing import List, NamedTuple

import db.clickhouse_client as chc
from config import settings
from db.kafka_consumer import Consumer
from models.models import ViewEvent


def transform(data: List[NamedTuple]) -> List[ViewEvent]:
    return [ViewEvent.parse_obj(i.value) for i in data]


def load(data: List[ViewEvent]):
    logger.debug(data)
    # chc.insert_views(data)


def etl_loop():
    logger.info(
        'Listening topic %s on %s',
        settings.KAFKA_TOPIC,
        settings.kafka_uri
    )
    views = Consumer(
        settings.KAFKA_TOPIC,
        settings.kafka_uri
    )
    while True:
        try:
            data = views.messages(
                settings.BATCH_SIZE,
                settings.READ_TIMEOUT
            )
            if data:
                t_data = transform(data)
                logger.debug(t_data)
                # load(t_data)
        except KeyboardInterrupt:
            logger.info('Interrupted')
            break
        except Exception:
            logger.error(traceback.format_exc())


if __name__ == "__main__":
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger('ETLUGC')
    logger.info('Started')
    etl_loop()
    logger.info('Finished')
