# Сравнение производительности OLAP хранилищ
Для сравнения были выбраны Vertica и ClickHouse. Основным методом тестирования были запись 1 000, 10 000, 100 000 записей и их чтение с замером затраченного времени.

## Аппаратная часть
Тестирование проводилось на ноутбуке с конфигурацией:
- Процессор: AMD Ryzen 5 5500U 2.10 ГГц, 6 ядер
- Оперативная память: 16 Гб DDR4
- Накопитель: SAMSUNG MZALQ512HBLU-00BL2 - SSD 512 Гб

## Результаты
Сравнительный результат тестирования [Vertica](./vertica/Readme.md) и [ClickHouse](./clickhouse/Readme.md) представлен в таблице

Операция     | Vertica     | ClickHouse  |
-------------|-------------| ----------- |
INSERT 1000  | 2.21s       | 0.031s      |
INSERT 10000 | 59.09s      | 1.742s      |
INSERT 100000| 602.96s     | 13.164s     |
SELECT 1000  | 0.05s       | 0.034s      |
SELECT 10000 | 0.38s       | 0.043s      |
SELECT 100000| 3.45s       | 0.227s      |

Как видно из таблицы, Vertica сильно уступает ClickHouse в скорости записи и чтения, при объемах выше 100 000 записей.
Поэтому в качестве OLAP для проекта UGC был выбран **ClickHouse**.