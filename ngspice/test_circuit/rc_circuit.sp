* RC Circuit Example
R1 1 2 1k  ; Resistor of 1k ohms between nodes 1 and 2
C1 2 0 1u  ; Capacitor of 1 microfarad between node 2 and ground (node 0)
V1 1 0 DC 5 ; DC voltage source of 5V between node 1 and ground

.tran 1ms 100ms  ; Perform a transient analysis, step 1ms, total 100ms
.plot tran v(2)  ; Plot the voltage at node 2 over time
.end

