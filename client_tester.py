import socket

HOST = 'localhost'
PORT = 5000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print(f"Conectado al servidor en {HOST}:{PORT}")

        try:
            # MENSAJE NORMAL
            message = "hola servidor"
            client_socket.sendall(message.encode())
            print(f"Enviado: {message}")

            response = client_socket.recv(1024).decode()
            print(f"Respuesta del servidor: {response}")

            # MENSAJE DE DESCONEXION
            disconnect_message = "DESCONEXION"
            client_socket.sendall(disconnect_message.encode())
            print(f"Enviado: {disconnect_message}")

            response = client_socket.recv(1024).decode()
            if response == "":
                print("Te has desconectado del servidor correctamente.")
            else:
                print("Error: la conexión no se cerró correctamente.")

        except Exception as e:
            print(f"Ocurrió un error durante el flujo de prueba: {e}")

if __name__ == "__main__":
    main()
