import socket
import threading

HOST = input("Ip host: ")
PORTA = int(input("Porta: "))

servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servidor.bind((HOST,PORTA))
servidor.listen()
print(f'Servidor escutando em: {HOST}:{PORTA}')

clientes = []
identificadores = []

def mensagemGlobal(mensagem):
    for cliente in clientes:
        cliente.send(mensagem)

def tratarCliente(cliente):
    while True:
        try:
            mensagemRecebidaCliente = cliente.recv(2048).decode('ascii')
            mensagemGlobal(f'{identificadores[clientes.index(cliente)]} :{mensagemRecebidaCliente}'.encode('ascii'))
        except:
            clienteRetirado = clientes.index(cliente)
            cliente.close()
            clientes.remove(clientes[clienteRetirado])
            identificadorClienteRetirado = identificadores[clienteRetirado]
            print(f'{identificadorClienteRetirado} saiu do chat...')
            mensagemGlobal(f'{identificadorClienteRetirado} abandonou o grupo...'.encode('ascii'))
            identificadores.remove(identificadorClienteRetirado)
        
def conexaoInicial():
    while True:
        try:
            cliente, endereco = servidor.accept()
            print(f"Nova conexão: {str(endereco)}")
            clientes.append(cliente)
            cliente.send('getUser'.encode('ascii'))
            idCliente = cliente.recv(2048).decode('ascii')
            identificadores.append(idCliente)
            mensagemGlobal(f'{idCliente} juntou-se ao grupo'.encode('ascii'))
            threadUsuario = threading.Thread(target=tratarCliente,args=(cliente,))
            threadUsuario.start()
        except:
            pass

conexaoInicial()
