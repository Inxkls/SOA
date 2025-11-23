#!/usr/bin/env python
import sys
import traceback

print("Python:", sys.version)
print("Path:", sys.path[:3])

try:
    print("\n1. Importando módulos...")
    import cgi
    print("   ✓ cgi")
    from spyne import Application, rpc, ServiceBase, Integer, Unicode, Date, Array, ComplexModel
    print("   ✓ spyne")
    from spyne.protocol.soap import Soap11
    print("   ✓ spyne.protocol.soap")
    from spyne.server.wsgi import WsgiApplication
    print("   ✓ spyne.server.wsgi")
    from wsgiref.simple_server import make_server
    print("   ✓ wsgiref")
    
    print("\n2. Importando módulos locales...")
    import database
    print("   ✓ database")
    
    print("\n3. Inicializando servidor...")
    import inscripciones_soap.server as server_module
    print("   ✓ Servidor cargado")
    
    print("\n4. Creando aplicación WSGI...")
    wsgi_app = WsgiApplication(server_module.application)
    print("   ✓ Aplicación WSGI lista")
    
    print("\n5. Creando servidor...")
    server = make_server('127.0.0.1', 8000, wsgi_app)
    print("   ✓ Servidor creado en 127.0.0.1:8000")
    
    print("\n6. Iniciando servidor...")
    print("   Escuchando en http://127.0.0.1:8000")
    print("   WSDL en http://127.0.0.1:8000/?wsdl")
    server.serve_forever()
    
except Exception as e:
    print(f"\n❌ ERROR: {type(e).__name__}: {e}")
    print("\nTraceback completo:")
    traceback.print_exc()
    sys.exit(1)
