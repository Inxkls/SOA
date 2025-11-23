CREATE DATABASE IF NOT EXISTS db_calificaciones;
USE db_calificaciones;

CREATE TABLE IF NOT EXISTS calificacion (
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    curso_id VARCHAR(255),
    estudiante_id VARCHAR(255),
    fecha_calificacion DATE,
    nota DOUBLE
);

CREATE TABLE IF NOT EXISTS inscripcion (
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    curso_id VARCHAR(255),
    estudiante_id VARCHAR(255),
    fecha_inscripcion DATE
);
