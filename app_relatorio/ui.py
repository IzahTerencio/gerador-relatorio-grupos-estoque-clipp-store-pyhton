# importing libraries
from PySide6.QtWidgets import *
from PySide6 import QtCore, QtGui
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys


class Window(QMainWindow): # Definição da classe
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerador de Relatório de Grupos de Estoque") # Título da janela principal
        self.setGeometry(100, 100, 1000, 600) # Setando as proporções da janela
        self.setStyleSheet("background-color: #E8E6D1;")
        self.UiComponents()
        self.show()

    def UiComponents(self):
        label_start = QLabel(self)
        label_start.setText("<h2>Selecione a data inicial<h2>")
        label_start.setStyleSheet("color: #363636")
        label_start.setMinimumWidth(300)
        label_start.move(180, 20)

        calendar_start = QCalendarWidget(self) # creating a QCalendarWidget object
        calendar_start.setGeometry(50, 50, 500, 200) # setting geometry to the calendar
        calendar_start.setStyleSheet("background-color: #363636;")

        label_end = QLabel(self)
        label_end.setText("<h2>Selecione a data final<h2>")
        label_end.setStyleSheet("color: #363636")
        label_end.setMinimumWidth(300)
        label_end.move(580, 320)

        calendar_end = QCalendarWidget(self)
        calendar_end.setGeometry(450, 350, 500, 200)
        calendar_end.setStyleSheet("background-color: #363636;")

        lbl_logo_soft = QLabel(self)
        lbl_logo_soft.set



# Call the user interactive  function
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())