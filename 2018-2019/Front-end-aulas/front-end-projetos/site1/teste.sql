CREATE TABLE Carros(
CodigoCarro int not null primary key auto_increment,
marca varchar(50) not null,
modelo varchar(50) not null,
ano int,
placa varchar(7),
proprietario int not null,
CONSTRAINT prop_fk
FOREIGN KEY (proprietario)
REFERENCES Clientes(CodigoCliente));
