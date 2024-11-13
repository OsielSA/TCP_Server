import socket

HOST = 'localhost'
PORT = 5000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print(f"Conectado al servidor en {HOST}:{PORT}")

        while True:
            try:
                # Mensaje del usuario
                message = input("Ingrese un mensaje ('DESCONEXION' para salir): ")

                client_socket.sendall(message.encode())
                response = client_socket.recv(1024).decode()
                
                if not response:
                    print("Te has desconectado del servidor.")
                    break
                print(f"Respuesta del servidor: {response}")

            except Exception as e:
                print("Te has desconectado del servidor debido a un error.")
                break

if __name__ == '__main__':
    main()
