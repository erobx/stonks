--logo_url,ticker,PE Ratio (TTM),Avg. Volume,Previous Close,Market Cap,EPS (TTM),sector,fullTimeEmployees,Revenue (ttm),Quarterly Revenue Growth,Gross Profit (ttm)
DROP TABLE IF EXISTS stock;

CREATE TABLE stock (
    logo TEXT NOT NULL,
    ticker TEXT NOT NULL,
    pe FLOAT NOT NULL,
    volume FLOAT NOT NULL,
    price FLOAT NOT NULL,
    market_cap FLOAT NOT NULL,
    eps FLOAT NOT NULL,
    sector TEXT NOT NULL,
    employees INTEGER NOT NULL,
    revenue FLOAT NOT NULL,
    growth FLOAT NOT NULL,
    profit FLOAT NOT NULL
);