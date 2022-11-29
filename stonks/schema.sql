--This is where we will define how our data is stored
--TICKER, P/E, VOLUME, PRICE, MARKET CAP, EPS, SECTOR, EMPLOYEES, LOGO, grossProfits, dividends, earningsGrowth

DROP TABLE IF EXISTS stock;

CREATE TABLE stock (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT UNIQUE NOT NULL,
    price FLOAT NOT NULL,
    p/e FLOAT NOT NULL,
    volume FLOAT NOT NULL
);