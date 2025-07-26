import os
import time
import json
from machine import Pin
from display_manager import DisplayManager
from load_cell import LoadCell
from calibration_manager import CalibrationManager

# Initialize components
display = DisplayManager()
cal_manager = CalibrationManager()
load_cell = LoadCell(Pin(0), Pin(1), cal_manager.calibration_data["factor"])

# Button setup
BUTTONS = {
    'A': Pin(18, Pin.IN, Pin.PULL_DOWN),
    'B': Pin(19, Pin.IN, Pin.PULL_DOWN),
    'C': Pin(20, Pin.IN, Pin.PULL_DOWN),
    'D': Pin(21, Pin.IN, Pin.PULL_DOWN)
}

# Filament data
FILAMENT_DATA = {
    'types': load_filament_types(),
    'diameters': load_diameters(),
    'spools': load_spools()
}

def load_filament_types(filename="ftypes.txt"):
    # Implementation from original code
    ...

def vibration_compensated_reading():
    raw = load_cell.hx.getRaw()
    return cal_manager.vibration_compensation(raw)

def main():
    current_mode = "FILAMENT"  # or "STANDARD"
    
    while True:
        if BUTTONS['D'].value() == 1:  # Calibration trigger
            from calibration_tool.calibrate import calibration_procedure
            calibration_procedure()
            
        if current_mode == "FILAMENT":
            handle_filament_mode()
        else:
            handle_standard_mode()

def handle_filament_mode():
    # Improved filament mode with vibration compensation
    compensated_weight = vibration_compensated_reading()
    net_weight = compensated_weight - current_spool_weight
    
    # Calculate length (original formula)
    volume = net_weight / current_density
    length = volume / ((current_diameter/2)**2 * 3.1415926535)
    
    display.show_reading(net_weight, length)
    time.sleep(0.5)

def handle_standard_mode():
    compensated_weight = vibration_compensated_reading()
    display.show_reading(compensated_weight)
    time.sleep(0.5)

if __name__ == "__main__":
    # Initial taring during startup
    display.show_message("Initializing...")
    load_cell.set_tare()
    display.show_message("Remove weight")
    time.sleep(10)  # Improved 10s countdown
    main()
