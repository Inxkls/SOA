package com.aparatamentos.api.repositories;

import com.aparatamentos.api.models.ReseñaModel;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface IResenaRepository extends JpaRepository<ReseñaModel, Long> {

}