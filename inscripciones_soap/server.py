from spyne import Application, rpc, ServiceBase, Integer, Unicode, Date, Array, ComplexModel
from spyne.protocol.soap import Soap11
import logging
from datetime import date
import database
import traceback
import sys

# Configurar logging para stdout Y archivo
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('soap_server.log', encoding='utf-8')
    ],
    force=True
)
logger = logging.getLogger(__name__)

# Inicializar base de datos al inicio
logger.info("=== INICIALIZANDO BASE DE DATOS ===")
database.init_db()
logger.info("=== BASE DE DATOS INICIALIZADA ===")

class Inscripcion(ComplexModel):
    __namespace__ = 'spyne.examples.inscripciones.soap'
    id = Integer
    estudiante_id = Unicode
    curso_id = Unicode
    fecha_inscripcion = Date

class InscripcionesService(ServiceBase):
    @rpc(Unicode, Unicode, _returns=Unicode)
    def InscribirEstudiante(self, estudiante_id, curso_id):
        logger.info(f"=== INICIANDO InscribirEstudiante ===")
        logger.info(f"Parámetros: estudiante_id={estudiante_id}, curso_id={curso_id}")
        
        try:
            # Convertir a string si es necesario
            estudiante_id = str(estudiante_id) if estudiante_id else ""
            curso_id = str(curso_id) if curso_id else ""
            
            logger.info(f"Después conversión: {estudiante_id}, {curso_id}")
            
            if not estudiante_id or not curso_id:
                msg = "Error: Parámetros vacíos"
                logger.error(msg)
                return msg
            
            logger.info("Obteniendo conexión a BD...")
            conn = database.get_db_connection()
            
            if not conn or not conn.is_connected():
                msg = "Error: No se pudo conectar a BD"
                logger.error(msg)
                return msg
            
            logger.info("Conexión exitosa. Preparando insert...")
            
            cursor = None
            try:
                cursor = conn.cursor()
                query = "INSERT INTO inscripcion (estudiante_id, curso_id, fecha_inscripcion) VALUES (%s, %s, %s)"
                fecha_actual = date.today()
                logger.info(f"Ejecutando: {query} con ({estudiante_id}, {curso_id}, {fecha_actual})")
                
                cursor.execute(query, (estudiante_id, curso_id, fecha_actual))
                conn.commit()
                
                resultado = f"Estudiante {estudiante_id} inscrito en curso {curso_id}."
                logger.info(f"Éxito: {resultado}")
                return resultado
                
            except Exception as inner_e:
                logger.error(f"Error en insert: {type(inner_e).__name__}: {inner_e}")
                logger.error(traceback.format_exc())
                return f"Error BD: {str(inner_e)}"
            finally:
                if cursor:
                    try:
                        cursor.close()
                    except:
                        pass
                if conn:
                    try:
                        conn.close()
                    except:
                        pass
        except Exception as e:
            logger.error(f"Error general en InscribirEstudiante: {type(e).__name__}: {e}")
            logger.error(traceback.format_exc())
            return f"Error: {str(e)}"

    @rpc(Unicode, _returns=Array(Inscripcion))
    def ConsultarInscripciones(self, estudiante_id):
        logger.info(f"=== INICIANDO ConsultarInscripciones ===")
        logger.info(f"Parámetro: estudiante_id={estudiante_id}")
        
        try:
            conn = database.get_db_connection()
            
            if not conn or not conn.is_connected():
                logger.error("No se pudo conectar a BD")
                return []
            
            cursor = None
            inscripciones_list = []
            
            try:
                cursor = conn.cursor(dictionary=True)
                query = "SELECT id, estudiante_id, curso_id, fecha_inscripcion FROM inscripcion WHERE estudiante_id = %s"
                logger.info(f"Ejecutando: {query} con {estudiante_id}")
                
                cursor.execute(query, (estudiante_id,))
                rows = cursor.fetchall()
                logger.info(f"Filas encontradas: {len(rows)}")
                
                for row in rows:
                    inscripcion = Inscripcion(
                        id=row['id'],
                        estudiante_id=row['estudiante_id'],
                        curso_id=row['curso_id'],
                        fecha_inscripcion=row['fecha_inscripcion']
                    )
                    inscripciones_list.append(inscripcion)
                    logger.info(f"Agregado: {row}")
                
                logger.info(f"Retornando {len(inscripciones_list)} inscripciones")
                return inscripciones_list
                
            except Exception as e:
                logger.error(f"Error al consultar: {type(e).__name__}: {e}")
                logger.error(traceback.format_exc())
                return []
            finally:
                if cursor:
                    try:
                        cursor.close()
                    except:
                        pass
                if conn:
                    try:
                        conn.close()
                    except:
                        pass
        except Exception as e:
            logger.error(f"Error general en ConsultarInscripciones: {type(e).__name__}: {e}")
            logger.error(traceback.format_exc())
            return []

application = Application([InscripcionesService], 'spyne.examples.inscripciones.soap',
                          in_protocol=Soap11(validator=None),
                          out_protocol=Soap11())

# Wrapper WSGI para capturar errores
def error_handling_wsgi_app(environ, start_response):
    logger.info(f"Solicitud recibida: {environ['REQUEST_METHOD']} {environ['PATH_INFO']}")
    try:
        from spyne.server.wsgi import WsgiApplication
        wsgi_app = WsgiApplication(application)
        return wsgi_app(environ, start_response)
    except Exception as e:
        logger.error(f"Error WSGI: {type(e).__name__}: {e}")
        logger.error(traceback.format_exc())
        start_response('500 Internal Server Error', [('Content-Type', 'text/plain')])
        return [b'Internal Server Error']

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    
    print("Iniciando servidor SOAP en http://127.0.0.1:8000", flush=True)
    print("WSDL disponible en http://127.0.0.1:8000/?wsdl", flush=True)
    sys.stdout.flush()
    
    try:
        server = make_server('127.0.0.1', 8000, error_handling_wsgi_app)
        print("Servidor listo. Esperando solicitudes...", flush=True)
        sys.stdout.flush()
        server.serve_forever()
    except Exception as e:
        logger.error(f"Error iniciando servidor: {e}")
        logger.error(traceback.format_exc())
