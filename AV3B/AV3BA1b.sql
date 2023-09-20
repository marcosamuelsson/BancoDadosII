SELECT actor_id, first_name, last_name
FROM actor 
WHERE actor_id IN (
	SELECT actor_id
	FROM film_actor
	WHERE film_id = (
		SELECT film_id 
		FROM film 
		WHERE title = 'SUPER WYOMING')
		);