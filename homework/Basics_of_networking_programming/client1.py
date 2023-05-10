import socket

SERVER_HOST = '127.0.0.1'  # The server's hostname or IP address
SERVER_PORT = 5000        # The port used by the server

# Create a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    # Send a message to the server
    message = "Hello, server!".encode()
    sock.sendto(message, (SERVER_HOST, SERVER_PORT))

    # Receive a response from the server
    data, addr = sock.recvfrom(1024)
    print(f"Received message: {data.decode()} from {addr}")