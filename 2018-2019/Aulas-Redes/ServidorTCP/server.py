import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print(' startando na {} porta {}'.format(*server_address))
sock.bind(server_address)

sock.listen(1)

while True:
    print('Esperando pela conexão')
    connection, client_address = sock.accept()
    try:
        print('Conexão de', client_address)

        while True:
            data = connection.recv(16)
            print('Recebido {!r}'.format(data))
            if data:
                print('Enviando de volta')
                connection.sendall(data)
            else:
                print('Sem mensagem do cliente', client_address)
                break

    finally:
        connection.close()