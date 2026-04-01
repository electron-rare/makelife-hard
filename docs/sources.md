# Source Traceability

Maps each design block back to its origin project, datasheet, and validation status.

## Traceability Matrix

| Block ID | Block Name | Source Project | Source Path | Datasheet Ref | Schematic Rev | PCB Validated | Notes |
|----------|-----------|----------------|-------------|---------------|---------------|---------------|-------|
| PWR-001  | LDO 3.3V + 5V | KXKM BMU v2 | `hardware/bmu/power.kicad_sch` | AMS1117-3.3/5.0 | 2.1 | Yes | Dual regulator, 24-30V input, thermal pad verified |
| PWR-002  | Bipolar +/-15V Supply | KXKM Audio Mixer | `hardware/mixer/supply.kicad_sch` | LM337/LM317 | 1.3 | Yes | Generates +/-15V for op-amp stages |
| PWR-003  | Battery Charger | KXKM Batterie Parallelator | `hardware/charger/charger.kicad_sch` | MCP73831 | 1.0 | No | USB LiPo charger, single cell |
| MCU-001  | ESP32-S3 Minimal | KXKM BMU v2 | `hardware/bmu/mcu.kicad_sch` | ESP32-S3-WROOM-1 | 2.1 | Yes | 16MB flash, 8MB PSRAM, USB-C |
| MCU-002  | ESP32-WROOM | KXKM LED Controller | `hardware/led-ctrl/mcu.kicad_sch` | ESP32-WROOM-32E | 1.4 | Yes | WiFi+BT, auto-reset circuit |
| SNS-001  | INA237 Current Sensor | KXKM BMU v2 | `hardware/bmu/sensing.kicad_sch` | INA237 (TI) | 2.1 | Yes | TSSOP-10, 10mR shunt, I2C |
| SNS-002  | TCA9535 I/O Expander | KXKM BMU v2 | `hardware/bmu/expander.kicad_sch` | TCA9535 (TI) | 2.1 | Yes | 16-bit I2C GPIO, interrupt output |
| SNS-003  | I2C Bus | KXKM BMU v2 | `hardware/bmu/i2c.kicad_sch` | N/A (passive) | 2.1 | Yes | 4.7k pull-ups, decoupling |
| PRT-001  | MOSFET Switch | KXKM BMU v2 | `hardware/bmu/protection.kicad_sch` | IRLML6402 | 2.1 | Yes | P-ch MOSFET, Rds(on) 65mOhm |
| PRT-002  | Reverse Protection | KXKM Batterie Parallelator | `hardware/charger/protection.kicad_sch` | DMG2305UX | 1.0 | No | P-MOSFET reverse polarity |
| AUD-001  | Preamp Mic/Line | KXKM Audio Mixer | `hardware/mixer/preamp.kicad_sch` | NE5532 | 1.3 | Yes | Differential, +20/+60dB gain |
| AUD-002  | 3-Band EQ | KXKM Audio Mixer | `hardware/mixer/eq.kicad_sch` | NE5532 | 1.3 | Yes | Parametric 3-band, +/-12dB |
| AUD-003  | Audio Codec I2S | KXKM Audio Processor | `hardware/audio-proc/codec.kicad_sch` | WM8960 (Cirrus) | 1.1 | Yes | I2S + I2C, headphone out |
| AUD-004  | Audio-to-LED | KXKM LED Bar | `hardware/led-bar/audio-led.kicad_sch` | LM358 | 1.2 | Yes | Envelope follower, PWM out |
| LED-001  | LED Driver Shift Register | KXKM LED Controller | `hardware/led-ctrl/driver.kicad_sch` | 74HC595 | 1.4 | Yes | 8-bit, cascade, 20mA/output |
| LED-002  | Level Shifter | KXKM LED Controller | `hardware/led-ctrl/shifter.kicad_sch` | BSS138 | 1.4 | Yes | Bidirectional, 2-channel |
| LED-003  | DALI Interface | KXKM Lighting | `hardware/lighting/dali.kicad_sch` | SN65176B | 1.0 | No | Optocoupler isolated DALI bus |
| MTR-001  | Stepper Driver | KXKM Stage Mechanics | `hardware/stage/stepper.kicad_sch` | A4988 (Allegro) | 1.2 | Yes | 1/16 microstepping, flyback diodes |
| MTR-002  | DMX-512 Input | KXKM DMX Controller | `hardware/dmx/input.kicad_sch` | MAX485 (Maxim) | 1.1 | Yes | RS-485, 120R termination, ESD |
| CON-001  | IDC Bus Connector | KXKM BMU v2 | `hardware/bmu/connectors.kicad_sch` | N/A (mechanical) | 2.1 | Yes | 10-pin IDC, keyed |
| CON-002  | Bornier 24V | KXKM BMU v2 | `hardware/bmu/connectors.kicad_sch` | N/A (mechanical) | 2.1 | Yes | 2-pin screw terminal, 10A |
| CON-003  | RJ45 Daisy Chain | KXKM LED Controller | `hardware/led-ctrl/connectors.kicad_sch` | N/A (mechanical) | 1.4 | Yes | Dual RJ45, data+power |

## Validation Legend

- **PCB Validated: Yes** -- block has been fabricated and tested on a production PCB
- **PCB Validated: No** -- block is schematic-only, pending fabrication or extracted from untested design
- **Schematic Rev** -- revision of the source project schematic at time of extraction
