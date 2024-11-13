import socket

HOST = 'localhost'
PORT = 5000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Servidor iniciado en [{HOST}:{PORT}]")

        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Conexión establecida con {client_address}")
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    message = data.decode()
                    print(f"Recibido de {client_address}: {message}")
                    
                    if message == "DESCONEXION":
                        client_socket.close()
                        break
                    
                    response = message.upper()
                    client_socket.sendall(response.encode())
                print(f"Conexión cerrada con {client_address}")

if __name__ == '__main__':
    main()
