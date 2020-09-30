# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'questionnairewidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_QuestionnaireWidget(object):
    def setupUi(self, QuestionnaireWidget):
        if not QuestionnaireWidget.objectName():
            QuestionnaireWidget.setObjectName(u"QuestionnaireWidget")
        QuestionnaireWidget.resize(555, 318)
        self.verticalLayout_5 = QVBoxLayout(QuestionnaireWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(QuestionnaireWidget)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_6)

        self.label_5 = QLabel(QuestionnaireWidget)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        self.verticalSpacer = QSpacerItem(20, 56, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(QuestionnaireWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)

        self.awfulCb = QCheckBox(QuestionnaireWidget)
        self.awfulCb.setObjectName(u"awfulCb")
        self.awfulCb.setFont(font1)

        self.horizontalLayout_4.addWidget(self.awfulCb)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(QuestionnaireWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.soSoCb = QCheckBox(QuestionnaireWidget)
        self.soSoCb.setObjectName(u"soSoCb")
        self.soSoCb.setFont(font1)

        self.horizontalLayout_3.addWidget(self.soSoCb)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(QuestionnaireWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.normalCb = QCheckBox(QuestionnaireWidget)
        self.normalCb.setObjectName(u"normalCb")
        self.normalCb.setFont(font1)

        self.horizontalLayout_2.addWidget(self.normalCb)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(QuestionnaireWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.excellentCb = QCheckBox(QuestionnaireWidget)
        self.excellentCb.setObjectName(u"excellentCb")
        self.excellentCb.setFont(font1)

        self.horizontalLayout.addWidget(self.excellentCb)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_5.addLayout(self.verticalLayout)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 55, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.answerLabel = QLabel(QuestionnaireWidget)
        self.answerLabel.setObjectName(u"answerLabel")
        self.answerLabel.setFont(font1)
        self.answerLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.answerLabel)

        self.closeButton = QPushButton(QuestionnaireWidget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setFont(font1)

        self.verticalLayout_5.addWidget(self.closeButton)


        self.retranslateUi(QuestionnaireWidget)

        QMetaObject.connectSlotsByName(QuestionnaireWidget)
    # setupUi

    def retranslateUi(self, QuestionnaireWidget):
        QuestionnaireWidget.setWindowTitle(QCoreApplication.translate("QuestionnaireWidget", u"Test GUI Qt Designer", None))
        self.label_6.setText(QCoreApplication.translate("QuestionnaireWidget", u"\u0412\u0435\u0447\u0435\u0440\u043d\u0438\u0439 \u043e\u043f\u0440\u043e\u0441", None))
        self.label_5.setText(QCoreApplication.translate("QuestionnaireWidget", u"\u041d\u0430\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u043f\u043b\u043e\u0434\u043e\u0442\u0432\u043e\u0440\u043d\u043e \u043f\u0440\u043e\u0448\u0435\u043b \u0412\u0430\u0448 \u0434\u0435\u043d\u044c?", None))
        self.label.setText(QCoreApplication.translate("QuestionnaireWidget", u"\u0423\u0436\u0430\u0441\u043d\u043e", None))
        self.awfulCb.setText(QCoreApplication.translate("QuestionnaireWidget", u"0", None))
        self.label_2.setText(QCoreApplication.translate("QuestionnaireWidget", u"\u041d\u0443, \u0442\u0430\u043a\u043e\u0435", None))
        self.soSoCb.setText(QCoreApplication.translate("QuestionnaireWidget", u"1", None))
        self.label_3.setText(QCoreApplication.translate("QuestionnaireWidget", u"\u041d\u043e\u0440\u043c\u0430\u043b\u044c\u043d\u043e", None))
        self.normalCb.setText(QCoreApplication.translate("QuestionnaireWidget", u"2", None))
        self.label_4.setText(QCoreApplication.translate("QuestionnaireWidget", u"\u041e\u0442\u043b\u0438\u0447\u043d\u043e", None))
        self.excellentCb.setText(QCoreApplication.translate("QuestionnaireWidget", u"3", None))
        self.answerLabel.setText(QCoreApplication.translate("QuestionnaireWidget", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043e: ", None))
        self.closeButton.setText(QCoreApplication.translate("QuestionnaireWidget", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

