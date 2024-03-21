import os
import sys
import struct
from Crypto.Cipher import AES
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QFont
from notifypy import Notify
import random
import string
import userpaths
import guardshield
import subprocess
import time
import multiprocessing as mp
import ctypes
import win32gui
import win32con
import win32api
import math
import winsound
import winreg as reg
import requests


class caferisimDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cafer")
        self.init_ui()
    def init_ui(self):
        layout = QVBoxLayout()
        self.caferisim_input = QLineEdit()
        layout.addWidget(self.caferisim_input)
        ask_caferisim_button = QPushButton("İsmin nedir?")
        ask_caferisim_button.clicked.connect(self.ask_caferisim)
        layout.addWidget(ask_caferisim_button)
        self.setLayout(layout)
    def ask_caferisim(self):
        caferisim = self.caferisim_input.text()
        if caferisim:
            QMessageBox.information(self, "İsiminiz", f"Merhaba, {caferisim}")
            self.hmmm_cafer()
        else:
            QMessageBox.warning(self, "HATA", "Erişim Reddedildi Lütfen Kendinizi tanıtın.")
    def hmmm_cafer(self):
        reply = QMessageBox.question(self, "Cafer", "Tamam mı?", QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            QMessageBox.information(self, "TAMAM", "....")
        else:
            QMessageBox.information(self, "Hata", "Cafergggg ")
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = caferisimDialog()
    dialog.show()
    sys.exit(app.exec())
    
