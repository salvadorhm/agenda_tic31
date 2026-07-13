-- Activar el soporte para claves foráneas en SQLite
PRAGMA foreign_keys = ON;
.mode box
.head on

CREATE TABLE contactos(
    id_contacto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    primer_apellido TEXT NOT NULL,
    segundo_apellido TEXT NOT NULL,
    email TEXT NOT NULL,
    telefono TEXT NOT NULL
);

CREATE TABLE direcciones(
    id_direccion INTEGER PRIMARY KEY AUTOINCREMENT,
    id_contacto INTEGER NOT NULL,
    pais TEXT NOT NULL,
    estado TEXT NOT NULL,
    ciudad TEXT NOT NULL,
    colonia TEXT NOT NULL,
    calle TEXT NOT NULL,
    numero_exterior TEXT NOT NULL,
    -- Definición de la relación (Clave Foránea)
    FOREIGN KEY (id_contacto) REFERENCES contactos(id_contacto)
);

-- Insertar contactos
INSERT INTO contactos(nombre, primer_apellido, segundo_apellido, email, telefono)
VALUES
('Dejah', 'Thoris', 'Barsonn', 'dejah@email.com', '111111111'),
('John', 'Carter', 'Earth', 'john@email.com', '22222222');

-- Insertar 2 direcciones para Dejah (id_contacto = 1)
-- Insertar 2 direcciones para John (id_contacto = 2)
INSERT INTO direcciones(id_contacto, pais, estado, ciudad, colonia, calle, numero_exterior)
VALUES
(1, 'Marte', 'Helium', 'Helium City', 'Royal Sector', 'Palace Avenue', '1'),
(1, 'Marte', 'Zodanga', 'Zodanga', 'Outskirts', 'Red Dust Road', '45'),
(2, 'Tierra', 'Virginia', 'Richmond', 'Downtown', 'Main Street', '100'),
(2, 'Marte', 'Helium', 'Helium City', 'Warrior Sector', 'Warlord Way', '7');

-- Ver todos los contactos
SELECT * FROM contactos;

-- Ver todas las direcciones
SELECT * FROM direcciones;

-- Consulta con JOIN para ver la relación entre contactos y direcciones
SELECT
    c.nombre,
    c.primer_apellido,
    d.pais,
    d.ciudad,
    d.calle,
    d.numero_exterior
FROM contactos c
JOIN direcciones d ON c.id_contacto = d.id_contacto;


