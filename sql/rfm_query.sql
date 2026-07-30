SELECT 
       customer_unique_id,
       MAX(order_purchase_timestamp) AS last_purchase_date,
       COUNT(DISTINCT order_id) AS frequency,
       SUM(total_item_value) AS monetary
   FROM orders_master
   GROUP BY customer_unique_id;