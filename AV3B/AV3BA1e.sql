SELECT actor.first_name, actor.last_name, film_actor.film_id
FROM actor
INNER JOIN film_actor ON actor.actor_id = film_actor.actor_id;