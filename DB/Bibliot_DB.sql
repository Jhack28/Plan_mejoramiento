drop database bibliot_db;
create database Bibliot_DB;
use Bibliot_DB;

create table Usuarios (
	ID int primary key auto_increment,
    nombres varchar(100) not null,
    apellidos varchar(100) not null,
    correo varchar(100) not null,
    contraseña varchar(100) not null
    );
    
