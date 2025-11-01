package com.aparatamentos.api.controllers;

import com.aparatamentos.api.models.ClienteModel;
import com.aparatamentos.api.models.PropiedadModel;
import com.aparatamentos.api.models.ReservaModel;
import com.aparatamentos.api.services.ReservaService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/reservas")
public class ReservaController {

    @Autowired
    private ReservaService reservaService;

    @PostMapping
    public ReservaModel createReserva(@RequestBody ReservaModel reserva) {

        PropiedadModel propiedad = new PropiedadModel();
        propiedad.setId_propiedad(reserva.getPropiedad().getId_propiedad());
        reserva.setPropiedad(propiedad);

        ClienteModel cliente = new ClienteModel();
        cliente.setId(reserva.getCliente().getId());
        reserva.setCliente(cliente);

        return reservaService.saveReserva(reserva);
    }

    @GetMapping
    public List<ReservaModel> getAllReservas() {
        return reservaService.getAllReservas();
    }

    @GetMapping("/{id}")
    public ResponseEntity<ReservaModel> getReservaById(@PathVariable Long id) {
        return reservaService.getReservaById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteReserva(@PathVariable Long id) {
        if (reservaService.getReservaById(id).isPresent()) {
            reservaService.deleteReserva(id);
            return ResponseEntity.noContent().build();
        } else {
            return ResponseEntity.notFound().build();
        }
    }
}