# Сервис UGC - контент создаваемый пользователем. Проектная работа 9 спринта.
[![Generic badge](https://img.shields.io/badge/Changelog-<COLOR>.svg)](./CHANGELOG.md)
[![Generic badge](https://img.shields.io/badge/Our-Team-<COLOR>.svg)](#команда)

Этот сервис будет примимать события от других компонентов системы, сохраняя их в Kafka, и последующей передачей через ETL процесс в OLAP ClickHouse. А так же позволит регистрировать лайки пользователей, их закладки и рецензии на фильмы.
[Ссылка на приватный репозиторий с командной работой.](https://github.com/RuslanSibgatulin/ugc_sprint_2)

## Сравнение хранилищ
Перед реализацией проекта были проведены сравнительные тесты 
- [аналитичесих хранилищ](./olap_test/Readme.md)
- [документоориентированной СУБД MongoDB](./mongodb_test/README.MD)


## Используемые технологии
- Код приложения на Python + fastapi.
- Хранилище BigData - MongoDB.
- Транзакционное хранилище (OLTP) - Kafka.
- Аналитическое хранилище (OLAP) - ClickHouse.
- Сборщики логов: Sentry и ELK.
- Все компоненты системы запускаются через Docker-compose.

# Запуск приложения
## Клонировать репозиторий
    git clone git@github.com:RuslanSibgatulin/ugc_sprint_2.git

## Подготовка окружения
### Подготовить файл с переменными окружения и сохранить под именем `docker/envs/prod`:

    KAFKA_HOST=broker
    KAFKA_PORT=29092
    SECRET_KEY=secret
    HASH_ALGORITHM=SHA-256
    MONGO_HOST=mongos1
    MONGO_PORT=27019
    LOGSTASH_HOST=logstash
    LOGSTASH_PORT=5044
    SENTRY_DSN=

    WEBAPP_WORKERS_PER_CORE=1
    WEBAPP_HOST=0.0.0.0
    WEBAPP_PORT=8888
    WEBAPP_LOG_LEVEL=debug


### Подготовить файл с переменными окружения и сохранить под именем `docker/envs/etl`:

    KAFKA_HOST=broker
    KAFKA_PORT=29092
    KAFKA_TOPIC=views
    BATCH_SIZE=10
    READ_TIMEOUT=1000
    CLICKHOUSE_SERVER=clickhouse


## Запуск UGC API и OLAP

    cd docker
    DOCKER_BUILDKIT=1 docker-compose -f kafka-docker-compose.yml -f ugc-docker-compose.yml -f ch-docker-compose.yml -f elk-docker-compose.yml -f mongo-docker-compose.yml up --build --force-recreate

## Документация сервиса регистрации событий UGC доступна по ссылке
- http://127.0.0.1:8000/api/openapi


# Команда
- [Ruslan Sibgatulin (lead)](https://github.com/RuslanSibgatulin)
- [Fedor Kuzminov](https://github.com/Riyce)