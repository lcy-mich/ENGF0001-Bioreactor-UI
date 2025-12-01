from enum import Enum

USE_OPENGL = True
USE_NUMBA = True

UNDO_BUFFER_SIZE = 50
REDO_BUFFER_SIZE = 50

SAVE_FILE_SHORTCUT = "Ctrl+S"
UNDO_SHORTCUT = "Ctrl+Z"
REDO_SHORTCUT = "Ctrl+Y"

class Stat(Enum):

    Acidity = {
        "Unit": "pH" ,
        "Range" : {
            "Low" : 3, 
            "High" : 7
            }, 
        "DecimalPlaces" : 1,
        "Default" : 7
        }
    
    Temperature = {
        "Unit": "℃" ,
        "Range" : {
            "Low" : 25, 
            "High" : 35
            }, 
        "DecimalPlaces" : 1,
        "Default" : 35
        }
    
    Stirring = {
        "Unit": "RPM" ,
        "Range" : {
            "Low" : 500, 
            "High" : 1500
            }, 
        "DecimalPlaces" : 0,
        "Default" : 800
        }