import socket
import threading

HOST = 'localhost'
PORT = 8000


def handle_connection(conn, addr):
    print(f'Connected by {addr}')

    while True:
        data = conn.recv(1024)
        if not data:
            break

        conn.sendall(data)

    conn.close()
    print(f'Connection with {addr} closed')


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        print(f'Server listening on {HOST}:{PORT}')

        while True:
            conn, addr = server_socket.accept()
            print(f'Accepted connection from {addr}')

            # create a new thread to handle the connection
            thread = threading.Thread(target=handle_connection, args=(conn, addr))
            thread.start()


if __name__ == '__main__':
    main()