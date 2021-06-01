import sys, os
# if hasattr(sys, 'frozen'):
#     os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

# from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import platform
import ctypes

import Memory_Allocator
import memory_allocator_rc
from memory_allocator_rc import *

from PyQt5.uic import loadUiType

Memory_Allocator, _ = loadUiType('Memory_Allocator.ui')


class MainApp(QMainWindow, Memory_Allocator):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.onlyInt = QIntValidator()
        self.setupUi(self)
        self.ui = Memory_Allocator
        self.handle_buttons()

    def handle_buttons(self):
        self.next.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.back.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.show()


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()
    input()


if __name__ == '__main__':
    main()
