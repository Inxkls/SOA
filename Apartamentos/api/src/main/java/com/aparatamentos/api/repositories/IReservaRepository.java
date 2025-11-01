package com.aparatamentos.api.repositories;

import com.aparatamentos.api.models.ReservaModel;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface IReservaRepository extends JpaRepository<ReservaModel, Long> {
}