import socket

SERVER_HOST = '127.0.0.1'  # The server's hostname or IP address
SERVER_PORT = 5000        # The port used by the server

# Caesar cipher implementation
def caesar_cipher(message, key):
    result = ""
    for char in message:
        if char.isalpha():
            shifted = (ord(char) - key - 65) % 26 + 65
            result += chr(shifted)
        else:
            result += char
    return result

# Create a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    # Send a message to the server with the message and key separated by a pipe (|)
    message = "Hello, server!"
    key = 3
    message_with_key = f"{message}|{key}"
    sock.sendto(message_with_key.encode(), (SERVER_HOST, SERVER_PORT))

    # Receive a response from the server
    data, addr = sock.recvfrom(1024)
    decrypted_message = caesar_cipher(data.decode(), key)
    print(f"Received message: {decrypted_message} from {addr}")