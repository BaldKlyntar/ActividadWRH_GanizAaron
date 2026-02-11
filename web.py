from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        if self.path == "/":
            filename = "home.html"
        else:
            filename = "notFound.html"
        # Se abre el archivo utilizando open
        #el archivo es leido en su formato binario (rb)
        with open(filename, "rb") as file:
            content = file.read()
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(content)
        #self.wfile.write(self.get_response().encode("utf-8"))

    #En la funcion get_response, accedo al diccionario creado por parse_qsl a partir
    # de la ruta url y accedo a la key autor para extraer el nombre
    def get_response(self):
        return f"""
    <h1>Proyecto: web-uno Autor: {self.query_data().get("autor")}</h1>
    <h1> Hola Web </h1>
    <p> URL Parse Result : {self.url()}         </p>
    <p> Path Original: {self.path}         </p>
    <p> Headers: {self.headers}      </p>
    <p> Query: {self.query_data()}   </p>
"""


if __name__ == "__main__":
    print("Starting server")
    # Almaceno en la variable PORT el puerto al que quiero acceder
    PORT = 8000 # Asigno el puerto 8000
    print(f"""Corriendo en el puerto: {PORT}""") #Se muestra la informacion del puerto
    server = HTTPServer(("localhost", PORT), WebRequestHandler)
    server.serve_forever()
