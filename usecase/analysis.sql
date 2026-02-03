/* =========================================================
   Name=Abhinav Kumar
   Emp_id=TSV-715
   ========================================================= */

USE TSV_715_abhinav_kumar_gold_db;
-- 1. Revenue by City
SELECT
    c.city,
    SUM(f.total_amount) AS total_revenue
FROM fact_sales f
JOIN dim_customer c ON f.customer_key = c.customer_key
GROUP BY c.city
ORDER BY total_revenue DESC;

-- 2. Revenue by Category
SELECT
    p.product_category,
    SUM(f.total_amount) AS total_revenue
FROM fact_sales f
JOIN dim_product p ON f.product_key = p.product_key
GROUP BY p.product_category
ORDER BY total_revenue DESC;

-- 3. Daily Revenue Trend
SELECT
    f.sale_date,
    SUM(f.total_amount) AS daily_revenue
FROM fact_sales f
GROUP BY f.sale_date
ORDER BY f.sale_date;