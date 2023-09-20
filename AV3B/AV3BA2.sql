SELECT * FROM view_filmes_categoria;
CREATE VIEW view_filmes_categoria AS
SELECT f.film_id,f.title AS titulo,c.name AS categoria
FROM film AS f
INNER JOIN film_category AS fc ON f.film_id = fc.film_id
INNER JOIN category AS c ON fc.category_id = c.category_id;