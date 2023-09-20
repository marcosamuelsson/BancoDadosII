SELECT actor.first_name, actor.last_name, film.title
FROM actor
RIGHT JOIN film_actor ON actor.actor_id = film_actor.actor_id
RIGHT JOIN film ON film_actor.film_id = film.film_id;
