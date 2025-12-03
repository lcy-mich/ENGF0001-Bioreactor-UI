# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'initialdialog.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(449, 156)
        Dialog.setMinimumSize(QSize(449, 156))
        Dialog.setMaximumSize(QSize(449, 156))
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(-1, -1, 451, 157))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(15, 15, 15, 10)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.hostLine = QLineEdit(self.formLayoutWidget)
        self.hostLine.setObjectName(u"hostLine")
        self.hostLine.setEchoMode(QLineEdit.EchoMode.Normal)
        self.hostLine.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.hostLine)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.portLine = QLineEdit(self.formLayoutWidget)
        self.portLine.setObjectName(u"portLine")
        self.portLine.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.portLine)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.keepaliveLine = QLineEdit(self.formLayoutWidget)
        self.keepaliveLine.setObjectName(u"keepaliveLine")
        self.keepaliveLine.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.keepaliveLine)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.topicLine = QLineEdit(self.formLayoutWidget)
        self.topicLine.setObjectName(u"topicLine")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.topicLine)

        self.isSimulatedCheckBox = QCheckBox(self.formLayoutWidget)
        self.isSimulatedCheckBox.setObjectName(u"isSimulatedCheckBox")
        self.isSimulatedCheckBox.setChecked(True)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.isSimulatedCheckBox)

        self.decisionBox = QDialogButtonBox(self.formLayoutWidget)
        self.decisionBox.setObjectName(u"decisionBox")
        self.decisionBox.setStandardButtons(QDialogButtonBox.StandardButton.NoButton)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.SpanningRole, self.decisionBox)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Initial Information Confirmation (haha it rhymes)", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Host:", None))
        self.hostLine.setText(QCoreApplication.translate("Dialog", u"engf0001.cs.ucl.ac.uk", None))
        self.hostLine.setPlaceholderText(QCoreApplication.translate("Dialog", u"Type MQTT host address here...", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Port:", None))
        self.portLine.setText(QCoreApplication.translate("Dialog", u"1883", None))
        self.portLine.setPlaceholderText(QCoreApplication.translate("Dialog", u"Type port number here...", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Keep Alive:", None))
        self.keepaliveLine.setText(QCoreApplication.translate("Dialog", u"60", None))
        self.keepaliveLine.setPlaceholderText(QCoreApplication.translate("Dialog", u"Type keep_alive in seconds here...", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Topic:", None))
        self.topicLine.setText(QCoreApplication.translate("Dialog", u"bioreactor_sim/nofaults/telemetry/summary", None))
        self.topicLine.setPlaceholderText(QCoreApplication.translate("Dialog", u"Type subscribed topic here...", None))
        self.isSimulatedCheckBox.setText(QCoreApplication.translate("Dialog", u"is simulated?", None))
    # retranslateUi

