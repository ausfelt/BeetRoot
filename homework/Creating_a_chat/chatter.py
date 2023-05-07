import socket
import threading

HOST = 'localhost'
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

name = input("Enter your name: ")
client_socket.send(name.encode())

def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            client_socket.close()
            break

def write():
    while True:
        message = f"{name}: {input('')}"
        client_socket.send(message.encode())

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()