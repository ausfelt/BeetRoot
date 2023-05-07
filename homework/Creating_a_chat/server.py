import socket
import threading

HOST = 'localhost'
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

clients = []

def handle_client(client_socket, client_address):
    name = client_socket.recv(1024).decode()
    welcome_message = f"Welcome {name} to the chat room!"
    broadcast(welcome_message)
    clients.append(client_socket)

    while True:
        try:
            message = client_socket.recv(1024).decode()
            broadcast(message)
        except:
            index = clients.index(client_socket)
            clients.remove(client_socket)
            client_socket.close()
            broadcast(f"{name} has left the chat room!")
            break

def broadcast(message):
    for client in clients:
        client.send(message.encode())

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connected with {client_address}")
    client_socket.send("NAME".encode())
    name = client_socket.recv(1024).decode()
    clients.append(client_socket)
    print(f"Name of the client is {name}")
    threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

server_socket.close()
