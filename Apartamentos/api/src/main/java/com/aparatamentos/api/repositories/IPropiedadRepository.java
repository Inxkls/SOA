package com.aparatamentos.api.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.aparatamentos.api.models.PropiedadModel;
import com.aparatamentos.api.models.PropiedadModel.TipoPropiedad;
import com.aparatamentos.api.models.ClienteModel;
import java.util.List; 

@Repository
public interface IPropiedadRepository extends JpaRepository<PropiedadModel, Long> {
    
    List<PropiedadModel> findByTipo(TipoPropiedad tipo);
    static List<PropiedadModel> findByPropietario(ClienteModel propietario) {

        throw new UnsupportedOperationException("Unimplemented method 'findByPropietario'");
    }
    
}