import sys
from PyQt5.QtWidgets import QApplication, QSplashScreen
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from gui.home import MainWindow



if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Carga y muestra el splash screen
    splash_pix = QPixmap('/home/pi/Documents/edrum/src/resources/images/g-drum.jpg')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.showMessage("Loading...", Qt.AlignBottom | Qt.AlignCenter, Qt.white)
    splash.show()
    app.processEvents()  # Asegura que el splash screen se muestre inmediatamente

    # Inicializa la ventana principal
    mainWin = MainWindow()

    # Función para simular la carga de componentes
    def finishSplash():
        splash.finish(mainWin)  # Cierra el splash screen
        mainWin.showFullScreen()  # Muestra la ventana principal

    # Cierra el splash screen después de un retraso y muestra la ventana principal
    QTimer.singleShot(3000, finishSplash)  # Ajusta este tiempo según tus necesidades
    
    sys.exit(app.exec_())