import requests

url = 'http://127.0.0.1:8000/'
headers = {'Content-Type': 'text/xml'}

xml_body = '''<?xml version="1.0" encoding="UTF-8"?>
<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns0="spyne.examples.inscripciones.soap">
  <soap-env:Body>
    <ns0:InscribirEstudiante>
      <ns0:estudiante_id>EST001</ns0:estudiante_id>
      <ns0:curso_id>CURSO001</ns0:curso_id>
    </ns0:InscribirEstudiante>
  </soap-env:Body>
</soap-env:Envelope>'''

print("Enviando solicitud SOAP...")
try:
    response = requests.post(url, data=xml_body, headers=headers)
    print(f'Status Code: {response.status_code}')
    print(f'Response Headers: {response.headers}')
    print(f'Response Body:\n{response.text}')
except Exception as e:
    print(f'Error: {type(e).__name__}: {e}')
    import traceback
    traceback.print_exc()
