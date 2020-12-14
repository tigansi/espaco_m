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