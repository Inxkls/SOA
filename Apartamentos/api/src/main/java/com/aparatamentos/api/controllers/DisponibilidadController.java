package com.aparatamentos.api.controllers;

import com.aparatamentos.api.models.DisponibilidadModel;
import com.aparatamentos.api.models.PropiedadModel;
import com.aparatamentos.api.services.DisponibilidadService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/disponibilidad")
public class DisponibilidadController {

    @Autowired
    private DisponibilidadService disponibilidadService;

    @GetMapping
    public List<DisponibilidadModel> getAllDisponibilidades() {
        return disponibilidadService.getAllDisponibilidades();
    }

    @PostMapping
    public DisponibilidadModel createDisponibilidad(@RequestBody DisponibilidadModel disponibilidad) {

        PropiedadModel propiedad = new PropiedadModel();
        propiedad.setId_propiedad(disponibilidad.getPropiedad().getId_propiedad());
        disponibilidad.setPropiedad(propiedad);

        return disponibilidadService.saveDisponibilidad(disponibilidad);
    }
}