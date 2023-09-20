SELECT first_name, last_name
FROM customer c  
WHERE EXISTS (
	SELECT 1
	FROM rental r
	WHERE r.customer_id = c.customer_id);