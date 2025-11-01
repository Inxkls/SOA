package com.aparatamentos.api.services;

import com.aparatamentos.api.models.ReservaModel;
import com.aparatamentos.api.repositories.IReservaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class ReservaService {

    @Autowired
    private IReservaRepository reservaRepository;

    public List<ReservaModel> getAllReservas() {
        return reservaRepository.findAll();
    }

    public Optional<ReservaModel> getReservaById(Long id) {
        return reservaRepository.findById(id);
    }

    public ReservaModel saveReserva(ReservaModel reserva) {
        return reservaRepository.save(reserva);
    }

    public void deleteReserva(Long id) {
        reservaRepository.deleteById(id);
    }
}