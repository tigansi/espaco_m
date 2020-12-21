create table usuarios
(
	id_usuario  serial primary key,
	nm_usuario  varchar(100) not null,
 	email       varchar(100) not null unique,
	celular     varchar(30)  not null,
	aniversario date 	     not null,
	senha       text 	     not null,
	foto        text         default './Fotos/avatar.png',
	tipo	    varchar(10)  default 'CLI',
	is_ativo    boolean default 'true'
);

create table servicos
(
	id_servico serial,
	nm_servico varchar(100) not null,
	categoria  varchar(100) not null,
	duracao    varchar(10)  not null,
	valor      varchar(30)  not null,
	is_ativo   boolean default true
);

create table categorias
(
	id_categoria serial,
	nm_categoria varchar(100) not null,
	is_ativo     boolean default true
);


create table horarios
(
	id_horario 		serial unique,
	id_servico 		int,
	id_usuario      int,
	data            timestamp default current_timestamp,
	is_ativo 		boolean   default true
);
