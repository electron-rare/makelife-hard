# Design Blocks Catalog

Reusable KiCad design blocks extracted from 15 production projects.

## Summary

| Category     | Count | Description                              |
|-------------|-------|------------------------------------------|
| Power       | 3     | LDO regulators, bipolar supply, battery charger |
| MCU         | 2     | ESP32-S3 and ESP32-WROOM base circuits   |
| Sensing     | 3     | Current sensor, I/O expander, I2C bus    |
| Protection  | 2     | MOSFET switch, reverse polarity protection |
| Audio       | 4     | Preamp, EQ, I2S codec, audio-to-LED      |
| LED         | 3     | Shift register driver, level shifter, DALI |
| Motor       | 2     | Stepper driver, DMX input                |
| Connectors  | 3     | IDC bus, bornier 24V, RJ45 daisy chain   |
| **Total**   | **22**|                                          |

## Power

| Block ID | Name | File Path | Source Project | Interface Labels | Key Constraints |
|----------|------|-----------|----------------|------------------|-----------------|
| PWR-001  | LDO 3.3V + 5V Dual Regulator | `blocks/power/ldo-3v3-5v.kicad_sch` | KXKM BMU v2 | VIN, 3V3, 5V, GND | 24-30V input, AMS1117-3.3 + AMS1117-5.0, 800mA max each, thermal pad required |
| PWR-002  | Bipolar +/-15V Supply | `blocks/power/supply-bipolar-15v.kicad_sch` | KXKM Audio Mixer | VIN, V_POS, V_NEG, GND | Generates +15V/-15V for op-amp stages, requires heatsink at >200mA |
| PWR-003  | Battery Charger | `blocks/power/battery-charger.kicad_sch` | KXKM Batterie Parallelator | VUSB, VBATT, GND, CHG_STATUS | USB input, LiPo/Li-Ion single cell, charge status LED output |

## MCU

| Block ID | Name | File Path | Source Project | Interface Labels | Key Constraints |
|----------|------|-----------|----------------|------------------|-----------------|
| MCU-001  | ESP32-S3 Minimal Module | `blocks/mcu/esp32-s3-minimal.kicad_sch` | KXKM BMU v2 | 3V3, GND, SDA, SCL, TX, RX, USB_DP, USB_DN | ESP32-S3-WROOM-1, 16MB flash, 8MB PSRAM, USB-C, boot/reset buttons |
| MCU-002  | ESP32-WROOM Module | `blocks/mcu/esp32-wroom.kicad_sch` | KXKM LED Controller | 3V3, GND, SDA, SCL, TX, RX, EN, IO0 | ESP32-WROOM-32, auto-reset via DTR/RTS, decoupling 10uF+100nF |

## Sensing

| Block ID | Name | File Path | Source Project | Interface Labels | Key Constraints |
|----------|------|-----------|----------------|------------------|-----------------|
| SNS-001  | INA237 Current/Voltage Sensor | `blocks/sensing/ina237-current.kicad_sch` | KXKM BMU v2 | SENSE_IN, SENSE_OUT, SDA, SCL, ALERT, VDD, GND | TSSOP-10, 10mR shunt 1%, I2C addr via A0/A1, decoupling 100nF |
| SNS-002  | TCA9535 I/O Expander | `blocks/sensing/tca9535-expander.kicad_sch` | KXKM BMU v2 | SDA, SCL, INT, VDD, GND, P0_0-P0_3, P1_0-P1_3 | 16-bit I2C I/O expander, 3 address bits, interrupt output, 25mA per pin |
| SNS-003  | I2C Bus (Pull-ups + Decoupling) | `blocks/sensing/i2c-bus.kicad_sch` | KXKM BMU v2 | SDA, SCL, VDD, GND | 4.7k pull-ups for 400kHz, 100nF decoupling, max 400pF bus capacitance |

## Protection

| Block ID | Name | File Path | Source Project | Interface Labels | Key Constraints |
|----------|------|-----------|----------------|------------------|-----------------|
| PRT-001  | MOSFET High-Side Switch | `blocks/protection/mosfet-switch.kicad_sch` | KXKM BMU v2 | GATE_CTRL, DRAIN_IN, SOURCE_OUT, GND | P-channel MOSFET, Rds(on) <10mOhm, gate charge <20nC, 10A max |
| PRT-002  | Reverse Polarity Protection | `blocks/protection/reverse-protection.kicad_sch` | KXKM Batterie Parallelator | VIN, VOUT, GND | P-MOSFET body diode protection, <50mV drop at rated current |

## Audio

| Block ID | Name | File Path | Source Project | Interface Labels | Key Constraints |
|----------|------|-----------|----------------|------------------|-----------------|
| AUD-001  | Mic/Line Preamplifier | `blocks/audio/preamp-mic-line.kicad_sch` | KXKM Audio Mixer | INPUT_P, INPUT_N, OUTPUT_P, OUTPUT_N, V_POS, V_NEG, GND | Differential input, +20dB to +60dB gain, requires bipolar supply |
| AUD-002  | 3-Band Parametric EQ | `blocks/audio/eq-3band.kicad_sch` | KXKM Audio Mixer | IN_P, IN_N, OUT_P, OUT_N, V_POS, V_NEG, GND | Low/Mid/High bands, +/-12dB boost/cut, requires bipolar supply |
| AUD-003  | Audio Codec I2S (WM8960) | `blocks/audio/audio-codec-i2s.kicad_sch` | KXKM Audio Processor | MCLK, BCLK, LRCLK, DIN, DOUT, SDA, SCL, HP_L, HP_R, VDD, GND | I2S + I2C control, headphone output, 16/24-bit, 8-48kHz sample rate |
| AUD-004  | Audio-to-LED Reactive | `blocks/audio/audio-to-led.kicad_sch` | KXKM LED Bar | AUDIO_IN, LED_PWM, VDD, GND | Envelope follower + comparator, PWM output for LED brightness |

## LED

| Block ID | Name | File Path | Source Project | Interface Labels | Key Constraints |
|----------|------|-----------|----------------|------------------|-----------------|
| LED-001  | LED Driver Shift Register (74HC595) | `blocks/led/led-driver-shift.kicad_sch` | KXKM LED Controller | SER_IN, SRCLK, RCLK, OE, SER_OUT, VDD, GND | 8-bit shift register, cascade via SER_OUT, max 20mA per output |
| LED-002  | Level Shifter (3.3V to 5V) | `blocks/led/level-shifter.kicad_sch` | KXKM LED Controller | A1, A2, B1, B2, VDD_A, VDD_B, GND | BSS138 bidirectional, 2 channels, supports I2C and SPI signals |
| LED-003  | DALI Interface | `blocks/led/dali-interface.kicad_sch` | KXKM Lighting | DALI_P, DALI_N, TX, RX, VDD, GND | DALI bus transceiver, optocoupler isolation, 16V bus |

## Motor

| Block ID | Name | File Path | Source Project | Interface Labels | Key Constraints |
|----------|------|-----------|----------------|------------------|-----------------|
| MTR-001  | Stepper Motor Driver | `blocks/motor/stepper-driver.kicad_sch` | KXKM Stage Mechanics | STEP, DIR, ENABLE, VDD, GND | A4988/DRV8825 compatible, microstepping, flyback diodes included |
| MTR-002  | DMX-512 Input | `blocks/motor/dmx-input.kicad_sch` | KXKM DMX Controller | DMX_RX, DMX_TX, VDD, GND | RS-485 transceiver (MAX485), 120R termination, ESD protection |

## Connectors

| Block ID | Name | File Path | Source Project | Interface Labels | Key Constraints |
|----------|------|-----------|----------------|------------------|-----------------|
| CON-001  | IDC Bus Connector | `blocks/connectors/idc-bus.kicad_sch` | KXKM BMU v2 | SDA, SCL, VCC, GND, ALERT | 10-pin IDC, I2C + alert bus, keyed connector |
| CON-002  | Bornier 24V Power Input | `blocks/connectors/bornier-24v.kicad_sch` | KXKM BMU v2 | VIN, GND | 2-pin screw terminal, 24V/10A rated, 2.54mm pitch |
| CON-003  | RJ45 Daisy Chain | `blocks/connectors/rj45-daisy.kicad_sch` | KXKM LED Controller | DATA_IN, DATA_OUT, VDD, GND | Dual RJ45 for daisy-chain topology, data + power passthrough |
