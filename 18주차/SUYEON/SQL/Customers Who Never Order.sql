select name AS 'Customers'
from Customers
left join orders 
on orders.customerId = Customers.id
where orders.customerId is null