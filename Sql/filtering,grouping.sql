-- 1
SELECT DISTINCT country 
FROM customers
ORDER BY country;

-- 2
SELECT DISTINCT state
FROM customers
ORDER BY state DESC;

-- 3
SELECT customerNumber, customerName, country
FROM customers
WHERE country != 'USA'
ORDER BY customerNumber DESC;

-- 4
SELECT *
FROM offices
WHERE city = 'Paris';

-- 5
SELECT customerNumber, customerName, country, state
FROM customers
WHERE country = 'USA' and state = 'CA'
ORDER BY customerName DESC;

-- 6
SELECT customerNumber, customerName, country, state
FROM customers
WHERE country = 'USA' 
and state = 'CA' or 'NY'
ORDER BY customerNumber DESC;

-- 7
SELECT customerNumber, customerName, state
FROM customers
WHERE state in ('CA', 'NY', 'CT', 'PA')
ORDER BY customerNumber DESC;

-- 8
SELECT productCode, productName, quantityInStock
FROM products
WHERE quantityInStock < 1000
ORDER BY quantityInStock;

-- 9
SELECT productCode, productName, quantityInStock
FROM products
WHERE quantityInStock BETWEEN 2000 and 3000;

-- 10
SELECT customerNumber, customerName, phone
FROM customers
WHERE phone LIKE '%555';

-- 11
SELECT productCode, quantityInStock
FROM products
ORDER BY quantityInStock DESC
LIMIT 5;

-- 12
SELECT jobTitle, COUNT(*) as count_job
FROM employees
GROUP BY jobTitle
ORDER BY count_job DESC;

-- 13
SELECT country, COUNT(*) as count_country
FROM customers
GROUP BY country
ORDER BY count_country DESC;

-- 14
SELECT orderNumber, SUM(quantityOrdered * priceEach) as total
FROM orderdetails
GROUP BY orderNumber
ORDER BY total DESC;

-- 15
SELECT year(orderDate), COUNT(orderNumber)
FROM orders
GROUP BY year(orderDate);

-- 16
SELECT productline, MAX(quantityInStock) as max_stock
FROM products
GROUP BY productLine
having max_stock < 9000;

-- 17
SELECT orderNumber, sum(quantityOrdered) as itemsCount, SUM(priceeach * quantityOrdered) as total
FROM orderdetails
GROUP BY orderNumber
HAVING itemsCount >= 500 and total >= 50000;