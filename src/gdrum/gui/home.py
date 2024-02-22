import sys
from PyQt5.QtWidgets import QApplication, QSplashScreen, QMainWindow
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap

# Simula la inicialización de la ventana principal para el ejemplo
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("G-Drum")
        self.setGeometry(100, 100, 800, 480)  # Ajusta esto según el tamaño de tu pantalla
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.showNormal() 


