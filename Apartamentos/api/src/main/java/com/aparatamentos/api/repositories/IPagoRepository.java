package com.aparatamentos.api.repositories;

import com.aparatamentos.api.models.PagosModel;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface IPagoRepository extends JpaRepository<PagosModel, Long> {

}