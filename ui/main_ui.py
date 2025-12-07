# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QMenu,
    QMenuBar, QRadioButton, QSizePolicy, QSlider,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(1120, 560)
        MainWindow.setMinimumSize(QSize(1120, 560))
        MainWindow.setMaximumSize(QSize(1120, 580))
        font = QFont()
        font.setFamilies([u"Consolas"])
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        MainWindow.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(u"icons/control.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color:rgb(224, 227, 235);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"alternate-background-color: rgb(224, 227, 235);")
        MainWindow.setIconSize(QSize(90, 90))
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        MainWindow.setAnimated(False)
        MainWindow.setDocumentMode(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionFullscreen = QAction(MainWindow)
        self.actionFullscreen.setObjectName(u"actionFullscreen")
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_File_As = QAction(MainWindow)
        self.actionSave_File_As.setObjectName(u"actionSave_File_As")
        self.actionSaveAs = QAction(MainWindow)
        self.actionSaveAs.setObjectName(u"actionSaveAs")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionReset_To_Default = QAction(MainWindow)
        self.actionReset_To_Default.setObjectName(u"actionReset_To_Default")
        self.actionChange_Connection = QAction(MainWindow)
        self.actionChange_Connection.setObjectName(u"actionChange_Connection")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setEnabled(True)
        self.centralWidget.setMinimumSize(QSize(1120, 560))
        self.centralWidget.setMaximumSize(QSize(1120, 560))
        self.centralWidget.setStyleSheet(u"background-color:rgb(237, 241, 249);\n"
"color: rgb(0, 0, 0);")
        self.verticalLayoutWidget = QWidget(self.centralWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-1, -1, 2011, 730))
        self.mainLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.mainLayout.setSpacing(5)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(0, 10, 0, 120)
        self.buttonsWidget = QWidget(self.verticalLayoutWidget)
        self.buttonsWidget.setObjectName(u"buttonsWidget")
        self.buttonsWidget.setMinimumSize(QSize(1000, 50))
        self.buttonsWidget.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayoutWidget = QWidget(self.buttonsWidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(-1, -1, 1121, 51))
        self.buttonsLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.buttonsLayout.setSpacing(90)
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.buttonsLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.buttonsLayout.setContentsMargins(60, 0, 60, 0)
        self.heatingButton = QRadioButton(self.horizontalLayoutWidget)
        self.heatingButton.setObjectName(u"heatingButton")
        font1 = QFont()
        font1.setFamilies([u"Noto Sans SC"])
        font1.setPointSize(14)
        font1.setBold(False)
        self.heatingButton.setFont(font1)
        self.heatingButton.setIconSize(QSize(30, 30))
        self.heatingButton.setChecked(True)

        self.buttonsLayout.addWidget(self.heatingButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.stirringButton = QRadioButton(self.horizontalLayoutWidget)
        self.stirringButton.setObjectName(u"stirringButton")
        self.stirringButton.setFont(font1)
        self.stirringButton.setIconSize(QSize(30, 30))

        self.buttonsLayout.addWidget(self.stirringButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.phButton = QRadioButton(self.horizontalLayoutWidget)
        self.phButton.setObjectName(u"phButton")
        self.phButton.setFont(font1)
        self.phButton.setIconSize(QSize(30, 30))

        self.buttonsLayout.addWidget(self.phButton, 0, Qt.AlignmentFlag.AlignHCenter)


        self.mainLayout.addWidget(self.buttonsWidget)

        self.setpointWidget = QWidget(self.verticalLayoutWidget)
        self.setpointWidget.setObjectName(u"setpointWidget")
        self.setpointWidget.setMinimumSize(QSize(2000, 50))
        self.setpointWidget.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayoutWidget_3 = QWidget(self.setpointWidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(0, 0, 1121, 71))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.setpointLayout = QVBoxLayout()
        self.setpointLayout.setSpacing(0)
        self.setpointLayout.setObjectName(u"setpointLayout")
        self.setpointLayout.setContentsMargins(20, -1, 20, -1)
        self.setpointSlider = QSlider(self.horizontalLayoutWidget_3)
        self.setpointSlider.setObjectName(u"setpointSlider")
        self.setpointSlider.setMinimumSize(QSize(1000, 0))
        self.setpointSlider.setMaximumSize(QSize(16777215, 16777215))
        self.setpointSlider.setStyleSheet(u"")
        self.setpointSlider.setMinimum(-100)
        self.setpointSlider.setMaximum(100)
        self.setpointSlider.setTracking(True)
        self.setpointSlider.setOrientation(Qt.Orientation.Horizontal)
        self.setpointSlider.setInvertedAppearance(False)
        self.setpointSlider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.setpointSlider.setTickInterval(10)

        self.setpointLayout.addWidget(self.setpointSlider, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.setpointLabel = QLabel(self.horizontalLayoutWidget_3)
        self.setpointLabel.setObjectName(u"setpointLabel")
        self.setpointLabel.setMaximumSize(QSize(920, 25))
        font2 = QFont()
        font2.setFamilies([u"Noto Sans SC"])
        font2.setPointSize(12)
        self.setpointLabel.setFont(font2)
        self.setpointLabel.setScaledContents(False)
        self.setpointLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setpointLayout.addWidget(self.setpointLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout.addLayout(self.setpointLayout)

        self.setpointTolerance = QDoubleSpinBox(self.horizontalLayoutWidget_3)
        self.setpointTolerance.setObjectName(u"setpointTolerance")
        self.setpointTolerance.setEnabled(True)
        self.setpointTolerance.setMinimumSize(QSize(15, 50))
        self.setpointTolerance.setMaximumSize(QSize(16777215, 16777215))
        self.setpointTolerance.setStyleSheet(u"font: 12pt \"Noto Sans SC\";")
        self.setpointTolerance.setWrapping(False)
        self.setpointTolerance.setFrame(False)
        self.setpointTolerance.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.setpointTolerance.setReadOnly(False)
        self.setpointTolerance.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.setpointTolerance.setAccelerated(True)
        self.setpointTolerance.setCorrectionMode(QAbstractSpinBox.CorrectionMode.CorrectToNearestValue)
        self.setpointTolerance.setDecimals(1)
        self.setpointTolerance.setMaximum(1.000000000000000)
        self.setpointTolerance.setSingleStep(0.100000000000000)

        self.horizontalLayout.addWidget(self.setpointTolerance, 0, Qt.AlignmentFlag.AlignTop)


        self.mainLayout.addWidget(self.setpointWidget)

        self.graphsWidget = QWidget(self.verticalLayoutWidget)
        self.graphsWidget.setObjectName(u"graphsWidget")
        self.graphsWidget.setMinimumSize(QSize(0, 450))
        self.graphsWidget.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayoutWidget_2 = QWidget(self.graphsWidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(-1, -1, 1121, 361))
        self.graphicsLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.graphicsLayout.setObjectName(u"graphicsLayout")
        self.graphicsLayout.setContentsMargins(20, 0, 20, 0)
        self.heatingGraph = PlotWidget(self.horizontalLayoutWidget_2)
        self.heatingGraph.setObjectName(u"heatingGraph")
        self.heatingGraph.setStyleSheet(u"")

        self.graphicsLayout.addWidget(self.heatingGraph)

        self.stirringGraph = PlotWidget(self.horizontalLayoutWidget_2)
        self.stirringGraph.setObjectName(u"stirringGraph")
        self.stirringGraph.setStyleSheet(u"")

        self.graphicsLayout.addWidget(self.stirringGraph)

        self.phGraph = PlotWidget(self.horizontalLayoutWidget_2)
        self.phGraph.setObjectName(u"phGraph")
        self.phGraph.setStyleSheet(u"")

        self.graphicsLayout.addWidget(self.phGraph)


        self.mainLayout.addWidget(self.graphsWidget)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1120, 23))
        font3 = QFont()
        font3.setFamilies([u"Noto Sans SC"])
        self.menuBar.setFont(font3)
        self.menuBar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.menuBar.setNativeMenuBar(True)
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setStyleSheet(u"")
        self.menuEdit = QMenu(self.menuBar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionChange_Connection)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionReset_To_Default)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Bioreactor Control Panel", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionFullscreen.setText(QCoreApplication.translate("MainWindow", u"Display Anomalies", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_File_As.setText(QCoreApplication.translate("MainWindow", u"Save File As", None))
        self.actionSaveAs.setText(QCoreApplication.translate("MainWindow", u"Save As...", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionReset_To_Default.setText(QCoreApplication.translate("MainWindow", u"Reset To Defaults", None))
        self.actionChange_Connection.setText(QCoreApplication.translate("MainWindow", u"Change Connection", None))
        self.heatingButton.setText(QCoreApplication.translate("MainWindow", u"Heating", None))
        self.stirringButton.setText(QCoreApplication.translate("MainWindow", u"Stirring", None))
        self.phButton.setText(QCoreApplication.translate("MainWindow", u"Acidity", None))
        self.setpointLabel.setText(QCoreApplication.translate("MainWindow", u"0\u2103", None))
        self.setpointTolerance.setPrefix(QCoreApplication.translate("MainWindow", u"\u00b1", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

