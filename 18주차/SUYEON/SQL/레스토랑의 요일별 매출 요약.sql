select round(avg(sum_bill), 2)
from (
	select day, sum(total_bill) sum_bill
	from tips
	group by day)