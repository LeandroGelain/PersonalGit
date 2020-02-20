drop database if exists cinema;
create database cinema;
use cinema;

create table atores(
	codigo_ator int primary key not null auto_increment,
    nome varchar(100) not null,
    nacionalidade varchar(50),
    idade int );
  
create table diretores(
	codigo_diretor int primary key not null auto_increment,
    nome varchar(100) not null,
    nacionalidade varchar(50)    
); 
 
create table filmes(
	codigo_filme int primary key not null auto_increment,
    nome varchar(150) not null,
    genero varchar(50),
    duracao varchar(20) not null,
    faixa_etaria int not null,
    cod_diretor int not null,
    foreign key (cod_diretor) references diretores(codigo_diretor)
);
    
create table atores_filmes(
	codigo int primary key not null auto_increment,
    cod_ator int not null,
    cod_filme int not null,
    cash double not null,
    foreign key (cod_ator) references atores(codigo_ator),
    foreign key (cod_filme) references filmes(codigo_filme)
);

# Inserção de dados na tabela atores
INSERT INTO `atores` (`nome`,`nacionalidade`,`idade`) VALUES ("Dustin Walker","Sint Maarten",40),("Jemima Compton","Greece",27),("Brenda Beck","El Salvador",37),("Yvonne Foster","Venezuela",51),("Owen Leon","Saudi Arabia",46),("Wayne Guerrero","South Sudan",36),("Catherine Nolan","Israel",31),("Oren Hale","Cook Islands",54),("Shea Dorsey","British Indian Ocean Territory",33),("Alec Walters","Albania",38);
INSERT INTO `atores` (`nome`,`nacionalidade`,`idade`) VALUES ("Erich Stevenson","Isle of Man",25),("Charles Cervantes","French Southern Territories",27),("Elton Kim","South Sudan",51),("Stone Doyle","Trinidad and Tobago",55),("Kyra Brewer","Georgia",42),("Illana Cobb","Hungary",53),("Richard Ruiz","Monaco",48),("Marshall Mendoza","Ecuador",58),("Cathleen Shelton","Tokelau",57),("Roanna Rosa","France",48);
INSERT INTO `atores` (`nome`,`nacionalidade`,`idade`) VALUES ("Gillian Livingston","Sao Tome and Principe",58),("Salvador Austin","Tanzania",56),("Dolan Barlow","Netherlands",27),("Yuri Rodgers","Greece",30),("Quynn Moon","Djibouti",51),("Seth Campos","Ukraine",41),("Wyoming Summers","Estonia",40),("Adam Meyer","Qatar",44),("Hop Miller","Jersey",26),("Jeanette Hinton","Guam",44);
INSERT INTO `atores` (`nome`,`nacionalidade`,`idade`) VALUES ("Maisie Valentine","Jordan",31),("Leo Mcpherson","Kenya",32),("Barrett Villarreal","Chad",59),("Barry Harris","Guam",42),("Sean Forbes","Pitcairn Islands",27),("Ciaran Cantrell","Bosnia and Herzegovina",60),("Austin Hammond","Latvia",31),("Jin Branch","Solomon Islands",57),("Lael Armstrong","Oman",42),("Deacon Merritt","Macedonia",34);
INSERT INTO `atores` (`nome`,`nacionalidade`,`idade`) VALUES ("Kamal Sweeney","San Marino",47),("Madaline Diaz","Pitcairn Islands",25),("Cooper Sloan","Mozambique",48),("Wing Workman","Kiribati",34),("Jin Delgado","Georgia",40),("Zachary Fox","Mauritania",55),("Upton Medina","Cocos (Keeling) Islands",35),("Grant Delgado","Burundi",51),("Tanner Wall","Grenada",45),("Maya Calderon","Chile",47);
INSERT INTO `atores` (`nome`,`nacionalidade`,`idade`) VALUES ("Reed Brock","Pitcairn Islands",31),("Kenyon Slater","Greece",54),("Tate Conley","Finland",37),("Sandra Stephenson","Tokelau",27),("Montana Hughes","Philippines",45),("Faith Barker","Afghanistan",38),("Adrian Byrd","Papua New Guinea",39),("Lucy Noble","Western Sahara",32),("Maite Hart","Dominica",37),("Yetta Osborn","Suriname",57);
INSERT INTO `atores` (`nome`,`nacionalidade`,`idade`) VALUES ("Reuben Harmon","Timor-Leste",32),("Juliet Sanders","Saudi Arabia",32),("Orson Delgado","Kyrgyzstan",39),("Montana Hester","Svalbard and Jan Mayen Islands",58),("Joshua Mosley","Holy See (Vatican City State)",47),("Blaze Knowles","Ghana",47),("Buffy Gilliam","Gambia",51),("Oprah Hicks","Thailand",42),("Malcolm Whitaker","Costa Rica",27),("Cassandra Rose","Saint Barthélemy",53);
INSERT INTO `atores` (`nome`,`nacionalidade`,`idade`) VALUES ("Jelani Willis","Martinique",34),("Tanner Carlson","Uzbekistan",40),("Amethyst Newton","American Samoa",30),("Kirestin Battle","Aruba",43),("Hu Daniels","Sweden",53),("Zephania Mcguire","French Southern Territories",33),("Elizabeth Herrera","Bonaire, Sint Eustatius and Saba",35),("Ora Morton","Azerbaijan",28),("Joy Franco","Argentina",31),("Shay Stewart","Iraq",38);
INSERT INTO `atores` (`nome`,`nacionalidade`,`idade`) VALUES ("Clementine Miranda","France",41),("Evan Gates","Guinea",42),("Yuri Kirkland","United Kingdom (Great Britain)",52),("Wendy Benson","Christmas Island",35),("Holly Gallegos","British Indian Ocean Territory",32),("Nasim Lloyd","Uruguay",44),("Harper Dean","Virgin Islands, British",49),("Zachary Cardenas","Bosnia and Herzegovina",43),("Laith King","Taiwan",49),("Austin Howell","Nicaragua",48);
INSERT INTO `atores` (`nome`,`nacionalidade`,`idade`) VALUES ("Lance Snider","Nicaragua",30),("Brian Love","Guyana",27),("Yuri Alvarez","Bangladesh",59),("Kyle Figueroa","Australia",51),("Rajah Washington","Armenia",28),("Grady Clements","Falkland Islands",40),("Ursula James","Macedonia",38),("Kylynn Sutton","Spain",29),("Nyssa Gates","Pakistan",47),("Basia Wheeler","China",48);

# Inserção de dados na tabela diretores
INSERT INTO `diretores` (`nome`,`nacionalidade`) VALUES ("Hamish Howe","Taiwan"),("Shana Mccormick","American Samoa"),("Brock Santos","Viet Nam"),("Jamalia Barker","Saint Vincent and The Grenadines"),("Palmer Villarreal","Guyana"),("Cullen Dickson","Bangladesh"),("Ross Durham","Nicaragua"),("Cain Rich","Fiji"),("Aurora Blake","South Africa"),("Guy Landry","Kiribati");
INSERT INTO `diretores` (`nome`,`nacionalidade`) VALUES ("Mannix Bryant","Sri Lanka"),("Glenna Melton","Mauritania"),("Brent Bonner","Congo, the Democratic Republic of the"),("Desiree Davis","Croatia"),("Jolie Santos","Egypt"),("Melinda Thornton","Liberia"),("Constance Frank","Mauritania"),("Lael Ball","Virgin Islands, United States"),("Wyoming Norton","Zambia"),("Garrison Nieves","Mexico");

# Inserção de dados na tabela  filmes
INSERT INTO `filmes` (`nome`,`genero`,`duracao`,`Faixa_etaria`,`cod_diretor`) VALUES ("scelerisque, lorem","pede,",102,12,15),("Fusce feugiat. Lorem ipsum dolor","Nunc",91,12,11),("placerat, orci lacus","sapien.",99,15,6),("dictum magna. Ut","massa.",88,15,3),("rutrum eu, ultrices sit amet,","primis",100,15,10),("per conubia","fermentum",51,15,4),("aliquet","Vivamus",62,13,5),("Etiam laoreet,","dignissim",120,18,7),("vulputate dui,","molestie.",103,12,17),("orci. Donec nibh. Quisque nonummy","ac",113,15,15);
INSERT INTO `filmes` (`nome`,`genero`,`duracao`,`Faixa_etaria`,`cod_diretor`) VALUES ("id sapien. Cras dolor","semper",50,15,10),("ut, nulla. Cras eu tellus","cursus.",69,17,3),("aliquam, enim nec tempus scelerisque,","ullamcorper.",79,10,19),("cursus, diam at","Integer",115,15,6),("nec","ipsum",84,9,15),("orci luctus et ultrices","Quisque",79,12,2),("cursus","magna.",60,10,14),("ac mattis","elementum,",55,10,6),("et, rutrum eu, ultrices sit","lobortis",74,10,9),("sed dictum eleifend, nunc","hymenaeos.",70,17,16);

# Inserção de atores nos filmes com cash
INSERT INTO `atores_filmes` (`cod_ator`,`cod_filme`,`cash`) VALUES (56,17,"82734.31"),(75,9,"92028.83"),(95,19,"12246.24"),(45,7,"11041.32"),(14,15,"81119.70"),(85,20,"75906.53"),(88,12,"41354.17"),(48,17,"72116.36"),(85,1,"10899.22"),(40,2,"14372.08");
INSERT INTO `atores_filmes` (`cod_ator`,`cod_filme`,`cash`) VALUES (60,2,"48288.25"),(100,18,"80316.91"),(82,6,"36153.57"),(41,10,"81556.66"),(48,7,"84010.49"),(8,18,"65058.87"),(5,12,"54486.19"),(59,12,"20300.49"),(44,13,"69058.26"),(19,8,"25148.95");
INSERT INTO `atores_filmes` (`cod_ator`,`cod_filme`,`cash`) VALUES (24,10,"76935.93"),(6,9,"39757.66"),(77,6,"81200.39"),(76,7,"50952.02"),(53,19,"48952.60"),(85,10,"80609.33"),(65,14,"93858.32"),(53,16,"02200.65"),(15,13,"37061.44"),(47,1,"11733.53");
INSERT INTO `atores_filmes` (`cod_ator`,`cod_filme`,`cash`) VALUES (66,3,"92862.84"),(45,17,"51041.61"),(10,5,"93923.25"),(64,4,"45445.12"),(2,1,"18558.03"),(1,8,"77913.14"),(49,20,"24156.69"),(2,20,"33085.25"),(72,2,"01524.16"),(33,2,"52072.52");
INSERT INTO `atores_filmes` (`cod_ator`,`cod_filme`,`cash`) VALUES (27,20,"4980.38"),(66,14,"41685.36"),(27,6,"15572.79"),(80,16,"65453.70"),(54,20,"21610.76"),(75,1,"11937.20"),(45,13,"49358.10"),(77,15,"49553.67"),(52,9,"87835.47"),(63,6,"92488.66");
INSERT INTO `atores_filmes` (`cod_ator`,`cod_filme`,`cash`) VALUES (1,6,"51269.92"),(85,18,"01308.00"),(7,17,"74001.99"),(35,19,"1613.47"),(99,6,"24340.50"),(13,20,"28081.46"),(89,9,"71268.37"),(93,11,"19424.99"),(80,3,"15442.25"),(35,1,"42376.04");
INSERT INTO `atores_filmes` (`cod_ator`,`cod_filme`,`cash`) VALUES (57,16,"34859.64"),(13,17,"39015.74"),(7,14,"61161.69"),(71,7,"63380.11"),(65,17,"74860.38"),(3,6,"89878.28"),(5,5,"28303.33"),(65,13,"75280.36"),(32,4,"36652.93"),(67,19,"67284.00");
INSERT INTO `atores_filmes` (`cod_ator`,`cod_filme`,`cash`) VALUES (81,6,"13175.45"),(87,14,"21944.54"),(64,8,"04985.03"),(67,17,"05979.01"),(76,13,"67521.98"),(16,18,"67982.29"),(64,1,"60673.23"),(43,5,"93525.34"),(52,11,"97318.68"),(13,18,"23472.16");
INSERT INTO `atores_filmes` (`cod_ator`,`cod_filme`,`cash`) VALUES (27,1,"13789.34"),(33,8,"01338.21"),(86,18,"15988.09"),(6,8,"74473.91"),(13,20,"13149.87"),(90,19,"08736.26"),(70,8,"08458.05"),(23,16,"34914.11"),(40,11,"01542.05"),(41,13,"48681.73");
INSERT INTO `atores_filmes` (`cod_ator`,`cod_filme`,`cash`) VALUES (33,19,"60772.95"),(10,20,"24540.79"),(90,3,"43028.73"),(51,15,"76522.69"),(42,20,"40645.66"),(93,10,"05125.22"),(40,1,"79074.94"),(35,6,"45163.96"),(28,3,"25071.10"),(34,8,"60147.11");

select f.Codigo_filme, f.nome, f.genero, f.duracao, f.faixa_etaria, d.nome
from filmes f
join diretores d
on f.cod_diretor = d.codigo_diretor;

select f.nome, a.nome, af.cash
from atores_filmes af
join filmes f
on af.cod_filme = f.codigo_filme
join atores a
on af.cod_ator = a.codigo_ator
order by af.cash desc;

select d.nome, d.nacionalidade
from diretores d
union
select a.nome, a.nacionalidade
from atores a;

select * from atores;

select * from diretores;

select * from filmes;

select * from atores_filmes;

# Subqueries

# Quais atores tiveram cash maiores que a média (subqueri dependente)
select * 
from atores_filmes as af1
where af1.cash > (
	select avg(af2.cash)
    from atores_filmes as af2
    where af2.cod_ator = af1.cod_ator
);


select * from atores_filmes where cash> (select avg(af.cash) from atores_filmes as af);

# Qual maior cash no filme 1 (subquerie independente)
select af1.*, (
	select max(af2.cash)
    from atores_filmes as af2
    where af2.cod_filme = 1
) as maior_cash
from atores_filmes as af1
where af1.cod_filme = 1;

# Joins
# Selecionar valores de filmes e diretores
Select *
from filmes as f
join diretores as d
on f.cod_diretor = d.codigo_diretor;

select f.nome, d.nome, d.nacionalidade
from filmes as f
join diretores as d
on f.cod_diretor = d.codigo_diretor;






# Selecionar registros de atores e filmes
select *
from atores_filmes as af
right join filmes as f
on af.cod_filme = f.codigo_filme
left join atores as a
on af.cod_ator = a.codigo_ator;
select * from filmes;
# Selecionando apenas nome do ator, do filme e cassh
select f.nome as 'nome_filme',
	   a.nome as 'nome_ator',
       af.cash as 'cachê'
from atores_filmes as af
right join filmes as f
on af.cod_filme = f.codigo_filme
left join atores as a
on af.cod_ator = a.codigo_ator
order by af.cash;

#Unions
# selecionar nome e nacionalidade de todos (atores e diretor) 
select nome, idade
from atores
union
select nome
from diretores
order by nome;

select * from atores order by nome;
select * from diretores order by nome;

# selecionar nome e nacionalidade de todos (atores e diretor) envolvidos em um filme
select a.nome, a.nacionalidade
from atores_filmes as af
right join filmes as f
on af.cod_filme = f.codigo_filme
left join atores as a
on af.cod_ator = a.codigo_ator
where af.cod_filme = 1
union
select d.nome, d.nacionalidade
from diretores as d
join filmes as f
on f.cod_diretor = d.codigo_diretor
where f.codigo_filme = 1;


select a.nome, f.nome 
from atores_filmes as af
inner join filmes as f
on af.cod_filme = f.codigo_filme 
inner join atores as a
on af.cod_ator = a.codigo_ator;




select * from filmes;