# Сервис UGC - контент создаваемый пользователем. Проектная работа 8 спринта.
[![Generic badge](https://img.shields.io/badge/Changelog-<COLOR>.svg)](./CHANGELOG.md)
[![Generic badge](https://img.shields.io/badge/Our-Team-<COLOR>.svg)](#команда)


Этот сервис будет примимать события от других компонентов системы, сохраняя их в Kafka, и последующей передачей через ETL процесс в OLAP ClickHouse.
[Ссылка на приватный репозиторий с командной работой.](https://github.com/RuslanSibgatulin/ugc_sprint_1)

## Используемые технологии
- Код приложения на Python + aiohttp.
- Транзакцилнной хранилище (OLTP) - Kafka.
- Аналитическое хранилище (OLAP) - ClickHouse
- Все компоненты системы запускаются через Docker-compose.

# Запуск приложения
## Клонировать репозиторий
    git clone git@github.com:RuslanSibgatulin/ugc_sprint_1.git

## Подготовка окружения
Подготовить .env файл с переменными окружения по шаблону docker/envs/example.sample и сохранить под именем docker/envs/prod.env.
Для среды разработи создать файл docker/envs/dev.env, для тестов docker/envs/test.env

## Запуск компонентов системы
Перейти в каталог `docker`
    cd docker
    DOCKER_BUILDKIT=1 docker-compose -f kafka-docker-compose.yml -f api-docker-compose.yml up --build --force-recreate

## Документация сервиса регистрации событий UGC доступна по ссылке
- http://127.0.0.1:8888/apidocs/


# Команда
- [Ruslan Sibgatulin (lead)](https://github.com/RuslanSibgatulin)
- [Fedor Kuzminov](https://github.com/Riyce)