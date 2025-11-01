package com.aparatamentos.api.controllers;

import com.aparatamentos.api.models.PagosModel;
import com.aparatamentos.api.models.ReservaModel;
import com.aparatamentos.api.services.PagoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/pagos")
public class PagoController {

    @Autowired
    private PagoService pagoService;

    @GetMapping
    public List<PagosModel> getAllPagos() {
        return pagoService.getAllPagos();
    }

    @PostMapping
    public PagosModel createPago(@RequestBody PagosModel pago) {
        ReservaModel reserva = new ReservaModel();
        reserva.setId_reserva(pago.getReserva().getId_reserva());
        pago.setReserva(reserva);
        
        return pagoService.savePago(pago);
    }

    @GetMapping("/{id}")
    public ResponseEntity<PagosModel> getPagoById(@PathVariable Long id) {
        return pagoService.getPagoById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }
}