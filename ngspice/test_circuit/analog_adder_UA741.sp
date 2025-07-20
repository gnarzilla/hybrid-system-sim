* Analog Adder Circuit Using Realistic Op-Amp (uA741)
* Summing amplifier: Vout = -(V1 * (R_f / R1) + V2 * (R_f / R2))

* Input voltages
V1 in1 0 DC 2  ; Voltage source V1 (2V)
V2 in2 0 DC 3  ; Voltage source V2 (3V)

* Resistor values
R1 in1 1 10k   ; Resistor R1 (10k ohms)
R2 in2 2 10k   ; Resistor R2 (10k ohms)
Rf 1 2 10k     ; Feedback resistor Rf (10k ohms)

* Op-Amp Power Supply Connections
Vcc vcc 0 DC 15   ; Positive power supply (15V)
Vee vee 0 DC -15  ; Negative power supply (-15V)

* Using uA741 Op-Amp Model
X1 2 0 out vcc vee uA741

* Built-in uA741 model (or add if not available)
.model uA741 opamp(gain=200000 GBW=1.5Meg slewrate=0.5mF)

* Analysis
.control
tran 1ms 20ms
print v(out)
plot v(out)
.endc

.end

