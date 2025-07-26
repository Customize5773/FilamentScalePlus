import json
from machine import Pin

class CalibrationManager:
    def __init__(self):
        self.calibration_data = {}
        self.load_calibration()
        
    def load_calibration(self, filename="cal_data.json"):
        try:
            with open(filename, 'r') as f:
                self.calibration_data = json.load(f)
            return True
        except:
            # Default calibration values
            self.calibration_data = {
                "factor": 405,
                "last_calibrated": "2025-01-01",
                "tare_offset": 0
            }
            return False
            
    def save_calibration(self, filename="cal_data.json"):
        with open(filename, 'w') as f:
            json.dump(self.calibration_data, f)
            
    def auto_calibrate(self, load_cell, known_weight):
        new_factor = load_cell.calibrate(known_weight)
        self.calibration_data["factor"] = new_factor
        self.calibration_data["last_calibrated"] = "2025-07-26"  # Update with actual date
        self.save_calibration()
        return new_factor

    def vibration_compensation(self, raw_value):
        # Simple low-pass filter for vibration damping
        if "prev_value" not in self.calibration_data:
            self.calibration_data["prev_value"] = raw_value
            
        smoothed = 0.7 * self.calibration_data["prev_value"] + 0.3 * raw_value
        self.calibration_data["prev_value"] = smoothed
        return smoothed
