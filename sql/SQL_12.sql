use retail_db;

Explain
select distinct order_status
from orders
order by order_status;


CREATE INDEX idx_orders_order_status ON orders(order_status);

EXPLAIN analyze
select * from orders;


CREATE DATABASE IF NOT EXISTS retail_analytics;
USE retail_analytics;
CREATE TABLE IF NOT EXISTS products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    category VARCHAR(50),
    product_name VARCHAR(100),
    total_sales INT
);


INSERT INTO products (category, product_name, total_sales) VALUES
('Electronics', 'iPhone 17', 120),
('Electronics', 'Samsung Galaxy S25', 115),
('Electronics', 'OnePlus Nord CE5', 115),
('Electronics', 'Redmi A4', 100),
('Electronics', 'Vivo V27', 100),
('Electronics', 'Realme Narzo', 95),
('Electronics', 'Samsung Galaxy A55', 90),
('Electronics', 'iPhone 16 Pro', 85);

select * from products order by total_sales desc;

select rank() over(order by total_sales desc),product_name
from products;

select product_ name,total_sales,
row_number() over(order by total_sales) as popularity,
rank() over(order by total_sales) as rank_num,
dense_rank() over(order by total_sales ),
ntile(4) over(order by total_sales desc) as performance_bucket 
from products;
-- select 1 as rnk, p1.product_name
-- from products p1 
-- join 
-- products p2
-- on p1.total_sales>p2.total_sales;



CREATE TABLE sales (
    order_id   INT,
    order_date DATE,
    product    VARCHAR(50),
    amount     INT
);

INSERT INTO sales VALUES
(1, '2025-01-05', 'Laptop', 1000),
(2, '2025-01-10', 'Phone',  500),
(3, '2025-01-20', 'Tablet', 300),
(4, '2025-02-02', 'Laptop', 1200),
(5, '2025-02-05', 'Phone',  600),
(6, '2025-02-15', 'Tablet', 400);

select order_id,
	   order_date,
       product,
       amount,
       Date_format(order_date,'%Y-%m') as order_month,
       sum(amount) as monthly_total
from sales
group by order_month
order by order_date;


select order_id,
	   order_date,
       product,
       amount,
       lag(amount) over(
       partition by date_format(order_date,'%Y-%m')
       order by order_date
       ),
       sum(amount) over(
       partition by date_format(order_date,'%Y-%m')
       order by order_date
       ) as running_total
from sales;


SELECT
    order_id,
    order_date,
    order_status,
    CASE
        WHEN order_status IN ('COMPLETE', 'CLOSED') 
            THEN 'No Action Needed'
            
		when order_status IN ('COMPLETE','CLOSED')
			then 'no/action needed'

        WHEN order_status IN (
            'PENDING_PAYMENT',
            'PROCESSING',
            'PAYMENT_REVIEW',
            'PENDING',
            'ON_HOLD'
        )
            THEN 'Action Needed'

        WHEN order_status = 'SUSPECTED_FRAUD'
            THEN 'Risky'

        WHEN order_status = 'CANCELED'
            THEN 'Closed / No Action'

        ELSE 'Unknown / Review Required'
    END AS order_status_category
FROM orders
ORDER BY order_date;


with order_needing_action as (
select order_id,order_status
from orders
where order_status in (
'PENDING_PAYMENT',
'PROCESSING',
'PAYMENT_REVIEW',
'ON_HOLD'
)
)

select * from order_needing_action;

use demo1;

show tables;

with max_salary as (
select max(sal) as highest_salary from emp
)
select max(sal) as second_highest_salary from emp
WHERE sal < (
    SELECT highest_salary
    FROM max_salary
);


use retail_db
DELIMITER $$

DROP PROCEDURE IF EXISTS get_monthly_orders $$

CREATE PROCEDURE get_monthly_orders()
BEGIN
  SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS order_month,
    COUNT(*) AS order_count
  FROM orders
  GROUP BY order_month
  ORDER BY order_month;
END $$
DELIMITER ;

call get_monthly_orders();

DELIMITER $$

DROP PROCEDURE IF EXISTS demo_error_handler $$

CREATE PROCEDURE demo_error_handler()
BEGIN
  DECLARE had_error TINYINT DEFAULT 0;

  DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
  SET had_error = 1;

  -- Intentional example: this may fail if customer_id does not exist
  INSERT INTO orders(order_date, order_customer_id, order_status)
  VALUES (now(), 1, 'CREATED');

  IF had_error = 1 THEN
    SELECT 'An error occurred during the insert. The handler captured it.' AS message;
  ELSE
    SELECT 'Insert succeeded.' AS message;
  END IF;
END $$

DELIMITER ;

call demo_error_handler();

SELECT
  oi.order_item_product_id AS product_id,
  SUM(oi.order_item_subtotal) AS total_revenue
FROM order_items oi
GROUP BY oi.order_item_product_id
ORDER BY total_revenue DESC
LIMIT 10;

-- CREATE INDEX if not EXISTS idx_orders_customer_id
-- ON orders(order_customer_id);

SELECT
  DATE_FORMAT(order_date, '%Y-%m') AS order_month,
  COUNT(*) AS total_orders,
  SUM(CASE WHEN order_status = 'COMPLETE' THEN 1 ELSE 0 END) AS complete_orders,
  SUM(CASE WHEN order_status = 'CLOSED'   THEN 1 ELSE 0 END) AS closed_orders
FROM orders
GROUP BY order_month
ORDER BY order_month;



drop table sales;

CREATE TABLE sales (
    order_id INT,
    order_date DATE,
    amount DECIMAL(10,2)
);
     

INSERT INTO sales VALUES
(1, '2025-01-01', 100.00),
(2, '2025-01-01', 150.00),
(3, '2025-01-02', 200.00),
(4, '2025-01-02', 50.00);


SELECT order_date, SUM(amount) AS daily_total
FROM sales
GROUP BY order_date;

create table daily_sales_summary as
select order_date,
sum(amount) as daily_total from
sales
group by order_date;

select * from daily_sales_summary;

select * from order_items;

use retail_db;



-- --------------q1---------------


select o.order_date,
round(sum(oi.order_item_quantity*oi.order_item_product_price),2) as total_order_revenue
from orders  o
inner join order_items  oi
on oi.order_item_order_id=o.order_id
where o.order_status in ('COMPLETE','CLOSED') 
group by o.order_date;


select o.order_date,
sum(oi.order_item_subtotal) as total_revenue
from orders o
join order_items oi
on o.order_id=oi.order_item_order_id
where o.order_status in ('COMPLETE','CLOSED')
group by o.order_date;



-- --------------q2---------------


select p.product_id,o.order_date,
sum(oi.order_item_subtotal) as total_revenue
from orders o
join order_items oi on o.order_id=oi.order_item_order_id
join products p on p.product_id=oi.order_item_product_id
where o.order_status in('COMPLETE','CLOSED')
group by o.order_date,p.product_id;

select p.product_id,o.order_date,
sum(oi.order_item_subtotal) as revenue
from orders o
join order_items oi on o.order_id=oi.order_item_order_id
join products p on p.product_id=oi.order_item_product_id
where o.order_status in ('COMPLETE','CLOSED')
group by o.order_date,p.product_id;


-- -------------- q3 ---------------


select o.order_date,
sum(oi.order_item_subtotal) as total_revenue,
sum(sum(oi.order_item_subtotal)) over( partition by year(o.order_date),month(o.order_date)) as monthly_revenue
from orders o
join order_items oi on o.order_id=oi.order_item_order_id
join products p on p.product_id=oi.order_item_product_id
where o.order_status in('COMPLETE','CLOSED')
group by o.order_date;


select o.order_date,
sum(oi.order_item_subtotal) as total_revenue,
sum(sum(oi.order_item_subtotal))  over(partition by year(o.order_date),month(o.order_date)) as monthly_revenue
from orders o
join order_items oi on o.order_id=oi.order_item_order_id
join products p on p.product_id=oi.order_item_product_id
where o.order_status in('COMPLETE','CLOSED')
group by o.order_date;


-- -------------- q4 ---------------


select p.product_id,
sum(oi.order_item_subtotal) as total_revenue,
rank() over(order by sum(oi.order_item_subtotal) desc) as rnk
from orders o
join order_items oi on o.order_id=oi.order_item_order_id
join products p on p.product_id=oi.order_item_product_id
where o.order_status in ('COMPLETE','CLOSED')
and o.order_date='2013-07-25 00:00:00' 
group by p.product_id;


select p.product_id,
sum(oi.order_item_subtotal) as income,
rank() over(order by sum(oi.order_item_subtotal) desc) 
from orders o
join order_items oi on oi.order_item_order_id=o.order_id
join products p on p.product_id=oi.order_item_product_id
where o.order_date='2013-07-25 00:00:00'
and o.order_status in ('COMPLETE','CLOSED') 
group by p.product_id;


-- -------------- q5 ---------------


select p.product_id,
sum(oi.order_item_subtotal) as total_revenue,
dense_rank() over(order by sum(oi.order_item_subtotal) desc)
from orders o
join order_items oi on o.order_id=oi.order_item_order_id
join products p on p.product_id=oi.order_item_product_id
where o.order_status in('COMPLETE','CLOSED') 
and o.order_date='2013-07-25 00:00:00' 
group by p.product_id limit 5;


-- --------------------------------------------


