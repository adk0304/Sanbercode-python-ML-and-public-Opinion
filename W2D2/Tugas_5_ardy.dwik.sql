#Order Number, Order Date, Customer Name, City, Country, Quantity Ordered, Product Name
#all customer -> 1992 Ferrari 360 spider red -> 1 agustus 2004 - 1 desember 2004
#tabel customers,orders, orderdetails,products
USE classicmodels;
select ord.orderNumber 'Order Number', ord.orderDate 'Order Date',cu.customername 'Customer Name', cu.city 'City', cu.country 'Country', ordd.quantityOrdered 'Quantity Ordered', pro.productName 'Product Name'
from customers cu
inner join orders ord using (customerNumber)
inner join orderdetails ordd on ord.orderNumber = ordd.orderNumber
inner join products pro on ordd.productCode = pro.productCode
where pro.productName = "1992 Ferrari 360 spider red" and ord.orderDate between '2004-08-01' and '2004-12-01';