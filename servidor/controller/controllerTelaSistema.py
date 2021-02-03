from PyQt5.QtWidgets import QMainWindow
from view.telaSistema import Ui_janelaPrincipal as Ui_MainWindow
import random
import threading
import time
from datetime import datetime
import socket


class ControllerTelaSistema(QMainWindow):
    def __init__(self, model, dados):
        super().__init__()
        self.model = model
        self.tela = Ui_MainWindow()
        self.tela.setupUi(self)
        #self.tela.opcao.setText(dados[0][1:-1])
        op = dados[0][1:-1]
        if op == '1':
            self.tela.opcao.setText("CANCELAR ITEM NA VENDA")
        if op == '2':
            self.tela.opcao.setText("CANCELAR VENDA COMPLETA")
        if op == '3':
            self.tela.opcao.setText("PRECISO DE AJUDA NO CAIXA")
        
        self.tela.caixa.setText(dados[1][1:-2])
        self.tela.msg.setPlainText(dados[2][1:-2])
        
        self.tela.fechar.clicked.connect(exit)

