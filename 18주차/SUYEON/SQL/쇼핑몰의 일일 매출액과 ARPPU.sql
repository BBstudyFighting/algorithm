SELECT DATE(A.order_purchase_timestamp) AS dt
	   , COUNT(DISTINCT B.ORDER_ID) AS pu, ROUND(SUM(B.payment_value), 2) AS revenue_daily
       , ROUND((SUM(B.payment_value) / COUNT(DISTINCT B.ORDER_ID)), 2) AS arppu
FROM olist_orders_dataset A, olist_order_payments_dataset B 
WHERE A.order_id = B.order_id
AND A.order_purchase_timestamp > '2018-01-01'
GROUP BY DATE(A.order_purchase_timestamp)
ORDER BY DATE(A.order_purchase_timestamp);