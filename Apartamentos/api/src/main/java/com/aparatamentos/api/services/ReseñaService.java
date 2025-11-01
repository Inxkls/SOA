package com.aparatamentos.api.services;

import com.aparatamentos.api.models.ReseñaModel;
import com.aparatamentos.api.repositories.IResenaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ReseñaService {

    @Autowired
    private IResenaRepository resenaRepository;

    public List<ReseñaModel> getAllResenas() {
        return resenaRepository.findAll();
    }

    public ReseñaModel saveResena(ReseñaModel resena) {
        return resenaRepository.save(resena);
    }
}