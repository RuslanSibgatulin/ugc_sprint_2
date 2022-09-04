CREATE TABLE IF NOT EXISTS film_likes (
    id uuid PRIMARY KEY,
    user_id uuid NOT NULL,
    film_id uuid NOT NULL,
    rating int,
    created timestamp with time zone
);