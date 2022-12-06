--This is where we will define how our data is stored
--TICKER, trailingPE, averageVolume, regularMarketPrice, marketCap, forwardPE, sector, fullTimeEmployees, logo_url, grossProfits, dividends, earningsGrowth

DROP TABLE IF EXISTS stock;

CREATE TABLE stock (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT UNIQUE NOT NULL,
    price FLOAT NOT NULL,
    p/e FLOAT NOT NULL,
    volume FLOAT NOT NULL
);