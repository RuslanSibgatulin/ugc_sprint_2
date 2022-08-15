CREATE DATABASE ugc_data;

CREATE DATABASE shard;

CREATE DATABASE replica;

CREATE TABLE shard.user_movie_progress (
    id         Int64,
    user_id    String,
    movie_id   String,
    time       UInt16,
    percent    Float32,
    event_time DateTime
)
Engine=ReplicatedMergeTree('/clickhouse/tables/shard1/user_movie_progress', 'replica_1')
    PARTITION BY toYYYYMMDD(event_time)
    ORDER BY id;

CREATE TABLE replica.user_movie_progress (
    id         Int64,
    user_id    String,
    movie_id   String,
    time       UInt16,
    percent    Float32,
    event_time DateTime
) Engine=ReplicatedMergeTree('/clickhouse/tables/shard2/user_movie_progress', 'replica_2')
    PARTITION BY toYYYYMMDD(event_time)
    ORDER BY id;

CREATE TABLE ugc_data.user_movie_progress (
    id         Int64,
    user_id    String,
    movie_id   String,
    time       UInt16,
    percent    Float32,
    event_time DateTime
)
ENGINE = Distributed('company_cluster', '', user_movie_progress, rand());