/*Aluno Marco Antônio Samuelsson, BCC 2023.4*/

SELECT * FROM chicago

SELECT AVG("Annual Salary") from chicago /*Média de ganho dos funcionários que trabalham por hora*/
WHERE ("Salary or Hourly") = 'Salary'
UNION 
SELECT AVG("Hourly Rate" * 251 * "Typical Hours"/5) from chicago /*Média de ganho dos funcionários que trabalham por hora*/
WHERE ("Salary or Hourly") = 'Hourly'

UPDATE chicago
SET "Hourly Rate" = "Hourly Rate" * 1.36 /*Aumentando 36% a taxa de hora para igualar as médias*/
WHERE ("Salary or Hourly") = 'Hourly'
