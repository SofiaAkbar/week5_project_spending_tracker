DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS tags;

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    type VARCHAR(255)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    amount FLOAT,
    date VARCHAR(255),
    tag_id SERIAL REFERENCES tags(id),
    merchant_id SERIAL REFERENCES merchants(id)
);