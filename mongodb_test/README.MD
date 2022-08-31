# Тестирование MongoDB
Для тестирования был поднят кластер MongoDB в docker на основе образа mongo:6.0 из 2 шардов по 3 реплики, 3 сервера конфигурации и 2 маршрутизатора.
## Запуск
Для запуска инфраструктуры выполнить в терминале

    DOCKER_BUILDKIT=1 docker-compose -f Mongo-docker-compose.yml up

Затем выполнить первоначальную настройку скриптом и запуск тестов
    
    rs-init.sh && pytest ./tests/mongo_test.py -vv --durations=0


## Запись 
Для тестирования скорости записи были произведены 3 последовательных операции на добавление 100, 1000 и 10000 документов в коллекцию лайков. Их результат 0.17s, 1.78s, 18.21s соответственно.

## Чтение 
Чтение производилось с агрегированием для формирования массива данных под задачи спринта.

### Топ рейтинговых фильмов
Рейтинг вычислялся на основе оценок пользователей для величины более 5.
Результат выборки:
- Топ-10   - 0.24s
- Топ-100  - 0.23s
- Топ-1000 - 0.31s

### Рейтинг одного фильма
Случайный выбор фильма из коллекции и его оценка заняли 0.05s.
В оценку входят операции агрегирования для получения массива данных:
- Количество лайков
- Количество дизлайков
- Средний рейтинг по всем оценкам
- Количество оценок для фильма

## Результат pytest
Тестирование было проведено с использованием библиотеки pytest в асинхронном режиме.  

    pytest mongo_test.py -vv --durations=0
    ========================================================== test session starts ===========================================================
    platform linux -- Python 3.10.4, pytest-7.1.2, pluggy-1.0.0
    cachedir: .pytest_cache
    rootdir: /Practicum/UGC/MongoDB, configfile: pytest.ini
    plugins: Faker-14.1.0, asyncio-0.18.3
    asyncio: mode=auto
    collected 12 items                                                                                                                       

    mongo_test.py::test_insert_movies_likes[100] PASSED                                                                                [  8%]
    mongo_test.py::test_insert_movies_likes[1000] PASSED                                                                               [ 16%]
    mongo_test.py::test_insert_movies_likes[10000] PASSED                                                                              [ 25%]
    mongo_test.py::test_insert_review_likes PASSED                                                                                     [ 33%]
    mongo_test.py::test_insert_bookmarks[100] PASSED                                                                                   [ 41%]
    mongo_test.py::test_insert_bookmarks[1000] PASSED                                                                                  [ 50%]
    mongo_test.py::test_insert_bookmarks[10000] PASSED                                                                                 [ 58%]
    mongo_test.py::test_top_movies[10] PASSED                                                                                          [ 66%]
    mongo_test.py::test_top_movies[100] PASSED                                                                                         [ 75%]
    mongo_test.py::test_top_movies[1000] PASSED                                                                                        [ 83%]
    mongo_test.py::test_film_ratings PASSED                                                                                            [ 91%]
    mongo_test.py::test_user_bookmarks PASSED                                                                                          [100%]

    =========================================================== slowest durations ============================================================
    19.25s call     mongo_test.py::test_insert_bookmarks[10000]
    18.21s call     mongo_test.py::test_insert_movies_likes[10000]
    12.29s call     mongo_test.py::test_insert_review_likes
    1.89s call     mongo_test.py::test_insert_bookmarks[1000]
    1.78s call     mongo_test.py::test_insert_movies_likes[1000]
    0.31s call     mongo_test.py::test_top_movies[1000]
    0.24s call     mongo_test.py::test_top_movies[10]
    0.23s call     mongo_test.py::test_top_movies[100]
    0.21s call     mongo_test.py::test_insert_bookmarks[100]
    0.17s call     mongo_test.py::test_insert_movies_likes[100]
    0.05s call     mongo_test.py::test_film_ratings
    0.00s call     mongo_test.py::test_user_bookmarks


    ========================================================== 12 passed in 56.18s ===========================================================
