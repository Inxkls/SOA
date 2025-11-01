package com.aparatamentos.api.services; 
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.aparatamentos.api.models.PropiedadModel;
import com.aparatamentos.api.models.ClienteModel;
import com.aparatamentos.api.models.PropiedadModel.TipoPropiedad;
import com.aparatamentos.api.repositories.IPropiedadRepository; 

@Service
public class PropiedadService {

    @Autowired
    private IPropiedadRepository propiedadRepository;

    public List<PropiedadModel> getAllPropiedades() {
        return propiedadRepository.findAll();
    }

    public Optional<PropiedadModel> getPropiedadById(Long id) {
        return propiedadRepository.findById(id);
    }

    public PropiedadModel savePropiedad(PropiedadModel propiedad) {
        return propiedadRepository.save(propiedad);
    } 
    
    public void deletePropiedad(Long id) {
        propiedadRepository.deleteById(id);
    }

    public List<PropiedadModel> getPropiedadesPorTipo(TipoPropiedad tipo) {
    
        return propiedadRepository.findByTipo(tipo);
    }
    
    public List<PropiedadModel> getPropiedadesPorPropietario(Long idPropietario) {
        ClienteModel propietario = new ClienteModel();
        propietario.setId(idPropietario);
        return IPropiedadRepository.findByPropietario(propietario);
    }
}