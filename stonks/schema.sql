--This is where we will define how our data is stored
--TICKER    P/E     VOLUME      PRICE       MARKET CAP      MORE?

DROP TABLE IF EXISTS stock;
DROP TABLE IF EXISTS tickers;

CREATE TABLE stock (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT UNIQUE NOT NULL,
    price FLOAT NOT NULL,
    p_e FLOAT NOT NULL
);