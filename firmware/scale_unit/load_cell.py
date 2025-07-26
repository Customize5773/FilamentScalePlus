from hx711f import HX711
import time

class LoadCell:
    def __init__(self, dout_pin, pd_sck_pin, calibration_factor=405):
        self.dout = dout_pin
        self.pd_sck = pd_sck_pin
        self.calibration_factor = calibration_factor
        self.tare_value = 0
        self.init_sensor()
        
    def init_sensor(self):
        try:
            self.hx = HX711(self.dout, self.pd_sck, self.calibration_factor)
            self.hx.wakeUp()
            self.hx.kanal(1)
            return True
        except:
            return False
    
    def calibrate(self, known_weight, samples=25):
        raw_value = self.hx.mean(samples)
        self.calibration_factor = (raw_value - self.tare_value) / known_weight
        self.hx.calFaktor(self.calibration_factor)
        return self.calibration_factor
        
    def set_tare(self, samples=25):
        self.tare_value = self.hx.tara(samples)
        return self.tare_value
        
    def get_weight(self, samples=10):
        raw_value = self.hx.mean(samples)
        return (raw_value - self.tare_value) / self.calibration_factor
        
    def save_calibration(self, filename="cal_factor.txt"):
        with open(filename, 'w') as f:
            f.write(str(self.calibration_factor))
