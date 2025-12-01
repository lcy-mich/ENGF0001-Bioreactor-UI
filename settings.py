from enum import Enum

MQTT_HOST = "engf0001.cs.ucl.ac.uk"
MQTT_PORT = 1883
MQTT_TOPIC = "bioreactor_sim/nofaults/telemetry/summary"
MQTT_KEEPALIVE = 60

USE_OPENGL = True
USE_NUMBA = True

UNDO_BUFFER_SIZE = 50
REDO_BUFFER_SIZE = 50

SAVE_FILE_SHORTCUT = "Ctrl+S"
UNDO_SHORTCUT = "Ctrl+Z"
REDO_SHORTCUT = "Ctrl+Y"

ACTION_SAVE_STATUS_TIP = "Save the bioreactor data into a JSON file"

class Stat(Enum):

    Acidity = "Acidity"
    
    Temperature = "Temperature"
    
    Stirring = "Stirring"

Info = {
    Stat.Acidity : {
        "Unit": "pH" ,
        "Range" : {
            "Low" : 3, 
            "High" : 7
            }, 
        "DecimalPlaces" : 1,
        "Default" : 7
        },

    Stat.Temperature : {
        "Unit": "℃" ,
        "Range" : {
            "Low" : 25, 
            "High" : 35
            }, 
        "DecimalPlaces" : 1,
        "Default" : 35
        },
    
    Stat.Stirring : {
        "Unit": "RPM" ,
        "Range" : {
            "Low" : 500, 
            "High" : 1500
            }, 
        "DecimalPlaces" : 0,
        "Default" : 800
        }
    }