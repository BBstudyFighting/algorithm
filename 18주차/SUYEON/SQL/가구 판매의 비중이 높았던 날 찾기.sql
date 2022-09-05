SELECT order_date
      ,count(distinct CASE WHEN category = "Furniture" THEN order_id END) as "furniture"
      --,count(distinct order_id) as "total_count"
      ,round(count(distinct CASE WHEN category = "Furniture" THEN order_id END)/(count(distinct order_id)+0.00)*100,2) as furniture_pct
FROM records
GROUP BY order_date
HAVING COUNT(distinct order_id) >= 10 AND furniture_pct >= 40
ORDER BY furniture_pct desc, order_date