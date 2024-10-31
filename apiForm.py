import requests

datos = {
 "name": "Mariano",
 "email": "mariano@ejemplo.com",
 "message": "¡Hola, mundo!"
}
r = requests.post("http://localhost:8880/form", data=datos)

