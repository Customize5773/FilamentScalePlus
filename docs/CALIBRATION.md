# Calibration Procedure

## Hardware Preparation
1. Ensure scale is on a stable surface with vibration dampers installed
2. Remove all weight from the platform
3. Connect via USB to monitor serial output (optional)

## Auto-Calibration Sequence
```python
# Run from calibration_tool/calibrate.py
def calibration_procedure():
    # Step 1: Initialize
    display.show_calibration(1, "Remove all weight")
    time.sleep(5)  # 5-second stabilization period
    
    # Step 2: Tare
    display.show_calibration(2, "Measuring zero point...")
    tare_value = load_cell.set_tare(samples=50)  # High sample count
    
    # Step 3: Add known weight
    display.show_calibration(3, "Add 100g weight now")
    time.sleep(10)  # Wait for user
    
    # Step 4: Calculate new factor
    raw_value = load_cell.hx.mean(100)  # 100 samples for accuracy
    new_factor = (raw_value - tare_value) / 100.0
    
    # Step 5: Save and verify
    load_cell.calibration_factor = new_factor
    load_cell.save_calibration()
```

## Manual Calibration
1. Power on while holding Button C
2. LCD will show current calibration factor
3. Adjust using:
   - Button A: Decrease factor (increase sensitivity)
   - Button B: Increase factor (decrease sensitivity)
   - Button D: Save and exit

## Calibration Schedule
| Condition | Recalibration Frequency |
|-----------|-------------------------|
| Normal use | Every 3 months |
| After mechanical impact | Immediately |
| Temperature change >10°C | When stabilized |
| Accuracy drift >1% | Immediately |
