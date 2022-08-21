# Результаты тестирования OLAP Vertica

## Запись 
Для тестирования скорости записи были произведены 3 последовательных операции на добавление 1000, 10000 и 100000 записей пачками по 1000. Их результат 0.031s, 1.742s, 13.164s соответственно

    Function generate_ch_data started.
    1000 records loaded
    Function generate_ch_data finished. 
    Excecute time: 0.031 sec.
    Function generate_ch_data started.
    100000 records loaded
    Function generate_ch_data finished. 
    Excecute time: 1.742 sec.
    Function generate_ch_data started.
    1000000 records loaded
    Function generate_ch_data finished. 
    Excecute time: 13.164 sec.

## Чтение 
Чтение того же количества записей в той же последовательности: 0.034s, 0.043s, 0.227s

    Function get_limited_rows started.
    Selected movies: 1000
    Function get_limited_rows finished. 
    Excecute time: 0.034 sec.
    Function get_limited_rows started.
    Selected movies: 10000
    Function get_limited_rows finished. 
    Excecute time: 0.043 sec.
    Function get_limited_rows started.
    Selected movies: 100000
    Function get_limited_rows finished. 
    Excecute time: 0.227 sec.
    Function get_count started.
    Total records: 2101000
    Function get_count finished. 
    Excecute time: 0.008 sec.
    Function get_uniq_movies_count started.
    Total unique movies: 2000
    Function get_uniq_movies_count finished. 
    Excecute time: 0.066 sec.
    Function get_uniq_users_count started.
    Total unique users: 2000
    Function get_uniq_users_count finished. 
    Excecute time: 0.064 sec.
    Function get_avg_percent started.
    Avg db percent: 0.5009023212834415
    Function get_avg_percent finished. 
    Excecute time: 0.016 sec.
    Function get_popular started.
    Result: 687469
    Function get_popular finished. 
    Excecute time: 0.372 sec.