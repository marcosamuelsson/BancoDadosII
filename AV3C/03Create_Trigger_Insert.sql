CREATE TRIGGER meu_trigger AFTER INSERT ON Pessoa
FOR EACH ROW
    -- Inserir um registro na tabela_destino com os mesmos valores do novo registro em tabela_origem
    INSERT INTO Pessoa (cpf, nome, email, telefone, v)
    VALUES (NEW.cpf, NEW.nome, NEW.email, NEW.telefone, NEW.v);

