#!/usr/bin/env python
"""Servidor SOAP simple sin Spyne para evitar problemas de compatibilidad."""
import http.server
import socketserver
from http import HTTPStatus
from datetime import date
import database
import xml.etree.ElementTree as ET

# Puerto
PORT = 8000
HOST = '127.0.0.1'

# Inicializar BD
print("Inicializando base de datos...")
database.init_db()
print("Base de datos lista.")

class SOAPHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        """Manejo de solicitudes POST para SOAP."""
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8')
        
        print(f"\n[SOLICITUD] Método: {self.command}")
        print(f"[BODY] {body[:200]}...")
        
        try:
            # Parsear XML
            root = ET.fromstring(body)
            
            # Namespaces
            namespaces = {
                'soap': 'http://schemas.xmlsoap.org/soap/envelope/',
                'ns0': 'spyne.examples.inscripciones.soap'
            }
            
            # Buscar Body
            body_elem = root.find('.//soap:Body', namespaces)
            if body_elem is None:
                body_elem = root.find('.//Body')
            
            print(f"[DEBUG] Body encontrado: {body_elem is not None}")
            
            # Buscar método
            inscribir_elem = body_elem.find('.//ns0:InscribirEstudiante', namespaces)
            consultar_elem = body_elem.find('.//ns0:ConsultarInscripciones', namespaces)
            
            if inscribir_elem is not None:
                print("[METODO] InscribirEstudiante")
                self.manejar_inscribir(inscribir_elem, namespaces)
            elif consultar_elem is not None:
                print("[METODO] ConsultarInscripciones")
                self.manejar_consultar(consultar_elem, namespaces)
            else:
                self.enviar_error("Método no reconocido")
                
        except Exception as e:
            print(f"[ERROR] {type(e).__name__}: {e}")
            import traceback
            traceback.print_exc()
            self.enviar_error(str(e))
    
    def manejar_inscribir(self, elem, ns):
        """Manejar InscribirEstudiante."""
        try:
            estudiante_id_elem = elem.find('ns0:estudiante_id', ns)
            curso_id_elem = elem.find('ns0:curso_id', ns)
            
            if estudiante_id_elem is None:
                estudiante_id_elem = elem.find('.//estudiante_id')
            if curso_id_elem is None:
                curso_id_elem = elem.find('.//curso_id')
            
            estudiante_id = estudiante_id_elem.text if estudiante_id_elem is not None else ""
            curso_id = curso_id_elem.text if curso_id_elem is not None else ""
            
            print(f"  estudiante_id: {estudiante_id}")
            print(f"  curso_id: {curso_id}")
            
            # Insertar en BD
            conn = database.get_db_connection()
            if conn and conn.is_connected():
                cursor = conn.cursor()
                query = "INSERT INTO inscripcion (estudiante_id, curso_id, fecha_inscripcion) VALUES (%s, %s, %s)"
                cursor.execute(query, (estudiante_id, curso_id, date.today()))
                conn.commit()
                cursor.close()
                conn.close()
                
                respuesta = f"Estudiante {estudiante_id} inscrito en curso {curso_id}."
                print(f"  Respuesta: {respuesta}")
                self.enviar_soap_respuesta(respuesta)
            else:
                self.enviar_error("No se pudo conectar a BD")
        except Exception as e:
            print(f"  ERROR: {e}")
            self.enviar_error(str(e))
    
    def manejar_consultar(self, elem, ns):
        """Manejar ConsultarInscripciones."""
        try:
            estudiante_id_elem = elem.find('ns0:estudiante_id', ns)
            if estudiante_id_elem is None:
                estudiante_id_elem = elem.find('.//estudiante_id')
            
            estudiante_id = estudiante_id_elem.text if estudiante_id_elem is not None else ""
            print(f"  estudiante_id: {estudiante_id}")
            
            conn = database.get_db_connection()
            if conn and conn.is_connected():
                cursor = conn.cursor(dictionary=True)
                query = "SELECT id, estudiante_id, curso_id, fecha_inscripcion FROM inscripcion WHERE estudiante_id = %s"
                cursor.execute(query, (estudiante_id,))
                rows = cursor.fetchall()
                cursor.close()
                conn.close()
                
                print(f"  Resultados: {len(rows)} registros")
                
                # Construir XML de respuesta
                respuesta_xml = self.construir_respuesta_consulta(rows)
                self.enviar_soap_xml(respuesta_xml)
            else:
                self.enviar_error("No se pudo conectar a BD")
        except Exception as e:
            print(f"  ERROR: {e}")
            self.enviar_error(str(e))
    
    def construir_respuesta_consulta(self, rows):
        """Construir XML SOAP con resultados de consulta."""
        xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml += '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns0="spyne.examples.inscripciones.soap">\n'
        xml += '  <soap:Body>\n'
        xml += '    <ns0:ConsultarInscripcionesResponse>\n'
        xml += '      <ns0:ConsultarInscripcionesResult>\n'
        
        for row in rows:
            xml += '        <ns0:Inscripcion>\n'
            xml += f'          <ns0:id>{row["id"]}</ns0:id>\n'
            xml += f'          <ns0:estudiante_id>{row["estudiante_id"]}</ns0:estudiante_id>\n'
            xml += f'          <ns0:curso_id>{row["curso_id"]}</ns0:curso_id>\n'
            xml += f'          <ns0:fecha_inscripcion>{row["fecha_inscripcion"]}</ns0:fecha_inscripcion>\n'
            xml += '        </ns0:Inscripcion>\n'
        
        xml += '      </ns0:ConsultarInscripcionesResult>\n'
        xml += '    </ns0:ConsultarInscripcionesResponse>\n'
        xml += '  </soap:Body>\n'
        xml += '</soap:Envelope>'
        return xml
    
    def enviar_soap_respuesta(self, mensaje):
        """Enviar respuesta SOAP con un string."""
        xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml += '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns0="spyne.examples.inscripciones.soap">\n'
        xml += '  <soap:Body>\n'
        xml += '    <ns0:InscribirEstudianteResponse>\n'
        xml += f'      <ns0:InscribirEstudianteResult>{mensaje}</ns0:InscribirEstudianteResult>\n'
        xml += '    </ns0:InscribirEstudianteResponse>\n'
        xml += '  </soap:Body>\n'
        xml += '</soap:Envelope>'
        
        self.enviar_soap_xml(xml)
    
    def enviar_soap_xml(self, xml_str):
        """Enviar respuesta XML SOAP."""
        xml_bytes = xml_str.encode('utf-8')
        
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-Type', 'text/xml; charset=utf-8')
        self.send_header('Content-Length', len(xml_bytes))
        self.end_headers()
        self.wfile.write(xml_bytes)
        
        print(f"[RESPUESTA] {len(xml_bytes)} bytes enviados")
    
    def enviar_error(self, error_msg):
        """Enviar error SOAP."""
        xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml += '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">\n'
        xml += '  <soap:Body>\n'
        xml += '    <soap:Fault>\n'
        xml += f'      <faultstring>{error_msg}</faultstring>\n'
        xml += '    </soap:Fault>\n'
        xml += '  </soap:Body>\n'
        xml += '</soap:Envelope>'
        
        xml_bytes = xml.encode('utf-8')
        
        self.send_response(HTTPStatus.INTERNAL_SERVER_ERROR)
        self.send_header('Content-Type', 'text/xml; charset=utf-8')
        self.send_header('Content-Length', len(xml_bytes))
        self.end_headers()
        self.wfile.write(xml_bytes)
        
        print(f"[ERROR ENVIADO] {error_msg}")
    
    def log_message(self, format, *args):
        """Suprimir logs automáticos."""
        pass

if __name__ == '__main__':
    handler = SOAPHandler
    
    with socketserver.TCPServer((HOST, PORT), handler) as httpd:
        print(f"\n✓ Servidor SOAP iniciado en http://{HOST}:{PORT}")
        print("Esperando solicitudes...")
        print("(Presiona Ctrl+C para detener)\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n✓ Servidor detenido.")
