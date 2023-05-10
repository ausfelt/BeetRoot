import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)

# Caesar cipher implementation
def caesar_cipher(message, key):
    result = ""
    for char in message:
        if char.isalpha():
            shifted = (ord(char) + key - 65) % 26 + 65
            result += chr(shifted)
        else:
            result += char
    return result

# Create a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    # Bind the socket to a specific IP address and port
    sock.bind((HOST, PORT))

    # Listen for incoming messages
    while True:
        # Receive a message from a client
        data, addr = sock.recvfrom(1024)
        message, key = data.decode().split("|")
        print(f"Received message: {message} from {addr}")

        # Encrypt the message using the Caesar cipher algorithm
        encrypted_message = caesar_cipher(message, int(key))

        # Send the encrypted message back to the client
        response = encrypted_message.encode()
        sock.sendto(response, addr)