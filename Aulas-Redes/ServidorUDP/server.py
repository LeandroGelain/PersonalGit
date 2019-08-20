import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 5000)
print('startando na {} porta {}'.format(*server_address))
sock.bind(server_address)
try:
    print("Ctrl + C para parar.")
    while True:
        print('\nEsperando receber mensagem')
        data, address = sock.recvfrom(4096)

        print('Recenbendo {} bytes da {}'.format(len(data), address))
        print(data)

        if data:
            sent = sock.sendto(data, address)
            print('Enviando {} bytes de volta {}'.format(sent, address))

except KeyboardInterrupt:
    print('Fim do Programa!')