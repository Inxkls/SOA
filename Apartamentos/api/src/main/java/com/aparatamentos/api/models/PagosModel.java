package com.aparatamentos.api.models;

import java.time.LocalDate;
import java.time.LocalDateTime;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.OneToOne;

@Entity
@Table(name = "pagos")
public class PagosModel {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY) 
    private Long id_pago;

    @OneToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "id_reserva", nullable = false)
    private ReservaModel reserva;

    @Column(name = "monto", nullable = false)
    private Double monto;

    @Enumerated(EnumType.STRING)
    @Column(name = "metodo_pago", nullable = false)
    private MetodoPago metodo_pago;

    @Enumerated(EnumType.STRING)
    @Column(name = "estado_pago", nullable = false)
    private EstadoPago estado_pago;

    @Column(name = "fecha_pago", nullable = false)
    private LocalDate fecha_pago;

    @Column(name = "referecia_pago", nullable = false, length = 100)
    private String refereciaPago;

    @Column(name = "detalles_pago", length = 500)
    private String detalles_pago;

    @Column(name = "created_at", nullable = false)
    private LocalDateTime created_at;

    enum MetodoPago {
        TARJETA_CREDITO,
        TARJETA_DEBITO,
        EFECTIVO
    }

    enum EstadoPago {
        PENDIENTE,
        COMPLETADO,
        FALLIDO,
        REEMBOLSADO
    }
    public ReservaModel getReserva() { return reserva; }
    public void setReserva(ReservaModel reserva) { this.reserva = reserva; }
    
}

