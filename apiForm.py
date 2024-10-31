import requests

datos = {
 "name": "Mariano",
 "email": "mariano@ejemplo.com",
 "message": "¡Hola, mundo!"
}
r = requests.post("http://localhost:8880/form", data=datos)

contenido = r.text
if contenido.find("Mensaje enviado") > -1:
 print("¡Formulario enviado!")
else:
 print("Ocurrió un error.")