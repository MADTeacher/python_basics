import sys
from PySide2.QtWidgets import (QApplication, QWidget,
                               QLabel, QTextEdit,
                               QLineEdit, QPushButton,
                               QCheckBox, QGridLayout,
                               QVBoxLayout, QMainWindow, QMessageBox)
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt, Slot, Signal


class ToDoListWidget(QWidget):

    doneSignal = Signal(str, str)
    warningSignal = Signal(str)

    def __init__(self, parent=None):
        super(ToDoListWidget, self).__init__(parent)
        self.dictToDo = {}
        self.dayMeet = []
        self.initializeUI()
        for it in self.dictToDo:
            it.clicked.connect(self.itIsDone)

    def initializeUI(self):
        main_grid = QGridLayout()
        todo_title = QLabel("Список дел на день")
        todo_title.setFont(QFont('Arial', 24))
        todo_title.setAlignment(Qt.AlignCenter)
        # создание меток
        mustdo_label = QLabel("Надо сделать")
        mustdo_label.setFont(QFont('Arial', 20))
        mustdo_label.setAlignment(Qt.AlignCenter)
        appts_label = QLabel("Запланированные встречи")
        appts_label.setFont(QFont('Arial', 20))
        appts_label.setAlignment(Qt.AlignCenter)
        # создание секций
        mustdo_grid = QGridLayout()
        mustdo_grid.setContentsMargins(5, 5, 5, 5)
        mustdo_grid.addWidget(mustdo_label, 0, 0, 1, 2)
        # создание чекбоксов с полями ввода
        for position in range(1, 15):
            checkbox = QCheckBox()
            checkbox.setObjectName(str(position))
            linedit = QLineEdit("")
            linedit.setMinimumWidth(200)
            mustdo_grid.addWidget(checkbox, position, 0)
            mustdo_grid.addWidget(linedit, position, 1)
            self.dictToDo[checkbox] = linedit

        # секция встреч
        morning_label = QLabel("Утро")
        morning_label.setFont(QFont('Arial', 16))
        noon_label = QLabel("Обед")
        noon_label.setFont(QFont('Arial', 16))
        evening_label = QLabel("Вечер")
        evening_label.setFont(QFont('Arial', 16))
        # первичная компоновка
        appt_v_box = QVBoxLayout()
        appt_v_box.setContentsMargins(5, 5, 5, 5)
        evening_entry = QTextEdit()
        noon_entry = QTextEdit()
        morning_entry = QTextEdit()
        appt_v_box.addWidget(appts_label)
        appt_v_box.addWidget(morning_label)
        appt_v_box.addWidget(morning_entry)
        appt_v_box.addWidget(noon_label)
        appt_v_box.addWidget(noon_entry)
        appt_v_box.addWidget(evening_label)
        appt_v_box.addWidget(evening_entry)
        self.dayMeet = [morning_entry, noon_entry, evening_entry]
        # завершение компоновки
        main_grid.addWidget(todo_title, 0, 0, 1, 2)
        main_grid.addLayout(mustdo_grid, 1, 0)
        main_grid.addLayout(appt_v_box, 1, 1)
        self.setLayout(main_grid)

    def itIsDone(self):
        sender = self.sender()
        # запрет на выполнение пустого элемента списка дел
        if not self.dictToDo[sender].text():
            sender.setChecked(False)
            self.warningSignal.emit(sender.objectName())
            return
        if sender.isChecked():
            self.doneSignal.emit(sender.objectName(), self.dictToDo[sender].text())

    @Slot()
    def clearToDoList(self):
        for it in self.dayMeet:
            it.clear()
        for checkbox, edit in self.dictToDo.items():
            checkbox.setChecked(False)
            edit.setText("")


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.todo = ToDoListWidget()
        self.todo.show()
        self.todo.doneSignal.connect(self.itIsDone)
        self.todo.warningSignal.connect(self.warningDone)
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle('Список дел')
        close_button = QPushButton("Закрыть")
        close_button.clicked.connect(self.close)
        clear_button = QPushButton("Очистить")
        clear_button.clicked.connect(self.todo.clearToDoList)
        v_box = QVBoxLayout()
        #v_box.addWidget(self.todo)
        v_box.addWidget(clear_button)
        v_box.addWidget(close_button)
        widget = QWidget(self)
        widget.setLayout(v_box)
        self.setCentralWidget(widget)
        self.setMaximumHeight(500)
        self.show()

    @Slot(str, str)
    def itIsDone(self, number, description):
        QMessageBox().information(self, "Внимание!",
                                  f"Дело '{description}' под №{number} выполнено!",
                                  QMessageBox.Ok, QMessageBox.Ok)

    @Slot(str)
    def warningDone(self, number):
        QMessageBox().warning(self, "Внимание!", f"Дело №{number} не заполнено!",
                              QMessageBox.Ok, QMessageBox.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())