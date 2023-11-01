CREATE TABLE MarcoTeste.Pessoa (cpf varchar(15), nome varchar(50), 
	email varchar(100), 
	telefone varchar(10), 
	v INT, 
	CONSTRAINT PK_av3 PRIMARY KEY (cpf, v)
);
