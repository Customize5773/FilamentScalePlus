
# Build Instructions

## Mechanical Assembly
1. **Base Construction**
   ```python
   # Recommended materials (choose one):
   materials = ["3mm Laser-cut Acrylic", "5mm Bamboo Plywood", "3D Printed PETG"]
   ```

2. **Vibration Damping Installation**
   - Install Sorbothane feet at 4 corners
   - Ensure 2mm gap between scale and printer surface
   - Apply damping ratio: 30-40 durometer

3. **Filament Path Optimization**
   ```python
   # PTFE liner specifications:
   length = 15  # cm
   inner_diameter = 2.1  # mm (for 1.75mm filament)
   installation_angle = 45°  # Entry/exit angle
   ```

## Electronic Connections
| Component | Pico Pin | Wire Color |
|-----------|----------|------------|
| HX711 DT | GP0 | Yellow |
| HX711 SCK | GP1 | Green |
| LCD SCK | GP10 | Blue |
| LCD MOSI | GP11 | Purple |
| LCD CS | GP9 | Gray |
| Button A | GP18 | Red |
| Button D | GP21 | Black |

## Firmware Flashing
1. Install [MicroPython 1.22](https://micropython.org/download/RPI_PICO/)
2. Deploy code:
   ```bash
   # Linux/macOS
   mpremote cp firmware/ :/
   
   # Windows (Thonny IDE)
   # Right-click -> Upload to /
   ```
