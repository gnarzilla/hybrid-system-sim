* Analog Adder Circuit Using Op-Amp (with improved convergence handling)
* Summing amplifier: Vout = -(V1 * (R_f / R1) + V2 * (R_f / R2))

* Define the Ideal Op-Amp Model
.subckt opamp in+ in- out
Eout out 0 in+ in- 1e6
Rout out 0 10k
.ends opamp

* Input voltages
V1 in1 0 DC 2  ; Voltage source V1 (2V)
V2 in2 0 DC 3  ; Voltage source V2 (3V)

* Resistor values
R1 in1 1 10k   ; Resistor R1 (10k ohms)
R2 in2 2 10k   ; Resistor R2 (10k ohms)
Rf 1 2 10k     ; Feedback resistor Rf (10k ohms)

* Op-Amp Power Supply Connections (limits)
Vcc vcc 0 DC 15   ; Positive power supply (15V)
Vee vee 0 DC -15  ; Negative power supply (-15V)

* Operational Amplifier with External Power Connections
X1 2 0 out opamp

* Small resistors to aid convergence
Rsmall1 out vcc 1Meg  ; 1 MΩ resistor to stabilize clamping behavior
Rsmall2 vee out 1Meg  ; 1 MΩ resistor to stabilize clamping behavior

* Clamping diodes for limiting output to power supply range
Dupper out vcc DCLAMP  ; Diode to limit to Vcc (15V)
Dlower vee out DCLAMP  ; Diode to limit to Vee (-15V)

* Diode model for clamping
.model DCLAMP D(IS=1e-14 N=1)

* Analysis
.control
tran 1ms 20ms
print v(out)
plot v(out)
.endc

.end

