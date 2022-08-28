SELECT 
    date(MIN(order_purchase_timestamp)) AS first_order_date,
    date(MAX(order_purchase_timestamp)) AS last_order_date
FROM olist_orders_dataset