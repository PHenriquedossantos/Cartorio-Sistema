CREATE TABLE principal.users (
    id uuid primary key,
    name varchar not null,
    password varchar not null,
    login varchar not null unique
)