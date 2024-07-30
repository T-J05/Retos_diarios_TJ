-- 17 Creación de tabla: Escribe una consulta SQL para crear una tabla Usuarios con columnas id y nombre.
CREATE TABLE Usuarios(
    id SERIAL PRIMARY KEY,
    nombre VARCHAR (50)UNIQUE
);