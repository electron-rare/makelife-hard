# Design Rules

Guidelines and constraints for reusable design blocks.

## Power

- **Trace width**: max 2A per trace at 0.5mm width, 4A at 1mm width. Use copper pours for higher currents.
- **Decoupling**: 100nF ceramic (X7R, 0402 or 0603) + 10uF bulk (tantalum or ceramic) per IC power pin.
- **Capacitor placement**: place decoupling caps within 5mm of VDD pin, on the same layer as the IC. Route directly to IC pad, not through via.
- **Input protection**: add TVS diode (SMAJ series) on power input for transient suppression.
- **Thermal pads**: LDO thermal pads must connect to ground plane with multiple vias (minimum 4x 0.3mm).
- **Dropout**: ensure input voltage exceeds output by at least 1.5V for AMS1117 series at full load.
- **Input capacitance**: minimum 10uF ceramic on regulator input for stability, placed within 3mm.
- **Output capacitance**: minimum 22uF on regulator output. ESR must match datasheet stability requirements.

## I2C

- **Pull-up resistors**: 4.7k for 400kHz (Fast Mode), 10k for 100kHz (Standard Mode). Use 2.2k for Fast Mode Plus (1MHz).
- **Bus capacitance**: maximum 400pF total bus capacitance. Each device adds 5-15pF. Budget carefully when daisy-chaining.
- **Trace length**: keep I2C traces under 30cm total. For longer runs, use I2C bus extender (P82B715).
- **Address allocation**: INA237 uses A0/A1 for 4 addresses (0x40-0x43). TCA9535 uses A0/A1/A2 for 8 addresses (0x20-0x27). Verify no conflicts before assembly.
- **Level shifting**: required when mixing 3.3V and 5V I2C devices. Use BSS138-based bidirectional shifter.
- **Shielding**: route SDA and SCL as a pair with GND guard traces on both sides for noise immunity.

## Battery

- **MOSFET selection**: Rds(on) must be <10mOhm for currents under 10A. Use parallel MOSFETs for >10A.
- **Gate charge**: select MOSFETs with gate charge <20nC for fast switching. Higher Qg increases switching losses.
- **Protection delay**: default 10 second delay before disconnect on overcurrent. Configurable via TCA9535 GPIO.
- **Topology**: each INA237 monitors one battery channel. TCA9535 controls 4 MOSFET switches. Total: 4x INA237 + 1x TCA9535 = 4 independent channels.
- **Sense resistor**: 10mOhm 1% tolerance, 1W rated. Kelvin connection (4-wire) mandatory for accurate measurement.
- **Current calibration**: INA237 shunt calibration register must be set for 10mOhm shunt. LSB = 1.25mA default.
- **Thermal monitoring**: place NTC thermistor within 5mm of each MOSFET for over-temperature protection.

## Audio

- **Ground planes**: separate analog and digital ground planes. Join at a single point near the power supply input.
- **Differential routing**: route audio signals as differential pairs. Maintain constant impedance (100 Ohm differential).
- **Isolation**: keep audio traces at least 5mm away from digital/power traces. Use ground guard traces.
- **Decoupling**: use 100nF + 10uF on analog VDD. Add 100pF caps on op-amp feedback networks for HF stability.
- **Signal path**: preamp -> EQ -> codec is the canonical signal chain. Each block has differential I/O for noise rejection.
- **Bipolar supply**: audio op-amps require +/-15V from the bipolar supply block. Do not substitute single-supply.
- **I2S routing**: keep MCLK, BCLK, LRCLK traces matched in length (within 2mm). Add 33R series resistors for impedance matching.
- **Headphone output**: WM8960 codec drives 16 Ohm headphones directly. Add 10uF DC blocking caps on HP_L/HP_R.

## LED

- **Current limiting**: R = (VDD - Vf) / If. For red LEDs: Vf=2.0V, If=20mA, R=150R at 5V. For white: Vf=3.2V, R=90R at 5V.
- **Thermal limits**: maximum 20mA per 74HC595 output pin. Total package dissipation 500mW. Use constant-current LED drivers (TLC5940, PCA9685) for loads exceeding 100mA per channel.
- **Shift register cascade**: connect SER_OUT of one 74HC595 to SER_IN of the next. Share SRCLK and RCLK. Total chain limited to 8 devices (64 outputs) for timing margin.
- **Level shifting**: 3.3V MCU to 5V LED logic requires BSS138-based level shifter. Place within 10mm of MCU outputs.
- **PWM frequency**: minimum 1kHz to avoid visible flicker. 10kHz recommended for video-compatible applications.
- **Data line termination**: for WS2812B addressable LEDs, add 330R series resistor on data line. Keep first LED within 15cm of MCU.
- **DALI bus**: 16V bus, max 250mA. Optocoupler isolation between MCU UART and DALI bus is mandatory.

## Motor

- **Optocoupler isolation**: mandatory for stepper driver control signals (STEP, DIR, ENABLE). Use PC817 or equivalent. Provides galvanic isolation between logic and motor power domains.
- **Flyback diodes**: required on all inductive loads (motors, solenoids, relays). Use fast-recovery diodes (1N4148 for <100mA, SS34 for <3A). Place directly at the load terminals.
- **Fuse protection**: fuse on motor power input is mandatory. Size at 150% of maximum expected current. Use resettable PTC fuse (polyfuse) for convenience.
- **EMI filtering**: add 100nF ceramic cap across motor terminals. For brush motors, add LC filter (10uH + 100nF) on power input.
- **Microstepping**: A4988 supports up to 1/16 microstepping. MS1/MS2/MS3 set via pull-up/pull-down. DRV8825 supports 1/32.
- **DMX-512**: RS-485 with 250kbaud. 120R termination at end of line only. Max 32 devices per segment. ESD protection (TVS diodes) on A/B lines.
- **Current sense**: set motor current via VREF pin. VREF = 8 * Imax * Rsense. For A4988 with 0.1R sense resistor: VREF = 0.8 * Imax.
