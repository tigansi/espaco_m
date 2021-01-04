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

create table agenda
(
	id_agenda	 serial unique,
	id_horario 	 int unique,
	id_cliente   int not null,
	is_concluido boolean default false,
	is_andamento boolean default false,
	is_ativo     boolean default true,

	foreign key(id_horario) 
		references horarios (id_horario)
);

create table avaliacao
(
	id_avaliacao 	 		serial unique,
	id_agenda    	 		int,
	id_colaborador  	 	int not null,
	id_cliente   	 		int not null,
	vl_avaliacao_col 		int default 0,
	vl_avaliacao_cli 		int default 0,
	is_avaliado_cliente 	boolean default 'false',
	is_avaliado_colaborador boolean default 'false'
);

create table comentarios
(
	id_comentario serial primary key,
	id_avaliacao  int not null,
	comentario    text,
	foreign key(id_avaliacao) 
		references avaliacao (id_avaliacao)
);


/*
--select * from avaliacao;
--6
SELECT AVG(vl_avaliacao_col)::numeric(10,2) FROM avaliacao WHERE vl_avaliacao_col > 0;
*/