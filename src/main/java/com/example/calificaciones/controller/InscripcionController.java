package com.example.calificaciones.controller;

import com.example.calificaciones.model.Inscripcion;
import com.example.calificaciones.repository.InscripcionRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/v1/inscripciones")
public class InscripcionController {

    @Autowired
    private InscripcionRepository inscripcionRepository;

    @PostMapping
    public ResponseEntity<Inscripcion> guardarInscripcion(@RequestBody Inscripcion inscripcion) {
        @SuppressWarnings("null")
        Inscripcion nuevaInscripcion = inscripcionRepository.save(inscripcion);
        return new ResponseEntity<>(nuevaInscripcion, HttpStatus.CREATED);
    }

    @GetMapping("/{estudianteId}")
    public ResponseEntity<List<Inscripcion>> obtenerInscripcionesPorEstudiante(@PathVariable String estudianteId) {
        List<Inscripcion> inscripciones = inscripcionRepository.findByEstudianteId(estudianteId);
        return new ResponseEntity<>(inscripciones, HttpStatus.OK);
    }

    @GetMapping
    public ResponseEntity<List<Inscripcion>> obtenerTodasLasInscripciones() {
        List<Inscripcion> inscripciones = inscripcionRepository.findAll();
        return new ResponseEntity<>(inscripciones, HttpStatus.OK);
    }
}
