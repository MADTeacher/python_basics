import sys
from PySide2.QtWidgets import (QApplication, QWidget,
                             QLabel, QLineEdit, QPushButton)
from PySide2.QtCore import Qt

class MainWindow(QWidget): # Inherits QWidget
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.button = QPushButton('Очистить', self)
        self.line_edit = QLineEdit(self)
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('QLineEdit Test')
        QLabel("Введите login", self).move(100, 10)
        name_label = QLabel("Login:", self)
        name_label.move(70, 50)
        self.line_edit.setAlignment(Qt.AlignLeft)  # выравнивание по левому краю
        self.line_edit.move(130, 50)
        self.line_edit.resize(200, 20)
        self.button.clicked.connect(self.clearEntries)
        self.button.move(160, 110)
        self.show()

    def clearEntries(self):
        # получаем ссылку на объект генерирующий сигнал
        sender = self.sender()
        # Проверяем, что это кнопка с надписью "Очистить"
        if sender.text() == 'Очистить':
            self.line_edit.clear()  # очищаем текст

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())