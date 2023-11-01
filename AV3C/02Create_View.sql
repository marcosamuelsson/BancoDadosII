CREATE VIEW Pessoa_View AS
SELECT p1.cpf, p1.nome, p1.email, p1.telefone
FROM Pessoa p1
WHERE p1.v = (
    SELECT MAX(p2.v)
    FROM Pessoa p2
    WHERE p2.cpf = p1.cpf
);
