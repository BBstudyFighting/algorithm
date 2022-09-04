select Region
     , sum(case when category = 'Furniture' then orders end) as Furniture
     , sum(case when category = 'Office Supplies' then orders end) as 'Office Supplies'
     , sum(case when category = 'Technology' then orders end) as Technology
FROM
  (select region AS 'Region', category, count(distinct order_id) orders
   from records
   group by region, category
) as commerce
group by Region
order by Region;