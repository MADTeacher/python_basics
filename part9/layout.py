import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
    QCheckBox, QButtonGroup, QHBoxLayout, QVBoxLayout)
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 230)
        self.setWindowTitle('Layout Test')
        self.displayWidgets()
        self.label.setAlignment(Qt.AlignHCenter)
        self.show()

    def displayWidgets(self):
        # create label and button widgets
        title = QLabel("Вечерний опрос")
        title.setFont(QFont('Arial', 17))
        question = QLabel("Насколько плодотворно прошел Ваш день?")
        question.setAlignment(Qt.AlignHCenter)
        # согдание горизонтального layout-а
        title_h_box = QHBoxLayout()
        title_h_box.addStretch()
        title_h_box.addWidget(title)
        title_h_box.addStretch()
        # Варианты выбора
        ratings = ["Ужасно", "Ну, такое", "Нормально", "Отлично"]

        ratings_h_box = QHBoxLayout()
        # Устанавливаем расстояние между виджетами в горизонтальном layout-е
        ratings_h_box.setSpacing(80)

        ratings_h_box.addStretch()
        for rating in ratings:
            rate_label = QLabel(rating, self)
            ratings_h_box.addWidget(rate_label)
        ratings_h_box.addStretch()

        cb_h_box = QHBoxLayout()
        # расстояние между виджетами в горизонтальном layout-е
        cb_h_box.setSpacing(100)

        # Создаем контейнер для групировки QCheckBox
        scale_bg = QButtonGroup(self)

        cb_h_box.addStretch()
        for cb in range(len(ratings)):
            scale_cb = QCheckBox(str(cb), self)
            cb_h_box.addWidget(scale_cb)
            scale_bg.addButton(scale_cb)
        cb_h_box.addStretch()

        # устанавливаем функцию отработки варианта выбора
        scale_bg.buttonClicked.connect(self.checkboxClicked)
        close_button = QPushButton("Закрыть", self)
        close_button.clicked.connect(self.close)
        # Компануем вертикальный layout последовательно
        # добавляя виджеты and элементы h_box layout
        v_box = QVBoxLayout()
        v_box.addLayout(title_h_box)
        v_box.addWidget(question)
        v_box.addStretch(1)
        v_box.addLayout(ratings_h_box)
        v_box.addLayout(cb_h_box)
        v_box.addStretch(2)
        v_box.addWidget(self.label)
        v_box.addWidget(close_button)
        self.setLayout(v_box)

    def checkboxClicked(self, cb):
        self.label.setText(f"Выбрано: {cb.text()}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())