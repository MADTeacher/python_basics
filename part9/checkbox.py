import sys
from PySide2.QtWidgets import (QApplication, QWidget,
                               QCheckBox, QLabel)
from PySide2.QtCore import Qt


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.label.setMinimumSize(200, 10)
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 250, 250)
        self.setWindowTitle('QCheckBox Test')
        self.label.move(30, 200)
        header_label = QLabel(self)
        header_label.setText("Во сколько вы просыпаетесь?")
        header_label.setWordWrap(True)
        header_label.move(10, 10)
        header_label.resize(230, 60)
        morning6 = QCheckBox("6 утра", self)  # text, parent
        morning6.move(20, 80)
        morning6.stateChanged.connect(self.printChoose)
        morning7 = QCheckBox("7 утра", self)  # text, parent
        morning7.move(20, 100)
        morning7.stateChanged.connect(self.printChoose)
        never_sleep = QCheckBox("Я вообще не сплю", self)  # text, parent
        never_sleep.move(20, 120)
        never_sleep.stateChanged.connect(self.printChoose)
        self.show()

    def printChoose(self, state):
        sender = self.sender()
        if state == Qt.Checked:
            choose = f"Выбрано: {sender.text()}."
        else:
            choose = f"Отменен выбор: {sender.text()}."
        self.label.setText(choose)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())