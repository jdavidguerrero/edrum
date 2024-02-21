import sys
from PyQt5.QtWidgets import QApplication, QSplashScreen, QMainWindow
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap

# Simula la inicialización de la ventana principal para el ejemplo
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tambor Electrónico")
        self.setGeometry(100, 100, 800, 480)  # Ajusta esto según el tamaño de tu pantalla

def main():
    app = QApplication(sys.argv)
    
    # Carga la imagen del splash screen
    splash_pix = QPixmap('/home/pi/Documents/edrum/resources/images/g-drum.jpg')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    
    # Muestra un mensaje en el splash screen (opcional)
    splash.showMessage("Cargando...", Qt.AlignBottom | Qt.AlignCenter, Qt.white)
    splash.show()
    
    # Asegúrate de que el splash screen tenga tiempo para mostrarse correctamente
    app.processEvents()
    
    # Inicializa la ventana principal (aquí deberías cargar o inicializar tu aplicación real)
    window = MainWindow()

    # Función para simular la carga de componentes y cerrar el splash screen
    def load_components():
        # Aquí es donde se inicializaría tu aplicación real
        print("Cargando componentes de la aplicación...")
        splash.finish(window)  # Cierra el splash screen
        window.show()  # Muestra la ventana principal

    # Usa un QTimer para simular el tiempo de carga y luego mostrar la ventana principal
    QTimer.singleShot(5000, load_components)  # Ajusta el tiempo según sea necesario
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()