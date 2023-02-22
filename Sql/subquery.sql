-- 1

SELECT productCode, productName, MSRP
FROM products
WHERE MSRP > (SELECT AVG(MSRP) FROM products)
ORDER BY MSRP;

-- 2

SELECT customerNumber, customerName
FROM customers
WHERE customerNumber IN (
    SELECT DISTINCT customerNumber
    FROM orders
    WHERE orderDate BETWEEN '2003-01-06' AND '2003-03-26'
)
ORDER BY customerNumber;

-- 3

SELECT productCode, productName, productLine, MSRP
FROM products
WHERE productLine = 'Classic Cars'
AND MSRP = (
  SELECT MAX(MSRP)
  FROM products
  WHERE productLine = 'Classic Cars'
);

-- 4

SELECT customerNumber, customerName, country
FROM customers
WHERE country = (
  SELECT country
  FROM customers
  GROUP BY country
  ORDER BY COUNT(*) DESC
  LIMIT 1
);


SELECT customerNumber, customerName, country
FROM customers
WHERE country IN (
    SELECT MAX(country)
    FROM customers
)
ORDER BY customerNumber;


-- 5
-- ???

SELECT customerNumber, customerName, MAX(c) AS order_count
FROM customers
WHERE customerNumber = (
	SELECT customerNumber
	FROM orders
	WHERE COUNT(*) = (
		SELECT MAX(c)
		FROM (
			SELECT COUNT(*) as c
			FROM orders
			GROUP BY customerNumber
            )as l_c
	) 
);

SELECT customers.customerNumber, customerName, COUNT(orders.customerNumber) as order_count
FROM customers
JOIN orders ON customers.customerNumber = orders.customerNumber
GROUP BY orders.customerNumber
ORDER BY order_count DESC
LIMIT 1;

-- 6

SELECT p.productCode, p.productName
FROM orderdetails o
JOIN products p ON o.productCode = p.productCode
JOIN orders c ON o.orderNumber = c.orderNumber
WHERE YEAR(c.orderDate) = 2004
ORDER BY p.productCode DESC;

-- 문제 6

SELECT DISTINCT p.productCode, p.productName
FROM orders o
INNER JOIN orderdetails od USING (orderNumber)
INNER JOIN products p USING (productCode)
WHERE o.orderDate BETWEEN '2004-01-01' AND '2004-12-31'
ORDER BY p.productCode DESC;

-- WHERE YEAR(c.orderDate) = 2004
-- WHERE productCode IN (SELECT productCode FROM orders WHERE DATE_FORMAT(orderDate, '%Y') = '2004')