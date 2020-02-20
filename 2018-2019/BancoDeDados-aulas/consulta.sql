use escola;

-- 1 - Faça uma consulta com o nome da disciplina e o professor responsável por ela
select d.nome as Disciplina, p.nome as Professor
	from disciplinas d
		inner join professores p
			where d.id_professor = p.id;
            
-- 2 - Faça uma consulta com o nome da turma, série e nome da disciplina de cada turma 
select t.nome as Turma, t.serie as Série, d.nome as Disciplina
	from disciplinas_turmas dt
		inner join turmas t
			on dt.id_turma = t.id
		inner join disciplinas d
			on dt.id_disciplina = d.id;

-- 3 - Faça uma consulta com o nome da turma, o número e localização da sala de cada turma.
select t.nome as Turma, s.numero as Numero, s.localizacao as Localização
	from turmas t
		inner join salas s
			on t.id_sala = s.id;
            
-- 4 - Faça uma consulta com o nome de todas as disciplinas de um professor e o nome e série da turma para quais essas são ministradas 
select p.nome as Professor, d.nome as Disciplina, t.nome as Turma, t.serie as Serie
	from disciplinas_turmas dt
		inner join disciplinas d
			on dt.id_disciplina = d.id
		inner join professores p
			on d.id_professor = p.id
		inner join turmas t
			on dt.id_turma = t.id;

-- 5 - Implemente uma tabela de Log para as tabelas de Professores e Turmas. Utilizando triggers, faça gatilhos para inserção, remoção e alteração de registros.
create table if not exists professores_log (
	id int not null primary key auto_increment,
    old_id int,
    new_id int,
    old_nome varchar(100),
    new_nome varchar(100),
    acao varchar(100),
    data datetime default current_timestamp
);
create table if not exists turmas_log (
	id int not null primary key auto_increment,
    old_id int,
    new_id int,
    old_nome varchar(100),
    new_nome varchar(100),
    old_serie varchar(100),
    new_serie varchar(100),
    old_id_sala int,
    new_id_sala int,
    acao varchar(100),
    data datetime default current_timestamp
);
-- Professores
create trigger professores_update after update
	on professores
		for each row
			insert into professores_log (old_id, old_nome, new_id, new_nome, acao) values (old.id, old.nome, new.id, new.nome, 'update');
create trigger professores_delete after delete
	on professores
		for each row
			insert into professores_log (old_id, old_nome, acao) values (old.id, old.nome, 'delete');
create trigger professores_insert after insert
	on professores
		for each row
			insert into professores_log (new_id, new_nome, acao) values (new.id, new.nome, 'insert');
 
 select * from turmas;

 -- Turmas
create trigger turmas_update after update
	on turmas
		for each row
			insert into turmas_log (old_id, old_nome, old_serie, old_id_sala, new_id, new_nome, new_serie, new_id_sala, acao) values (old.id, old.nome, old.serie, old.id_sala, new.id, new.nome, new.serie, new.id_sala, 'update');
create trigger turmas_delete after delete
	on turmas
		for each row
			insert into turmas_log (old_id, old_nome, old_serie, old_id_sala, acao) values (old.id, old.nome, old.serie, old.id_sala, 'delete');
create trigger turmas_insert after insert
	on turmas
		for each row
			insert into turmas_log (new_id, new_nome, new_serie, new_id_sala, acao) values (new.id, new.nome, new.serie, new.id_sala, 'insert');

-- 6 - Teste todos os gatilhos desenvolvidos.
-- Professores
insert into professores (nome) values ('Eloiza');
update professores set nome = 'Eloiza C.' where id = 4;
delete from professores where id = 4;
select * from professores_log;

-- Turmas
insert into turmas (nome, serie, id_sala) values ('Big Map', '1 termo', 1);
update turmas set serie = '2 termo' where id = 9;
delete from turmas where id = 9;
select * from turmas_log;