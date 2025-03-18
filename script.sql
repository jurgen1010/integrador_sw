CREATE DATABASE db_hotel;

USE db_hotel;

CREATE TABLE `db_hotel`.`habitaciones` (
	`id` INT NOT NULL AUTO_INCREMENT,
    `numero` INT NOT NULL UNIQUE,
    `precioPorNoche` DOUBLE NOT NULL,
    `estado` VARCHAR(50) NOT NULL,
    `capacidad` INT NOT NULL,
    `tipo` VARCHAR(50) NOT NULL,
    `descripcion` TEXT,
    PRIMARY KEY(`id`)
);

CREATE TABLE `db_hotel`.`huespedes` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(50) NOT NULL,
    `apellido` VARCHAR(50) NOT NULL,
    `email` VARCHAR(100) NOT NULL,
    `telefono` VARCHAR(20) NOT NULL,
    `habitacion_id` INT,
    PRIMARY KEY(`id`),
    UNIQUE(`email`),
    FOREIGN KEY (`habitacion_id`) REFERENCES `db_personas`.`habitaciones`(`id`)
);


-- Insertar datos en la tabla habitaciones
INSERT INTO `db_hotel`.`habitaciones` (`numero`, `precioPorNoche`, `estado`, `capacidad`, `tipo`, `descripcion`) VALUES
(101, 100.0, 'Disponible', 2, 'Individual', 'Habitación individual con vista al mar'),
(102, 150.0, 'Ocupada', 3, 'Doble', 'Habitación doble con aire acondicionado'),
(103, 200.0, 'Mantenimiento', 4, 'Suite', 'Suite con todas las comodidades');

-- Insertar datos en la tabla huespedes
INSERT INTO `huespedes` (`nombre`, `apellido`, `email`, `telefono`, `habitacion_id`) VALUES
('Juan', 'Perez', 'juan.perez@example.com', '1234567890', 1),
('Maria', 'Gomez', 'maria.gomez@example.com', '0987654321', 2),
('Carlos', 'Lopez', 'carlos.lopez@example.com', '1122334455', 3);