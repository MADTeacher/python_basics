import sys
from PySide2.QtWidgets import QApplication, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # Вызываем конструктор базового класса QWidget
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 300)  # размер виджета
        self.setWindowTitle('Hello World with Qt')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
