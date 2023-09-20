SELECT MONTH(rental_date) AS mes, COUNT(*) AS total_alugueis
FROM rental
GROUP BY mes
ORDER BY mes;