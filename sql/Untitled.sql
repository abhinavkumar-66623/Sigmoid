CREATE DATABASE IF NOT EXISTS nyse;

USE nyse;

CREATE TABLE nyse_daily_prices (
    exchange        VARCHAR(10),
    symbol          VARCHAR(10),
    trade_date      DATE,
    open_price      DECIMAL(10,2),
    high_price      DECIMAL(10,2),
    low_price       DECIMAL(10,2),
    close_price     DECIMAL(10,2),
    volume          BIGINT,
    adj_close_price DECIMAL(10,2)
);

CREATE TABLE nyse_daily_prices1(
    exchange        VARCHAR(10),
    symbol          VARCHAR(10),
    trade_date      DATE,
    open_price      DECIMAL(10,2),
    high_price      DECIMAL(10,2),
    low_price       DECIMAL(10,2),
    close_price     DECIMAL(10,2),
    volume          BIGINT,
    adj_close_price DECIMAL(10,2)
);

LOAD DATA LOCAL INFILE
'/Users/as-mac-1166/Downloads/nyse_sample_data.csv'
INTO TABLE nyse_daily_prices1
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(exchange,
 symbol,
 trade_date,
 open_price,
 high_price,
 low_price,
 close_price,
 volume,
 adj_close_price);
 
 
--  show variables like 'secure_file_priv';
 
 show variables like 'local_infile';
 set global local_infile=1;
 
SELECT *
FROM nyse_daily_prices1
LIMIT 10;
     
