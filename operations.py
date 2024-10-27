import matplotlib.pyplot as plt

def plot_signal(signal_values):
    plt.plot(signal_values)
    plt.xlabel("Time")
    plt.ylabel("Signal Strength")
    plt.title("Analog Signal Over Time")
    plt.savefig("analog_signal_plot.png")  # Save the plot as a PNG file
    print("Plot saved as 'analog_signal_plot.png'")

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

