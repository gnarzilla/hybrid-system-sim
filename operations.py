# operations.py

import matplotlib.pyplot as plt

def plot_signal(signal_values):
    plt.plot(signal_values)
    plt.xlabel("Time")
    plt.ylabel("Signal Strength")
    plt.title("Analog Signal Over Time")
    plt.savefig("analog_signal_plot.png")  # Save the plot as a PNG file
    print("Plot saved as 'analog_signal_plot.png'")

def plot_dynamic_signal(signal_values):
    plt.ion() # Turn on interactive mode
    fig, ax = plt.subplots()
    line, = ax.plot(signal_values)
    ax.set_xlabel("Time")
    ax.set_ylabel("Signal Strength")
    ax.set_title("Dynamic Analog Signal Over Time")

    # Display each point dynamically
    for i in range(len(signal_values)):
        line.set_ydata(signal_values[:i+1]) # Update data
        line.set_xdata(range(i+1))
        fig.canvas.draw()
        fig.canvas.flush_events()

    # After dynamic plotting, save the static image
    plt.savefig("analog_signal_plot.png")
    plt.ioff() # Turn off interactive mode
    print("Plot saved as 'analog_signal_plot.png'")

def set_circuit(component, name, value):
    if component.upper() == "RESISTOR":
        return f"R{name} 1 0 {value}\n"
    elif component.upper() == "CAPACITOR":
        return f"C{name} 1 0 {value}\n" # Capacitor across nodes 1 and 2
    elif component.upper() == "VOLTAGE_SOURCE":
        return f"V{name} 1 0 DC {value}\n"
    else:
        return f"* Unknown component: {component}\n" # Comment line in .spice file

def add_simulation_directive():
    # Add a basic transient analysis directive
    return ".tran 0.1 10\n.end\n"

def and_operation(reg1, reg2):
    return reg1 & reg2

def nand_operation(reg1, reg2):
    return ~(reg1 & reg2)

def or_operation(reg1, reg2):
    return reg1 | reg2

def xor_operation(reg1, reg2):
    return reg1 ^ reg2

def not_operation(reg):
    return ~reg

def phase_shift(signal, degrees):
    # Placeholder, would adjust the waveform phase by `degrees`
    # In a real system, we'd apply some waveform transformation.
    return signal  # For now, return unchanged

def frequency_modulate(signal, multiplier):
    # Placeholder, would change the frequency of the analog signal
    return signal * multiplier

def amplify(signal, factor):
    return signal * factor

def attenuate(signal, factor):
    return signal * factor

def range_check(signal, min_val, max_val):
    return min_val <= signal <= max_val

# Conversion functions
def a2d(signal):
    # Simple binary conversion (e.g., thresholded binary, could refine)
    return int(signal > 0.5)

def d2c(value):
    # Convert a digital value to a continuous analog-like signal
    return float(value)

