SELECT 
       seller_id,
       COUNT(DISTINCT order_id) AS num_orders,
       SUM(total_item_value) AS total_revenue
   FROM orders_master
   GROUP BY seller_id
   ORDER BY total_revenue DESC
   LIMIT 10;