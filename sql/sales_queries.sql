-- Total Sales by Region
SELECT Region,
SUM(Sales) AS TotalSales
FROM Superstore
GROUP BY Region;

-- Total Profit by Category
SELECT Category,
SUM(Profit) AS TotalProfit
FROM Superstore
GROUP BY Category;

-- Top 10 Customers
SELECT Customer_Name,
SUM(Sales) AS Revenue
FROM Superstore
GROUP BY Customer_Name
ORDER BY Revenue DESC
LIMIT 10;
