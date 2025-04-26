    drop database Bibliot_DB;
    create database Bibliot_DB;
    use Bibliot_DB;
    
    create table usuarios (
    id int primary key auto_increment,
    nombres varchar(100) not null,
    apellidos varchar(100) not null,
    correo varchar(100) not null unique,
    contraseña varchar(400) not null
    );
    
    