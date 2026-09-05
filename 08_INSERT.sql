INSERT INTO razas (description)
VALUES ("Criollo"), ("Angora");

INSERT INTO empleados (documentoE, nombreE, apellidoE, telefonoE)
VALUES ('123456', "Vannesa", "Pulido", '3001234567'), ('789456', 'Jorge', 'Peña', '412565');

INSERT INTO propietario (nombreP, apellidoP, documento, nTelefono, correo, direccion)
VALUES ("Kyungsoo", "Do", '123345', '3044567890', "dokyungsoo@hotmail.com", "Cr 567B #45-12");

INSERT INTO mascotas (nombreM, edad, peso, fechaIngreso, idPropietario, idRaza, idEmpleado)
VALUES ("Kiwi", 5, 4, '2026-09-05', 1, 1, 1);