import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('Conectando na {} porta {}'.format(*server_address))
sock.connect(server_address)
while True:
    message = input(str('Escreva a mensagem: '))
    mensagem = bytes(message, encoding = 'utf-8')
    print('Enviado {!r}'.format(mensagem))
    sock.sendall(mensagem)

    amount_received = 0
    amount_expected = len(mensagem)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('Recebido {!r}'.format(data))
    if message == 'close 00':
        print('Fechando socket')
        sock.close()