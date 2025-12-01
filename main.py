from sys import exit as sysexit

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import Slot
import pyqtgraph as qtgraph

from collections import deque

from BioMainWindow import Ui_MainWindow as BioMainWindow

from settings import *
from json import dumps

class InvalidStatName(Exception):
    pass

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        qtgraph.setConfigOptions(
            background = (234, 237, 245), 
            foreground = (110,110,150),
            # leftButtonPan = False,
            useOpenGL = USE_OPENGL,
            useNumba = USE_NUMBA,
        )

        self.ui = BioMainWindow()
        self.ui.setupUi(self)

        self.setpoints = {
            "Temperature" : self.convertForSlider(Stat.Temperature), 
            "Acidity" : self.convertForSlider(Stat.Acidity), 
            "Stirring" : self.convertForSlider(Stat.Stirring)
            }

        self.datapoints = {
            "Temperature" : [],
            "Acidity" : [],
            "Stirring" : []
        }

        self.undobuffer = deque(maxlen=UNDO_BUFFER_SIZE)
        self.redobuffer = deque(maxlen=REDO_BUFFER_SIZE)

        self.ui.setpointSlider.valueChanged.connect(self.sliderValueChange)


        for name, plot in [("Acidity (pH)", self.ui.phGraph), ("Temperature (℃)", self.ui.heatingGraph), ("Stirring (RPM)", self.ui.stirringGraph)]:
            plotitem : qtgraph.PlotItem = plot.getPlotItem() # type: ignore
            y_axis = plotitem.getAxis("left")
            y_axis.setLabel(name)

            plotitem.getAxis("bottom").setLabel("Time (seconds)")


        self.ui.phButton.toggled.connect(self.phButtonToggled)
        self.ui.heatingButton.toggled.connect(self.tempButtonToggled)
        self.ui.stirringButton.toggled.connect(self.stirButtonToggled)

        self.ui.actionQuit.triggered.connect(QApplication.quit)

        self.ui.actionSave.setShortcut(SAVE_FILE_SHORTCUT)
        self.ui.actionSave.setStatusTip("Save the bioreactor data into a JSON file")
        self.ui.actionSave.triggered.connect(self.save_file)

        self.ui.actionUndo.setShortcut(UNDO_SHORTCUT)
        self.ui.actionUndo.triggered.connect(self.undo_move)

        self.ui.actionRedo.setShortcut(REDO_SHORTCUT)
        self.ui.actionRedo.triggered.connect(self.redo_move)

        self.ui.phButton.toggle()

    ### -- file saving shit --

    @Slot()
    def undo_move(self):
        action = self.undobuffer.pop()
        if action:
            action = self.undobuffer.pop() #incredibly jank solution to issue
        self.redobuffer.append((self.currentStat, self.ui.setpointSlider.value()))
        if not action: return
        print(action)
        if action[0] == self.currentStat:
            print("hell yeah")
            self.ui.setpointSlider.setValue(action[1])
        else:
            self.setpoints[action[0].name] = action[1]
        print(self.setpoints)
    
    @Slot()
    def redo_move(self):
        action = self.redobuffer.pop()
        if not action: return
        self.undobuffer.append((self.currentStat, self.ui.setpointSlider.value()))

        if action[0] == self.currentStat:
            self.ui.setpointSlider.setValue(action[1])
        else:
            self.setpoints[action[0].name] = action[1]

        
    @Slot()
    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "JSON Files (*.json)")
        if file_name:
            with open(file_name, 'w') as file:
                file.write(dumps(self.datapoints))
        

    ### -- slider shit --

    def convertForSlider(self, stat, value = None):
        if not value:
            value = stat.value["Default"]
        decimalplaces = stat.value["DecimalPlaces"]
        return value * (10**decimalplaces)

    def convertFromSlider(self, stat = None, value = None):
        if not stat:
            stat = self.currentStat
        if not value:
            value = self.setpoints[stat.name]
        decimalplaces = stat.value["DecimalPlaces"]
        if decimalplaces > 0:
            return self.ui.setpointSlider.value() / (10**decimalplaces)
        else:
            return self.ui.setpointSlider.value()

    def changeSliderInfo(self, setpoint, range_low, range_high):
        self.ui.setpointSlider.setRange(range_low, range_high)
        self.ui.setpointSlider.setValue(setpoint)
        self.ui.setpointSlider.setTickInterval(((range_high-range_low)/10))
        
    def changeCurrentStat(self, stat : Stat):
        self.currentStat = stat
        self.changeSliderInfo(
            self.setpoints[stat.name], 
            self.convertForSlider(self.currentStat, self.currentStat.value["Range"]["Low"]), 
            self.convertForSlider(self.currentStat, self.currentStat.value["Range"]["High"])
            )

    @Slot(float)
    def sliderValueChange(self, value):
        if value > self.convertForSlider(self.currentStat, self.currentStat.value["Range"]["High"]):
            self.ui.setpointSlider.setValue(self.convertForSlider(self.currentStat, self.currentStat.value["Range"]["High"]))
        elif value < self.convertForSlider(self.currentStat, self.currentStat.value["Range"]["Low"]):
            self.ui.setpointSlider.setValue(self.convertForSlider(self.currentStat, self.currentStat.value["Range"]["Low"]))
        self.undobuffer.append((self.currentStat, self.ui.setpointSlider.value()))
        self.ui.setpointLabel.setText(f"{self.convertFromSlider():.{self.currentStat.value["DecimalPlaces"]}f} {self.currentStat.value["Unit"]}")

    @Slot(bool)
    def phButtonToggled(self, checked : bool):
        if not checked: return
        self.changeCurrentStat(Stat.Acidity)
    @Slot(bool)
    def tempButtonToggled(self, checked : bool):
        if not checked: return
        self.changeCurrentStat(Stat.Temperature)
    @Slot(bool)
    def stirButtonToggled(self, checked : bool):
        if not checked: return
        self.changeCurrentStat(Stat.Stirring)



    


if __name__ == "__main__":
    app = QApplication()

    main = MainWindow()
    main.show()

    sysexit(app.exec())
    
    