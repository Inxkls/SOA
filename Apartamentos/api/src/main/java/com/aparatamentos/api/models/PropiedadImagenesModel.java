package com.aparatamentos.api.models;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "propiedad_imagenes")
public class PropiedadImagenesModel {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id_imagen;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "id_propiedad", nullable = false)
    private PropiedadModel propiedad;

    @Column(name = "url_imagen", nullable = false, length = 500)
    private String urlImagen;

    @Column(length = 200)
    private String descripcion;

    @Column(name = "fecha_carga", nullable = false, updatable = false)
    private LocalDateTime fecha_carga;

    @PrePersist
    protected void onCreate() {
        fecha_carga = LocalDateTime.now();
    }
    
    // --- Getters y Setters ---
    // (Añade todos los Getters y Setters aquí si no usas Lombok)
    
    public Long getId_imagen() { return id_imagen; }
    public void setId_imagen(Long id_imagen) { this.id_imagen = id_imagen; }
    public PropiedadModel getPropiedad() { return propiedad; }
    public void setPropiedad(PropiedadModel propiedad) { this.propiedad = propiedad; }
    public String getUrlImagen() { return urlImagen; }
    public void setUrlImagen(String urlImagen) { this.urlImagen = urlImagen; }
    public String getDescripcion() { return descripcion; }
    public void setDescripcion(String descripcion) { this.descripcion = descripcion; }
    public LocalDateTime getFecha_carga() { return fecha_carga; }
    public void setFecha_carga(LocalDateTime fecha_carga) { this.fecha_carga = fecha_carga; }
}