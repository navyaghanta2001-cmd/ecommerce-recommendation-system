SELECT 
    order_year_month,
    SUM(total_item_value) AS monthly_revenue,
    SUM(SUM(total_item_value)) OVER (ORDER BY order_year_month) AS running_total
FROM orders_master
GROUP BY order_year_month
ORDER BY order_year_month;