import socket
import threading

class Cliente:
    def __init__(self):
        self.IP = ""
        self.PORTA = ""
        self.identificador = ""
        self.mensagem = ""
        self.recebidas = []
        self.cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.thread1 = threading.Thread(target=self.receberMensagem,args=()) 

    def conectarServer(self):
        try:
            self.cliente.connect((self.IP,self.PORTA))
            print(f'Conexão estabelecida em: {self.IP}:{self.PORTA}')
        except:
            print(f'Erro de conexão em: {self.IP}:{self.PORTA}')
            raise Exception

    def receberMensagem(self):
        fim = False
        while fim == False:
            try:
                mensagem = self.cliente.recv(2048).decode('ascii')
                if mensagem=='getUser':
                    self.cliente.send(self.identificador.encode('ascii'))
                else:
                    self.recebidas.append(mensagem)
            except:
                print('Erro: cheque suas entradas')
                fim = True

    def enviarMensagem(self):
        self.cliente.send(self.mensagem.encode('ascii'))

    def sairChat(self):
        self.cliente.close()
