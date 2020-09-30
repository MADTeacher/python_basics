import sys

from PySide2.QtWidgets import QApplication, QButtonGroup, QWidget
# подключаем сгенерированный виджет
from questionnairewidget import Ui_QuestionnaireWidget


class MainWindow(QWidget):
    ratings = {"0": "Ужасно",
               "1": "Ну, такое",
               "2": "Нормально",
               "3": "Отлично"
               }

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_QuestionnaireWidget()
        self.ui.setupUi(self)
        scale_bg = QButtonGroup(self)
        scale_bg.addButton(self.ui.awfulCb)
        scale_bg.addButton(self.ui.soSoCb)
        scale_bg.addButton(self.ui.normalCb)
        scale_bg.addButton(self.ui.excellentCb)
        # устанавливаем метод отработки варианта выбора
        scale_bg.buttonClicked.connect(self.checkboxClicked)

    def checkboxClicked(self, cb):
        self.ui.answerLabel.setText(f"Выбрано: {self.ratings[cb.text()]} "
                                    f"({cb.text()})")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())