package com.example.calificaciones.controller;

import com.example.calificaciones.model.Calificacion;
import com.example.calificaciones.repository.CalificacionRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/v1/calificaciones")
public class CalificacionController {

    @Autowired
    private CalificacionRepository calificacionRepository;

    @GetMapping
    public ResponseEntity<List<Calificacion>> obtenerTodasLasCalificaciones() {
        List<Calificacion> calificaciones = calificacionRepository.findAll();
        return new ResponseEntity<>(calificaciones, HttpStatus.OK);
    }

    @PostMapping
    public ResponseEntity<Calificacion> guardarCalificacion(@RequestBody Calificacion calificacion) {
        @SuppressWarnings("null")
        Calificacion nuevaCalificacion = calificacionRepository.save(calificacion);
        return new ResponseEntity<>(nuevaCalificacion, HttpStatus.CREATED);
    }

    @GetMapping("/{estudianteId}")
    public ResponseEntity<List<Calificacion>> obtenerCalificacionesPorEstudiante(@PathVariable String estudianteId) {
        List<Calificacion> calificaciones = calificacionRepository.findByEstudianteId(estudianteId);
        return new ResponseEntity<>(calificaciones, HttpStatus.OK);
    }
}
