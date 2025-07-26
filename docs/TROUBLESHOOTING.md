# Troubleshooting Guide

## Common Issues
### Symptom: Weight Drift
```python
# Solution: Apply software filter
def vibration_compensation(raw):
    # In calibration_manager.py
    return 0.7 * prev_value + 0.3 * raw
```

### Symptom: HX711 Not Detected
1. Check wiring:
   - Verify 5V power to HX711
   - Test continuity between Pico GP0/GP1 and HX711
2. Run diagnostic:
   ```python
   from scale_unit.hx711f import HX711
   hx = HX711(Pin(0), Pin(1), 405)  # Should print channel info
   ```

### Symptom: LCD Artifacts
1. Apply hardware fix:
   - Add 100Ω resistor on MOSI line
   - Shorten SPI cables < 15cm
2. Software adjustment:
   ```python
   # In lcd096.py
   self.spi = SPI(1, 8_000_000)  # Reduce from 10MHz
   ```

## Error Codes
| LCD Message | Meaning | Solution |
|-------------|---------|----------|
| ERR: DRIFT | >5% deviation | Recalibrate |
| ERR: NO CELL | HX711 timeout | Check wiring |
| ERR: OVER | >5kg detected | Remove weight |
