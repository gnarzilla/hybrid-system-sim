* Analog Adder Circuit Using Realistic Op-Amp (with Power Supply Limits)
* Summing amplifier: Vout = -(V1 * (R_f / R1) + V2 * (R_f / R2))

* Define a Realistic Op-Amp Subcircuit
.subckt my_opamp in+ in- out vcc vee
E1 out 0 in+ in- 1e6
R1 out 0 10k
Vlim1 out_lim_high out vcc 10k
Vlim2 out_lim_low out vee 10k
.ends my_opamp

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

* Using the Realistic Op-Amp Subcircuit
X1 2 0 out vcc vee my_opamp

* Small resistors to stabilize circuit
Rsmall1 out vcc 1Meg  ; 1 MΩ resistor to stabilize clamping behavior
Rsmall2 vee out 1Meg  ; 1 MΩ resistor to stabilize clamping behavior

* Analysis
.control
tran 1ms 20ms
print v(out)
plot v(out)
.endc

.end

