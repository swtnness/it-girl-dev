-- Comando o clausula para crear base de datos
CREATE DATABASE ejemplos;
-- comando para usar la o las bases de datos
use ejemplos;
-- comando para crear tablas

CREATE TABLE propietario (
    idPropietario INT PRIMARY KEY AUTO_INCREMENT,
    nombreP VARCHAR(50),
    apellidoP VARCHAR(50),
    documento VARCHAR(50) UNIQUE,
    nTelefono VARCHAR(15),
    correo VARCHAR(100),
    direccion VARCHAR(100),
    idMascota INT
);

CREATE TABLE razas (
    idRaza INT PRIMARY KEY AUTO_INCREMENT,
    description VARCHAR(15)
);

CREATE TABLE empleados (
    idEmpleado INT PRIMARY KEY AUTO_INCREMENT,
    documentoE VARCHAR(15) UNIQUE,
    nombreE VARCHAR(50),
    apellidoE VARCHAR(50),
    telefonoE VARCHAR(50),
    idMascota INT
);

CREATE TABLE mascotas (
    idMascota INT PRIMARY KEY AUTO_INCREMENT,
    nombreM VARCHAR(50),
    edad VARCHAR(3),
    peso INT,
    fechaIngreso DATE,
    idPropietario INT,
    idRaza INT,
    idEmpleado INT,

    FOREIGN KEY (idPropietario) REFERENCES propietario(idPropietario),
    FOREIGN KEY (idRaza) REFERENCES razas(idRaza),
    FOREIGN KEY (idEmpleado) REFERENCES empleados(idEmpleado)
);
