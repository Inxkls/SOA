package com.aparatamentos.api.controllers;

import com.aparatamentos.api.models.ClienteModel;
import com.aparatamentos.api.models.PropiedadModel;
import com.aparatamentos.api.models.ReseñaModel;
import com.aparatamentos.api.services.ReseñaService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/resenas")
public class ReseñaController {

    @Autowired
    private ReseñaService resenaService;

    @GetMapping
    public List<ReseñaModel> getAllResenas() {
        return resenaService.getAllResenas();
    }

    @PostMapping
    public ReseñaModel createResena(@RequestBody ReseñaModel resena) {
        PropiedadModel propiedad = new PropiedadModel();
        propiedad.setId_propiedad(resena.getPropiedad().getId_propiedad());
        resena.setPropiedad(propiedad);

        ClienteModel cliente = new ClienteModel();
        cliente.setId(resena.getCliente().getId());
        resena.setCliente(cliente);
        
        return resenaService.saveResena(resena);
    }
}