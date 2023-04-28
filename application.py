from cProfile import label
from time import time
from tkinter import *
import tkinter
from cliente import Cliente
import threading
import time
import sys

class Application:
    def __init__(self,master=None):
        self.cliente =  Cliente()
     
        self.fontePadrao = ('verdana',8,'bold')
        self.coneccao = Tk()
        self.chat = Toplevel(master=None)
        self.threadAtualizar = threading.Thread(target=self.atualizarChat, args=())
        
        self.coneccao.resizable(True,True)
        self.coneccao.minsize(width = 500, height = 400) 
        self.coneccao.maxsize(width = 1000, height = 1000) 

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer["pady"] = 5
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 30
        self.quartoContainer["pady"] = 5
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer["pady"] = 5
        self.quintoContainer.pack()

        self.sextoContainer = Frame(master)
        self.sextoContainer["padx"] = 20
        self.sextoContainer["pady"] = 5
        self.sextoContainer.pack()
       
        self.ipLabel = Label(self.terceiroContainer,text="Ip do sevidor: ", font=self.fontePadrao)
        self.ipLabel.pack(side=LEFT)

        self.ip = Entry(self.terceiroContainer)
        self.ip["width"] = 20
        self.ip["font"] = self.fontePadrao
        self.ip.pack(side=LEFT)

        self.portaLabel = Label(self.quartoContainer, text="Porta servidor: ", font=self.fontePadrao)
        self.portaLabel.pack(side=LEFT)

        self.porta = Entry(self.quartoContainer)
        self.porta["width"] = 30
        self.porta.pack(side=RIGHT)

        self.identificadorLabel = Label(self.quintoContainer, text="Identificador: ", font=self.fontePadrao)
        self.identificadorLabel.pack(side=LEFT)

        self.identificador = Entry(self.quintoContainer)
        self.identificador["width"] = 30
        self.identificador.pack(side=RIGHT)

        self.conectar = Button(self.sextoContainer,text="Conectar",bd=2,bg='#9c3337',fg='white',font=('verdana',8,'bold'))
        self.conectar["width"] = 10
        self.conectar["command"] = self.conexao
        self.conectar.pack(side=RIGHT)

        self.chat.title("chat") 
        self.chat.geometry("500x400") 

        self.chat.primeiroContainer = Frame(master=self.chat)
        self.chat.primeiroContainer["padx"] = 20
        self.chat.primeiroContainer["pady"] = 5
        self.chat.primeiroContainer.pack()

        self.chat.segundoContainer = Frame(master=self.chat)
        self.chat.segundoContainer["padx"] = 30
        self.chat.segundoContainer["pady"] = 5
        self.chat.segundoContainer.pack()

        self.chat.terceiroContainer = Frame(master=self.chat)
        self.chat.terceiroContainer["padx"] = 30
        self.chat.terceiroContainer["pady"] = 20
        self.chat.terceiroContainer.pack()

        self.chat.mensagem = Entry(self.chat.primeiroContainer)
        self.chat.mensagem["width"] = 30
        self.chat.mensagem.pack(side=LEFT)

        self.chat.enviar = Button(self.chat.primeiroContainer,text="Enviar",bd=2,bg='#3ea528',fg='white',font=('verdana',8,'bold'))
        self.chat.enviar["width"] = 10
        self.chat.enviar["command"] = self.mandarMensagem
        self.chat.enviar.pack(side=LEFT)

        self.chat.sair = Button(self.chat.primeiroContainer,text="Sair",bd=2,bg='#9c3337',fg='white',font=('verdana',8,'bold'))
        self.chat.sair["width"] = 10
        self.chat.sair["command"] = self.sairChat
        self.chat.sair.pack(side=RIGHT)

        self.chat.texto = tkinter.Text(self.chat, height = 50, width = 500, state=NORMAL) 
        self.chat.texto.pack()

    def sairChat(self):
        self.cliente.sairChat()
        self.chat.destroy()
        sys.exit(1)

    def mandarMensagem(self):
        self.cliente.mensagem = self.chat.mensagem.get()
        self.cliente.enviarMensagem()
        self.chat.mensagem.delete(0,'end')

    def atualizarChat(self):
        while True:
            tamanho = len(self.cliente.recebidas)
            if tamanho > 0:
                self.chat.texto.insert(tkinter.END, f"{self.cliente.recebidas[0]} \n")
                self.cliente.recebidas.pop()
                time.sleep(1)

    def limparCampos(self):
        self.ip.delete(0,'end')
        self.porta.delete(0,'end')
        self.identificador.delete(0,'end')

    def conexao(self):
        self.cliente.IP = self.ip.get()
        self.cliente.PORTA = int(self.porta.get())
        self.cliente.identificador = self.identificador.get()
        try:
            self.cliente.conectarServer()
            self.cliente.thread1.start()
            self.threadAtualizar.start()
            self.coneccao.withdraw()
        except Exception:
            self.limparCampos()
   
app = Application()
app.coneccao.mainloop()



