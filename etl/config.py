from pydantic import BaseSettings


class ETLSettings(BaseSettings):
    LOG_LEVEL: str = "INFO"
    BATCH_SIZE: int = 10
    READ_TIMEOUT: int = 1000
    CLICKHOUSE_SERVER: str = "127.0.0.1"
    KAFKA_TOPIC: str = 'views'
    KAFKA_BROKER: str = '127.0.0.1:9092'


settings = ETLSettings()
