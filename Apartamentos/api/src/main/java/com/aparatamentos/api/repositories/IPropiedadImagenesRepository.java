package com.aparatamentos.api.repositories;

import com.aparatamentos.api.models.PropiedadImagenesModel;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface IPropiedadImagenesRepository extends JpaRepository<PropiedadImagenesModel, Long> {

}