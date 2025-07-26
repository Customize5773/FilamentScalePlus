# Enclosure System - Improved Durability

## Base Plate Specifications
```python
# OpenSCAD Parametric Design (base.scad)
module base_plate(
  thickness = 3,          // mm
  material = "PETG",      // Recommended material
  infill = 40,            // %
  edge_radius = 5,        // mm
  damping_cavities = 4,   // Number of damper slots
  cable_routing = true
) {
  // Core dimensions
  width = 160;            // mm (matches LCD width)
  depth = 100;            // mm
  height = thickness;
  
  // Generate model
  difference() {
    // Main plate
    rounded_cube(width, depth, height, edge_radius);
    
    // Vibration damper cavities
    for(i=[0:3]) {
      translate([20+i*40, 20, -1]) 
        cylinder(d=12.5, h=thickness+2);
    }
    
    // Cable routing channels
    if(cable_routing) {
      translate([width-15, depth/2, -1])
        cube([20, 10, thickness+2]);
    }
  }
}
```

## Printing Guidelines
| Parameter | Value | Notes |
|-----------|-------|-------|
| Material | PETG/ASA | UV and impact resistant |
| Layer Height | 0.2mm | Balance of strength and print time |
| Walls | 4 | Minimum for structural integrity |
| Infill Pattern | Gyroid | Best vibration damping |
| Orientation | Flat side down | Critical for dimensional accuracy |
| Post-Processing | Acetone vapor (ASA) | Surface sealing |

## Material Comparison
| Material | Impact Strength | UV Resistance | Cost/m |
|----------|-----------------|---------------|--------|
| PLA | Low | Poor | $ |
| PETG | Medium | Good | $$ |
| ASA | High | Excellent | $$$ |
| Polycarbonate | Very High | Excellent | $$$$ |
