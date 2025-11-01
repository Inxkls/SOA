package com.aparatamentos.api.services;

import com.aparatamentos.api.models.PropiedadImagenesModel;
import com.aparatamentos.api.repositories.IPropiedadImagenesRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PropiedadImagenesService {

    @Autowired
    private IPropiedadImagenesRepository imagenesRepository;

    public List<PropiedadImagenesModel> getAllImagenes() {
        return imagenesRepository.findAll();
    }

    public PropiedadImagenesModel saveImagen(PropiedadImagenesModel imagen) {
        return imagenesRepository.save(imagen);
    }
}