SELECT first_name, last_name
FROM actor 
WHERE actor_id IN (
	SELECT actor_id
	FROM film_actor);