# TCP Server and Client

Este proyecto implementa un servidor TCP y un cliente que permite enviar mensajes de texto. El servidor responde a cada mensaje recibido en mayúsculas y cierra la conexión cuando se recibe el mensaje especial `"DESCONEXION"`.

## Requisitos

- Python 3. Se recomienda tener la versión más reciente.
- Asegúrate de tener los archivos `server.py`, `client.py` y `client_tester.py` en el mismo directorio.

## Instrucciones

### 1. Ejecutar el Servidor

Para iniciar el servidor, abre una terminal, navega hasta el directorio del proyecto y ejecuta:

```bash
python3 server.py

Esto iniciará el servidor en localhost en el puerto 5000. El servidor estará a la espera de conexiones de clientes.
```

### 2. Ejecutar el Cliente
Para conectarse al servidor, abre una nueva terminal en el mismo directorio y ejecuta:
```bash
python3 client.py`
```
Una vez conectado, el cliente permitirá enviar mensajes al servidor. El cliente te pedirá que ingreses un mensaje para enviar.

Mensaje normal: Si envías un cualquier texto, el servidor responderá con el mensaje en mayúsculas.
Cierre de conexión: Si envías el mensaje "DESCONEXION", el cliente cerrará la conexión.

### 3. Ejecución de Pruebas
Las pruebas del cliente y servidor se ejecutan mediante el script client_tester.py. Este script simula la interacción con el servidor en dos pasos:

Enviar un mensaje de texto normal

El cliente envía el mensaje "hola servidor" al servidor.
Se espera que el servidor responda con el mensaje en mayúsculas ("HOLA SERVIDOR").
Enviar el mensaje "DESCONEXION"

El cliente envía el mensaje "DESCONEXION" al servidor para cerrar la conexión.
El cliente verifica que la conexión se haya cerrado correctamente.
El servidor también cierra la conexión y deja de recibir mensajes de ese cliente.
Para ejecutar estas pruebas, simplemente corre el siguiente comando:

```bash
python3 client_tester.py
Este script realiza automáticamente ambas pruebas y muestra el resultado en la consola, confirmando que el servidor responde correctamente y que la conexión se cierra adecuadamente al enviar el mensaje de desconexión.
```

### Notas
El servidor debe estar ejecutándose antes de iniciar el cliente o las pruebas.
Asegúrate de que el puerto 5000 esté libre antes de iniciar el servidor para evitar conflictos.
Para detener el servidor, presiona Ctrl + C en la terminal donde se esté ejecutando.

### Estructura del Proyecto
- server.py: Código del servidor TCP.
- client.py: Código del cliente que se conecta al servidor.
- client_tester.py: Pruebas automáticas para validar el funcionamiento del servidor y el cliente.
- README.md: Instrucciones y documentación del proyecto.
 
