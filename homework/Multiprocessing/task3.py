import multiprocessing
import socket

def handle_connection(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
    conn.close()

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 8080))
        s.listen()
        print('Server started')
        while True:
            conn, addr = s.accept()
            print(f'Connected by {addr}')
            p = multiprocessing.Process(target=handle_connection, args=(conn,))
            p.start()
