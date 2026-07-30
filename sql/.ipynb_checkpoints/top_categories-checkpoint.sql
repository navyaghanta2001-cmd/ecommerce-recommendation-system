SELECT 
       product_category_name_english,
       COUNT(DISTINCT order_id) AS num_orders,
       SUM(total_item_value) AS total_revenue
   FROM orders_master
   GROUP BY product_category_name_english
   ORDER BY total_revenue DESC
   LIMIT 10;