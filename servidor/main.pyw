from model.modelTelaSistema import ModelTelaSistema
from controller.controllerTelaSistema import ControllerTelaSistema
from PyQt5.QtWidgets import QApplication

import sys


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = ModelTelaSistema()
        self.dados = sys_argv[1:]
        if len(self.dados)>2:
            for x in range(1, len(self.dados)-2):
                self.dados[2]+=" "+self.dados[x+2]
        self.view = ControllerTelaSistema(self.model, self.dados)
        self.view.show()


if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec())
