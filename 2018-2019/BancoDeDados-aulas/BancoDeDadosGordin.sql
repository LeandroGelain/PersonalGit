create database Escola;
use Escola;

create table professores(
	idprofessores int not null primary key auto_increment,
    nome varchar(100)
);
create table Disciplina (
	codDisciplina int not null primary key auto_increment,
    nomeDisciplina varchar(45),
    professores_idprofessores int not null,
    foreign key(professores_idprofessores) references professores(idprofessores)
);
create table salas (
	idsalas int not null primary key auto_increment,
    numero int not null,
    localizacao varchar(45)
);
create table turmas (
	idturmas int not null primary key auto_increment,
    nome varchar(45),
	serie varchar(45),
    salas_idsalas int not null,
    foreign key(salas_idsalas) references salas(idsalas)
);
create table Disciplina_has_turmas (
	CodDiscTurma int not null primary key auto_increment,
    Disciplina_codDisciplina int not null,
    turmas_idturmas int not null,
    foreign key(Disciplina_codDisciplina) references Disciplina (codDisciplina),
    foreign key(turmas_idturmas) references turmas (idturmas)
);

#Adicionar dados 
INSERT INTO professores(nome)
VALUES("João Ricardo Favan"),("Luís Hilário Tobler Garcia"),("Tsen Chung Kang"),("Marçal Luiz Bissoli");

select* from professores;

INSERT INTO Disciplina(nomeDisciplina, professores_idprofessores)
VALUES ("IOT - Internet das Coisas","1");
INSERT INTO Disciplina(nomeDisciplina, professores_idprofessores)
VALUES ("Lógica de Programação","2");
INSERT INTO Disciplina(nomeDisciplina, professores_idprofessores)
VALUES ("Sociedade,Tecnologia e Inovação","3");
INSERT INTO Disciplina(nomeDisciplina, professores_idprofessores)
VALUES ("Programação FRONT-END","1");
INSERT INTO Disciplina(nomeDisciplina, professores_idprofessores)
VALUES ("Geometria Analítica","4");

select * from Disciplina;

INSERT INTO salas(numero, localizacao)
values ("1","BLOCO 1 - TÉRREO");
INSERT INTO salas(numero, localizacao)
values ("2","BLOCO 1 - SEGUNDO ANDAR");
INSERT INTO salas(numero, localizacao)
values ("3","BLOCO 2 - TÉRREO");
INSERT INTO salas(numero, localizacao)
values ("4","BLOCO 2 - SEGUNDO ANDAR");

select * from salas;

INSERT INTO turmas(nome, serie, salas_idsalas)
VALUES("BDAG","1° TERMO",1);
INSERT INTO turmas(nome, serie, salas_idsalas)
VALUES("MAP","1° TERMO",2);
INSERT INTO turmas(nome, serie, salas_idsalas)
VALUES("BDAG","2° TERMO",3);
INSERT INTO turmas(nome, serie, salas_idsalas)
VALUES("MAP","2° TERMO",4);

select * from turmas;

INSERT INTO Disciplina_has_turmas(Disciplina_codDisciplina, turmas_idturmas)
VALUES(4,4);
INSERT INTO Disciplina_has_turmas(Disciplina_codDisciplina, turmas_idturmas)
VALUES(3,2);
INSERT INTO Disciplina_has_turmas(Disciplina_codDisciplina, turmas_idturmas)
VALUES(1,3);
INSERT INTO Disciplina_has_turmas(Disciplina_codDisciplina, turmas_idturmas)
VALUES(2,1);

#ATIVIDADE 1
select d.nomeDisciplina, p.nome
from Disciplina d 
join professores p
on d.professores_idprofessores = p.idprofessores;

#ATIVIDADE 2
select t.nome, t.serie, d.nomeDisciplina
from turmas t
join Disciplina_has_turmas dht
on dht.turmas_idturmas = t.idturmas
join Disciplina d
on d.codDisciplina = dht.Disciplina_codDisciplina;

#ATIVIDADE 3
select t.nome, s.numero, s.localizacao
from turmas t 
join salas s
on t.salas_idsalas = s.idsalas;

#ATIVIDADE 4
select p.nome, d.nomeDisciplina, t.nome, t.serie
from turmas t
join Disciplina_has_turmas dht
on dht.turmas_idturmas = t.idturmas
join Disciplina d
on d.codDisciplina = dht.Disciplina_codDisciplina
join professores p
on d.professores_idprofessores = p.idprofessores;

#ATIVIDADE 5
create table if not exists professores_log (
idprofessor int not null primary key auto_increment,
old_idprofessor int,
new_idprofessor int,
old_nome varchar(100),
new_nome varchar(100),
acao varchar(100),
data datetime default current_timestamp
);
create table if not exists turmas_log (
idturmas int not null primary key auto_increment,
old_idturmas int,
new_idturmas int,
old_nome varchar(100),
new_nome varchar(100),
old_serie varchar(100),
new_serie varchar(100),
old_id_salas int,
new_id_salas int,
acao varchar(100),
data datetime default current_timestamp
);

##PROFESSORES

create trigger professor_insert after insert on professores
for each row
insert into professores_log(new_idprofessor, new_nome, acao) 
values(new.idprofessor, new.nome, "INSERT");

create trigger professores_delete before delete on professores
for each row
insert into professores_log(old_idprofessor, old_nome, acao) 
values(old.idprofessor, old.nome, old.valor, "DELETE");

create trigger professores_update after update on professores
for each row
insert into professores_log(old_idprofessor, old_nome, new_idprofessor, new_nome,acao) 
values (old.idprofessor, old.nome, new.idprofessor, new.nome, "UPDATE");

##TURMAS
create trigger turma_insert after insert on turmas for each row
insert into turmas_log(new_idturmas, new_nome, new_serie, new_id_salas, acao)
values(new.idturmas, new.nome, new.serie, new.salas_idsalas, "INSERT");

create trigger turma_update before update on turmas for each row
insert into turmas_log(old_idturmas, old_nome, old_serie, old_id_salas, new_idturmas, new_nome, new_serie, new_id_salas, acao)
values(old.idturmas, old.nome, old.serie, old.salas_idsalas, new.idturmas, new.nome, new.serie, new.salas_idsalas, "UPDATE");

create trigger turma_delete before delete on turmas for each row
insert into turmas_log(old_idturmas, old_nome, old_serie, old_id_salas, acao)
values(old.idturmas, old.nome, old.serie, old.salas_idsalas, "DELETE");

#Atividade 6

insert into professores (nome) values ("Alann");
update professores set nome = "Alan Siriani" where idprofessores = 6;
delete from professores where idprofessores = 6;
select * from professores_log;

insert into turmas (nome, serie, salas_idsalas) values ("Mecanizaação", "3", 3);
update turmas set nome = "Mecanização" where idturmas = 6;
delete from turmas where idturmas = 6;
select * from turmas_log;