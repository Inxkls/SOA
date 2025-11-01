package com.aparatamentos.api.services;

import com.aparatamentos.api.models.PagosModel;
import com.aparatamentos.api.repositories.IPagoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class PagoService {

    @Autowired
    private IPagoRepository pagoRepository;

    public List<PagosModel> getAllPagos() {
        return pagoRepository.findAll();
    }

    public Optional<PagosModel> getPagoById(Long id) {
        return pagoRepository.findById(id);
    }

    public PagosModel savePago(PagosModel pago) {
        return pagoRepository.save(pago);
    }
}