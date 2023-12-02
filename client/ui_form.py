# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        Widget.setStyleSheet(u"QFrame {\n"
"        background-color: #4A90E2;\"\n"
"        border: 2px solid #4A90E2;\"\n"
"    }")
        self.formLayoutWidget = QWidget(Widget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(130, 50, 531, 321))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(10, 5, 10, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.record = QPushButton(self.formLayoutWidget)
        self.record.setObjectName(u"record")
        self.record.setStyleSheet(u"    QPushButton {\n"
"        background-color: #4A90E2;\n"
"        border: 2px solid #4A90E2;\n"
"        color: #FFFFFF;\n"
"        border-radius: 5px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #357ABD;\n"
"        border: 2px solid #357ABD;\n"
"    }\n"
"    QPushButton:pressed {\n"
"       background-color: #27679F;\n"
"       border: 2px solid #27679F;\n"
"    }")

        self.horizontalLayout.addWidget(self.record)

        self.line_2 = QFrame(self.formLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.cancel = QPushButton(self.formLayoutWidget)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setStyleSheet(u"    QPushButton {\n"
"        background-color: #4A90E2;\n"
"        border: 2px solid #4A90E2;\n"
"        color: #FFFFFF;\n"
"        border-radius: 5px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #357ABD;\n"
"        border: 2px solid #357ABD;\n"
"    }\n"
"    QPushButton:pressed {\n"
"       background-color: #27679F;\n"
"       border: 2px solid #27679F;\n"
"    }")

        self.horizontalLayout.addWidget(self.cancel)


        self.formLayout.setLayout(0, QFormLayout.SpanningRole, self.horizontalLayout)

        self.textEdit = QTextEdit(self.formLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"    background-color: #FFFFFF;\n"
"    color: #000000;\n"
"    border: 1px solid #4A90E2;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"    border: 1px solid #357ABD;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 1px solid #0078D4;\n"
"    background-color: #E5F6FE;\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.textEdit)

        self.line = QFrame(self.formLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(3)
        self.line.setFrameShape(QFrame.HLine)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.line)

        self.pushButton = QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"    QPushButton {\n"
"        background-color: #4A90E2;\n"
"        border: 2px solid #4A90E2;\n"
"        color: #FFFFFF;\n"
"        border-radius: 5px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #357ABD;\n"
"        border: 2px solid #357ABD;\n"
"    }\n"
"    QPushButton:pressed {\n"
"       background-color: #27679F;\n"
"       border: 2px solid #27679F;\n"
"    }")

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.pushButton)

        self.pushButton_2 = QPushButton(self.formLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"    QPushButton {\n"
"        background-color: #4A90E2;\n"
"        border: 2px solid #4A90E2;\n"
"        color: #FFFFFF;\n"
"        border-radius: 5px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #357ABD;\n"
"        border: 2px solid #357ABD;\n"
"    }\n"
"    QPushButton:pressed {\n"
"       background-color: #27679F;\n"
"       border: 2px solid #27679F;\n"
"    }")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.pushButton_2)

        self.line_3 = QFrame(self.formLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.line_3)

        self.line_4 = QFrame(self.formLayoutWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.line_4)

        self.textEdit_2 = QTextEdit(self.formLayoutWidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setStyleSheet(u"QTextEdit {\n"
"    background-color: #FFFFFF;\n"
"    color: #000000;\n"
"    border: 1px solid #4A90E2;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"    border: 1px solid #357ABD;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 1px solid #0078D4;\n"
"    background-color: #E5F6FE;\n"
"}")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.textEdit_2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.record.setText(QCoreApplication.translate("Widget", u"Record", None))
        self.cancel.setText(QCoreApplication.translate("Widget", u"To text", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Play", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Last Record", None))
    # retranslateUi

