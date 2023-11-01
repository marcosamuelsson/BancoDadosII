-- Crie o trigger
CREATE TRIGGER meu_trigger02 BEFORE INSERT ON Pessoa
FOR EACH ROW
    -- Modificar o valor antes da inserção
    SET NEW.v = '2';
