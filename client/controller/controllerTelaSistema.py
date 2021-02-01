from PyQt5.QtWidgets import QMainWindow
from view.telaSistema import Ui_janelaPrincipal as Ui_MainWindow
import random, threading, time
from datetime import datetime
import socket

class ControllerTelaSistema(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.tela = Ui_MainWindow()
        self.tela.setupUi(self)
        self.caixa = self.busca_dados()
        print(self.caixa)
        
    def busca_dados(self):
        arquivo = open("config.txt", 'r')
        dados = arquivo.readlines()
        arquivo.close()
        return dados
    
    def clicado_1(self):
        preparar_mensagem(1)
    def clicado_2(self):
        preparar_mensagem(2)
    def clicado_3(self):
        preparar_mensagem(3)
        
    def preparar_mensagem(self,botao):
        mensagem = {
            "botao": botao,
            "caixa": self.caixa,
            obs:"teste",
        }
        
        self.enviar_mensagem(mensagem)
        
    def enviar_mensagem(self, mensagem):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((socket.gethostbyname("23.1.1.250"),12397))
        self.clientsocket.send(bytes(mensagem, "utf-8"))
        self.clientsocket.close()