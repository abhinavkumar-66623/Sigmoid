-- Identify peak order dates
select date(order_date),count(date(order_date)) from orders
group by date(order_date) order by count(date(order_date)) desc;

-- Find dates with high order value
select date(order_date),count(date(order_date)) from orders
group by date(order_date) having count(date(order_date))>120 order by count(date(order_date));

-- compute revenue for second order id
select order_item_order_id,sum(order_item_quantity*order_item_product_price) from order_items where order_item_order_id=2;

-- compute revenue per order
select order_item_order_id,sum(order_item_quantity*order_item_product_price) 
from order_items 
group by order_item_order_id;


-- produce monthly order count for reporting
select month(order_date),year(order_date),count(month(order_date)) from orders
group by month(order_date),year(order_date) order by month(order_date);

use demo1;

create or replace view deptno20 as
select *
from emp
where deptno=20;

INSERT INTO deptno20 VALUES 
(9001,'ARJUN','NAYAK',7782,'1982-01-23',1300.00,NULL,20);

select * from deptno20;

SELECT view_definition
FROM information_schema.views
WHERE table_schema = DATABASE()
  AND table_name = 'count_per_dept';
     

CREATE OR REPLACE VIEW emp_above_avg_sal AS
SELECT e.ename, e.sal
FROM emp e
JOIN (
    SELECT AVG(sal) AS avg_sal
    FROM emp
) a
ON e.sal > a.avg_sal;



SELECT view_definition
FROM information_schema.views
WHERE table_schema = DATABASE()
  AND table_name = 'emp_above_avg_sal';
  
SELECT table_name
FROM information_schema.views
WHERE table_schema = DATABASE();