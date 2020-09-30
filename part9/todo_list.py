from PySide2.QtWidgets import (QWidget, QLabel, QTextEdit,
                               QLineEdit, QPushButton,
                               QCheckBox, QGridLayout,
                               QVBoxLayout)
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt, Signal


class ToDoList(QWidget):

    doneSignal = Signal(str, str)
    warningSignal = Signal(str)

    def __init__(self, parent=None):
        super(ToDoList, self).__init__(parent)
        self.dictToDo = {}
        self.clear_button = QPushButton("Очистить")
        self.clear_button.clicked.connect(self.clearToDoList)
        self.dayMeet = []
        self.initializeUI()
        for it in self.dictToDo:
            it.clicked.connect(self.itIsDone)

    def initializeUI(self):
        main_grid = QGridLayout()
        todo_title = QLabel("Список дел на день")
        todo_title.setFont(QFont('Arial', 24))
        todo_title.setAlignment(Qt.AlignCenter)

        # create section labels for to do list
        mustdo_label = QLabel("Надо сделать")
        mustdo_label.setFont(QFont('Arial', 20))
        mustdo_label.setAlignment(Qt.AlignCenter)
        appts_label = QLabel("Запланированные встречи")
        appts_label.setFont(QFont('Arial', 20))
        appts_label.setAlignment(Qt.AlignCenter)

        # create must do section
        mustdo_grid = QGridLayout()
        mustdo_grid.setContentsMargins(5, 5, 5, 5)

        mustdo_grid.addWidget(mustdo_label, 0, 0, 1, 2)

        # create checkboxes and line edit widgets
        for position in range(1, 15):
            checkbox = QCheckBox()
            checkbox.setObjectName(str(position))
            linedit = QLineEdit("")
            linedit.setMinimumWidth(200)
            mustdo_grid.addWidget(checkbox, position, 0)
            mustdo_grid.addWidget(linedit, position, 1)
            self.dictToDo[checkbox] = linedit

        # create labels for appointments section
        morning_label = QLabel("Утро")
        morning_label.setFont(QFont('Arial', 16))
        noon_label = QLabel("Обед")
        noon_label.setFont(QFont('Arial', 16))
        evening_label = QLabel("Вечер")
        evening_label.setFont(QFont('Arial', 16))
        # create vertical layout and add widgets
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
        # add other layouts to main grid layout
        main_grid.addWidget(todo_title, 0, 0, 1, 2)
        main_grid.addLayout(mustdo_grid, 1, 0)
        main_grid.addLayout(appt_v_box, 1, 1)
        main_grid.addWidget(self.clear_button, 2, 0, 1, 2)
        self.setLayout(main_grid)

    def itIsDone(self):
        sender = self.sender()
        # запрет на выполнение пустого элемента списка дел
        if not self.dictToDo[sender].text():
            sender.setChecked(False)
            self.warningSignal.emit("1")
            self.warningSignal.emit(sender.objectName())
            return
        if sender.isChecked():
            self.doneSignal.emit(sender.objectName(), self.dictToDo[sender].text())

    def clearToDoList(self):
        for it in self.dayMeet:
            it.clear()

        for checkbox, edit in self.dictToDo.items():
            checkbox.setChecked(False)
            edit.setText("")