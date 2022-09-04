# Тестирование Postgres
Для тестирования был поднят инстанс PostgreSQL 13 в docker.
Эта СУБД использует следующие алгоритмы сжатия:
- LZ4 (Postgres 14)
- PGLZ 

## Запись 
Для тестирования скорости записи были произведены 4 последовательных операции на добавление 10к, 100к, 1М и 10М записей в таблицу лайков. Их результат:
- 10к   - 0.81s
- 100к  - 7.78s
- 1М    - 74.51s
- 10М   - 773.83s

## Чтение 
Чтение производилось с агрегированием для формирования массива данных под задачи спринта.

### Топ рейтинговых фильмов
Рейтинг вычислялся на основе оценок пользователей для величины более 5.
Результат выборки:
- Топ-10   - 2.07s
- Топ-100  - 1.94s
- Топ-1000 - 1.96s

### Рейтинг одного фильма
Случайный выбор фильма из БД и его оценка заняли 0.29s.
В оценку входят операции агрегирования для получения массива данных:
- Количество лайков
- Количество дизлайков
- Средний рейтинг по всем оценкам
- Количество оценок для фильма

## Результат pytest
Тестирование было проведено с использованием библиотеки pytest в синхронном режиме.

    pytest tests/ -vvs --durations=0
    ===================================================== test session starts ======================================================
    platform linux -- Python 3.10.4, pytest-7.1.2, pluggy-1.0.0
    cachedir: .pytest_cache
    rootdir: Postgres/tests, configfile: pytest.ini
    plugins: Faker-14.1.0, asyncio-0.18.3
    asyncio: mode=auto
    collected 8 items                                                                                                              

    tests/test_postgres.py::test_1_insert_likes[10000] Inserted 10000 likes
    PASSED
    tests/test_postgres.py::test_1_insert_likes[100000] Inserted 100000 likes
    PASSED
    tests/test_postgres.py::test_1_insert_likes[1000000] Inserted 1000000 likes
    PASSED
    tests/test_postgres.py::test_1_insert_likes[10000000] Inserted 10000000 likes
    PASSED
    tests/test_postgres.py::test_2_top_ratings[10] PASSED
    tests/test_postgres.py::test_2_top_ratings[100] PASSED
    tests/test_postgres.py::test_2_top_ratings[1000] PASSED
    tests/test_postgres.py::test_3_film_rating PASSED

    ========================================================== slowest durations ==========================================================
    773.83s call     test_postgres.py::test_1_insert_likes[10000000]
    74.51s call     test_postgres.py::test_1_insert_likes[1000000]
    7.78s call     test_postgres.py::test_1_insert_likes[100000]
    2.07s call     test_postgres.py::test_2_top_ratings[10]
    1.96s call     test_postgres.py::test_2_top_ratings[1000]
    1.94s call     test_postgres.py::test_2_top_ratings[100]
    0.81s call     test_postgres.py::test_1_insert_likes[10000]
    0.29s call     test_postgres.py::test_3_film_rating
    ==================================================== 8 passed in 865.07s (0:14:25) ====================================================
