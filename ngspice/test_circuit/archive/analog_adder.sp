* Analog Adder Circuit Using Op-Amp
* Summing amplifier: Vout = -(V1 * (R_f / R1) + V2 * (R_f / R2))

* Input voltages
V1 in1 0 DC 2  ; Voltage source V1 (2V)
V2 in2 0 DC 3  ; Voltage source V2 (3V)

* Resistor values
R1 in1 1 10k   ; Resistor R1 (10k ohms)
R2 in2 2 10k   ; Resistor R2 (10k ohms)
Rf 1 2 10k     ; Feedback resistor Rf (10k ohms)

* Operational Amplifier
X1 2 0 out opamp

* Op-amp model (can use 'uA741' if available in your library)
* Otherwise, use the ideal op-amp subcircuit below
.model opamp opamp

* Analysis
.control
tran 1ms 20ms
print v(out)
plot v(out)
.endc

.end

