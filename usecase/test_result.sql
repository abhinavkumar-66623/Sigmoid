/* =========================================================
   Name=Abhinav Kumar
   Emp_id=TSV-715
   ========================================================= */

create database TSV_715_abhinav_kumar_qa_db;
use TSV_715_abhinav_kumar_qa_db;

-- SET @test_run_id = DATE_FORMAT(NOW(), '%Y%m%d_%H%i%s');
SET @test_run_id = STR_TO_DATE(DATE_FORMAT(NOW(), '%Y%m%d_%H%i%s'), '%Y%m%d_%H%i%s');

create table test_results(
test_run_id Datetime,
test_name varchar(100),
test_status varchar(100),
actual_value varchar(300),
expected_desc varchar(300),
details varchar(300),
run_ts datetime default current_timestamp
);



-- test 1
INSERT INTO TSV_715_abhinav_kumar_qa_db.test_results
(test_run_id, test_name, test_status, actual_value, expected_desc, details)
SELECT
  @test_run_id,
  'Bronze: Duplicate order_id check',
  CASE WHEN COUNT(*) = 0 THEN 'PASS' ELSE 'FAIL' END,
  COUNT(*),
  '0 expected',
  'order_id should be unique in Bronze layer'
FROM (
  SELECT order_id
  FROM TSV_715_abhinav_kumar_bronze_db.bronze_sales_raw
  GROUP BY order_id
  HAVING COUNT(*) > 1
) dups;



-- test 2
INSERT INTO TSV_715_abhinav_kumar_qa_db.test_results (test_run_id, test_name, test_status, actual_value, expected_desc, details)
SELECT
  @test_run_id,
  'Silver: Beauty exclusion rule',
  CASE WHEN COUNT(*) = 0 THEN 'PASS' ELSE 'FAIL' END,
  COUNT(*),
  '0 expected',
  'Beauty rows should not be promoted to Silver'
FROM TSV_715_abhinav_kumar_silver_db.silver_sales_clean
WHERE product_category = 'Beauty';
 
 
 
 -- test 3 
 
INSERT INTO TSV_715_abhinav_kumar_qa_db.test_results
(test_run_id, test_name, test_status, actual_value, expected_desc, details)
SELECT
  @test_run_id,
  'Silver: Null or blank city check',
  CASE WHEN COUNT(*) = 0 THEN 'PASS' ELSE 'FAIL' END,
  COUNT(*),
  '0 expected',
  'City should not be NULL or blank after'
FROM TSV_715_abhinav_kumar_silver_db.silver_sales_clean
WHERE city IS NULL OR TRIM(city) = '';
 
 
 -- test 4
 INSERT INTO TSV_715_abhinav_kumar_qa_db.test_results
(test_run_id, test_name, test_status, actual_value, expected_desc, details)
SELECT
  @test_run_id,
  'Silver: Invalid email check',
  CASE WHEN COUNT(*) = 0 THEN 'PASS' ELSE 'FAIL' END,
  COUNT(*),
  '0 expected',
  'Email must contain both @ and .'
FROM TSV_715_abhinav_kumar_silver_db.silver_sales_clean
WHERE email IS NOT NULL
  AND (email NOT LIKE '%@%' OR email NOT LIKE '%.%');
  
  
-- test 5
  INSERT INTO TSV_715_abhinav_kumar_qa_db.test_results
(test_run_id, test_name, test_status, actual_value, expected_desc, details)
SELECT
  @test_run_id,
  'Gold: total_amount calculation check',
  CASE WHEN COUNT(*) = 0 THEN 'PASS' ELSE 'FAIL' END,
  COUNT(*),
  '0 expected',
  'total_amount must equal quantity * unit_price within tolerance'
FROM TSV_715_abhinav_kumar_gold_db.fact_sales
WHERE ABS(total_amount - (quantity * unit_price)) > 0.01;
 
-- test 6

INSERT INTO TSV_715_abhinav_kumar_qa_db.test_results
(test_run_id, test_name, test_status, actual_value, expected_desc, details)
SELECT
  @test_run_id,
  'Completeness: Silver to Gold order_id check',
  CASE WHEN COUNT(*) = 0 THEN 'PASS' ELSE 'FAIL' END,
  COUNT(*),
  '0 expected',
  'All Silver order_id must exist in Gold fact_sales'
FROM TSV_715_abhinav_kumar_silver_db.silver_sales_clean s
LEFT JOIN TSV_715_abhinav_kumar_gold_db.fact_sales f
  ON s.order_id = f.order_id
WHERE f.order_id IS NULL; 

drop table test_results;
select * from test_results;


