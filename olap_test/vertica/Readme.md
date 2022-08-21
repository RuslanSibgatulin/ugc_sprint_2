# Результаты тестирования OLAP Vertica

## Запись 
Для тестирования скорости записи были произведены 3 последовательных операции на добавление 1000, 10000 и 100000 записей пачками по 1000. Их результат 2.21s, 59.09s, 602.96s соответственно

    ============================================== test session starts ==============================================
    platform linux -- Python 3.10.4, pytest-6.2.5, py-1.11.0, pluggy-1.0.0                                             

    test_vertica.py::test_1_insert[1] PASSED                                                                  [ 16%]
    test_vertica.py::test_1_insert[10] PASSED                                                                 [ 33%]
    test_vertica.py::test_1_insert[100] PASSED                                                                [ 50%]

    =============================================== slowest durations ===============================================
    602.96s call     test_vertica.py::test_1_insert[100]
    59.09s call     test_vertica.py::test_1_insert[10]
    2.21s call     test_vertica.py::test_1_insert[1]

## Чтение 
Чтение того же количества записей в той же последовательности: 0.05s, 0.38s, 3.45s

    ============================================== test session starts ==============================================
    platform linux -- Python 3.10.4, pytest-6.2.5, py-1.11.0, pluggy-1.0.0                                          

    test_vertica.py::test_2_select[1000] PASSED                                                               [ 33%]
    test_vertica.py::test_2_select[10000] PASSED                                                              [ 66%]
    test_vertica.py::test_2_select[100000] PASSED                                                             [100%]

    =============================================== slowest durations ===============================================
    3.45s call     test_vertica.py::test_2_select[100000]
    0.38s call     test_vertica.py::test_2_select[10000]
    0.05s call     test_vertica.py::test_2_select[1000]
    ======================================== 3 passed, 2 deselected in 3.90s ========================================

## Чтение в процессе вставки большого набора данных
    ============================================== test session starts ==============================================
    platform linux -- Python 3.10.4, pytest-6.2.5, py-1.11.0, pluggy-1.0.0a/tests                                          

    test_vertica.py::test_2_select[1000] PASSED
    test_vertica.py::test_2_select[10000] PASSED
    test_vertica.py::test_2_select[100000] PASSED
    test_vertica.py::test_3_count Rows stored 117395
    PASSED
    test_vertica.py::test_4_avg Rows fetched 1989
    PASSED
    test_vertica.py::test_5_sum Rows fetched 0
    PASSED

    =============================================== slowest durations ===============================================
    2.86s call     test_vertica.py::test_2_select[100000]
    0.39s call     test_vertica.py::test_2_select[10000]
    0.05s call     test_vertica.py::test_2_select[1000]
    0.05s call     test_vertica.py::test_4_avg
    0.01s call     test_vertica.py::test_5_sum
    0.01s call     test_vertica.py::test_3_count
    ======================================== 6 passed, 4 deselected in 3.41s ========================================

## Вставка 1М записей их чтение
    ============================================== test session starts ==============================================
    platform linux -- Python 3.10.4, pytest-6.2.5, py-1.11.0, pluggy-1.0.0                                          

    test_vertica.py::test_1_insert[1] PASSED
    test_vertica.py::test_1_insert[10] PASSED
    test_vertica.py::test_1_insert[100] PASSED
    test_vertica.py::test_1_insert[1000] PASSED
    test_vertica.py::test_2_select[1000] PASSED
    test_vertica.py::test_2_select[10000] PASSED
    test_vertica.py::test_2_select[100000] PASSED
    test_vertica.py::test_2_select[1000000] PASSED
    test_vertica.py::test_3_count Rows stored 549621
    PASSED
    test_vertica.py::test_4_avg Rows fetched 1989
    PASSED
    test_vertica.py::test_5_sum Rows fetched 0
    PASSED

    =============================================== slowest durations ===============================================
    6129.46s call     test_vertica.py::test_1_insert[1000]
    604.00s call     test_vertica.py::test_1_insert[100]
    59.73s call     test_vertica.py::test_1_insert[10]
    21.80s call     test_vertica.py::test_2_select[1000000]
    4.04s call     test_vertica.py::test_2_select[1000]
    3.41s call     test_vertica.py::test_2_select[100000]
    2.35s call     test_vertica.py::test_1_insert[1]
    0.36s call     test_vertica.py::test_2_select[10000]
    0.06s call     test_vertica.py::test_4_avg
    0.02s call     test_vertica.py::test_3_count
    0.01s call     test_vertica.py::test_5_sum
    ======================================== 11 passed in 6827.71s (1:53:47) ========================================