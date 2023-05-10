import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)

# Create a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    # Bind the socket to a specific IP address and port
    sock.bind((HOST, PORT))

    # Listen for incoming messages
    while True:
        # Receive a message from a client
        data, addr = sock.recvfrom(1024)
        print(f"Received message: {data.decode()} from {addr}")

        # Send a response back to the client
        response = f"ACK: {data.decode()}".encode()
        sock.sendto(response, addr)