from display_manager import DisplayManager
from load_cell import LoadCell
from calibration_manager import CalibrationManager
import time

def calibration_procedure():
    display = DisplayManager()
    cal_manager = CalibrationManager()
    
    # Step 1: Remove weight
    display.show_calibration(1, "Remove all weight")
    time.sleep(5)
    
    # Initialize load cell
    load_cell = LoadCell(Pin(0), Pin(1), cal_manager.calibration_data["factor"])
    
    # Step 2: Tare
    display.show_calibration(2, "Taring...")
    load_cell.set_tare()
    cal_manager.calibration_data["tare_offset"] = load_cell.tare_value
    cal_manager.save_calibration()
    
    # Step 3: Calibrate with known weight
    display.show_calibration(3, "Add known weight")
    KNOWN_WEIGHT = 100.0  # 100g calibration weight
    time.sleep(5)
    
    new_factor = cal_manager.auto_calibrate(load_cell, KNOWN_WEIGHT)
    display.show_calibration(4, f"New factor: {new_factor:.2f}")
    time.sleep(3)
    
    return new_factor
