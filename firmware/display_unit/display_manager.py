from lcd096 import LCD_0inch96

class DisplayManager:
    COLORS = {
        'RED': 0x00F8,
        'GREEN': 0xE007,
        'BLUE': 0x1F00,
        'WHITE': 0xFFFF,
        'BLACK': 0x0000,
        'YELLOW': 0x00FF
    }
    
    def __init__(self):
        self.lcd = LCD_0inch96()
        self.lcd.fill(self.COLORS['BLACK'])
        self.lcd.display()
        
    def show_menu(self, menu_items):
        self.lcd.fill(self.COLORS['BLACK'])
        for i, item in enumerate(menu_items):
            self.lcd.text(item, 5, 15 + i*10, self.COLORS['GREEN'])
        self.lcd.display()
        
    def show_reading(self, weight, length=None):
        self.lcd.fill(self.COLORS['BLACK'])
        if length is not None:
            self.lcd.text(f"Length: {length:.2f}m", 5, 20, self.COLORS['GREEN'])
        self.lcd.text(f"Weight: {weight:.2f}g", 5, 40, self.COLORS['GREEN'])
        self.lcd.display()
        
    def show_calibration(self, step, message):
        self.lcd.fill(self.COLORS['BLACK'])
        self.lcd.text(f"Calibration Step {step}", 5, 20, self.COLORS['YELLOW'])
        self.lcd.text(message, 5, 40, self.COLORS['WHITE'])
        self.lcd.display()
