package com.aparatamentos.api.controllers;

import com.aparatamentos.api.models.PropiedadImagenesModel;
import com.aparatamentos.api.models.PropiedadModel;
import com.aparatamentos.api.services.PropiedadImagenesService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/imagenes")
public class PropiedadImagenesController {

    @Autowired
    private PropiedadImagenesService imagenesService;

    @GetMapping
    public List<PropiedadImagenesModel> getAllImagenes() {
        return imagenesService.getAllImagenes();
    }

    @PostMapping
    public PropiedadImagenesModel createImagen(@RequestBody PropiedadImagenesModel imagen) {
        PropiedadModel propiedad = new PropiedadModel();
        propiedad.setId_propiedad(imagen.getPropiedad().getId_propiedad());
        imagen.setPropiedad(propiedad);
        
        return imagenesService.saveImagen(imagen);
    }
}