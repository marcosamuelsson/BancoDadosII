-- Crie o trigger
CREATE TRIGGER meu_trigger03 AFTER UPDATE ON Pessoa
FOR EACH ROW
    -- Modificar o dado após a atualização
    UPDATE Pessoa
    SET cpf = '101.502.793-77'
    WHERE v = NEW.v;
