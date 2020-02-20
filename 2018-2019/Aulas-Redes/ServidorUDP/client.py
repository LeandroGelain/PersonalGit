import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 5000)
try:
    print('Ctrl + C para parar.')
    while True:
        message = input(str("Escreva a mensagem: "))
        print('Enviando {!r}'.format(message))
        b1 = bytes(message, encoding = 'utf-8')
        sent = sock.sendto(b1, server_address)

        print('Esperando resposta')
        data, server = sock.recvfrom(4096)
        print('Recebido {!r}'.format(data))
        if message == 'close 00':
            print('closing socket')
            sock.close()
except KeyboardInterrupt:
    print('Fim do Programa!')