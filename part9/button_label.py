import sys
from PySide2.QtWidgets import QApplication, QWidget, \
    QLabel, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # Вызываем конструктор базового класса QWidget
        self.label = QLabel(self)
        self.button = QPushButton('Ok', self)
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 300)  # размер виджета
        self.setWindowTitle('Hello World with Qt')

        self.label.setText("Нажми на кнопку!")
        self.label.move(60, 30)  # позиция QLabel на виджете

        # задаем вызываемый метод экземпляра класса при нажатии кнопки
        self.button.clicked.connect(self.buttonClicked)
        self.button.move(80, 70)  # позиция QPushButton на виджете
        self.show()

    def buttonClicked(self):
        self.label.setText("Ура!")
        self.button.setText("^_^")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())