# interpreters.py

from registers import Registers
import operations
import error_correction
import gpio_control

class Interpreter:
    def __init__(self):
        self.registers = Registers()
        self.analog_values = []  # To track analog changes for plotting
        self.circuit_commands = [] # Store lines for .spice files

    def execute(self, command):
        parts = command.strip().split()
        if not parts:
            return

        op = parts[0].upper()
        args = parts[1:]

        # Handle 'A2D' specifically
        if op == "A2D":
            print(f"Arguments for A2D: {args}") # Debugging
            if len(args) != 2:
                raise ValueError("A2D command expects exactly two arguments: <analog_reg> <digital_reg>")
            analog_reg, digital_reg = args
            analog_value = self.registers.get_analog(analog_reg)
            digital_value = operations.a2d(analog_value)
            self.registers.set_digital(digital_reg, digital_value)
            print(f"A2D Conversion {analog_reg} -> {digital_reg}: {analog_value} -> {digital_value}")

        # Read GPIO pin
        if  op == "READ_GPIO_PIN":
            pin = int(args[0])
            value = gpio_control.read_gpio_pin(pin)
            self.analog_values.append(value)
            print(f"Read GPIO pin {pin}: {value}")

        elif op == "WRITE_GPIO_PIN":
            pin, state = int(args[0]), args[1]
            gpio_control.set_gpio_pin(pin, state)
            print(f"Set GPIO pin {pin} to {state}")

        elif op == "READ_ANALOG":
            reg = args[0]
            # Simulate reading an analog value (in real scenarios, read from a sensor)
            analog_value = self.registers.get_analog(reg)
            print(f"READ_ANALOG {reg}: {analog_value}")

        elif op == "CHECK_VOLTAGE":
            reg, expected = args[0], float(args[1])
            current = self.registers.get_analog(reg)
            if current < expected:
                print(f"Voltage check failed: {current} < {expected}")
            else:
                print(f"Voltage check passed: {current} >= {expected}")

        elif op == "AND":
            reg1, reg2 = args
            result = operations.and_operation(self.registers.get_digital(reg1), self.registers.get_digital(reg2))
            self.registers.set_digital(reg1, result)
        
        elif op == "AMPLIFY":
            reg, factor = args[0], float(args[1])
            result = operations.amplify(self.registers.get_analog(reg), factor)
            self.registers.set_analog(reg, result)
            self.analog_values.append(result)  # Track changes

        elif op == "A2D":
            analog_reg, digital_reg = args
            analog_value = self.registers.get_analog(analog_reg)
            digital_value = operations.a2d(analog_value)
            self.registers.set_digital(digital_reg, digital_value)
       
        elif op == "OR":
            reg1, reg2 = args
            result = operations.or_operation(self.registers.get_digital(reg1), self.registers.get_digital(reg2))
            self.registers.set_digital(reg1, result)

        elif op == "NOT":
            reg = args[0]
            result = operations.not_operation(self.registers.get_digital(reg))
            self.registers.set_digital(reg, result)

        elif op == "FREQUENCY_MODULATE":
            analog_reg, multiplier = args[0], float(args[1])
            result = operations.frequency_modulate(self.registers.get_analog(analog_reg), multiplier)
            self.registers.set_analog(analog_reg, result)
            self.analog_values.append(result)  # Track changes

        elif op == "SET_CIRCUIT":
            component, name, value, = args[0], args[1], args[2]
            circuit_line = operations.set_circuit(component, name, value)
            self.circuit_commands.append(circuit_line)

    def run_program(self, program):
        for line in program:
            # Remove any inline comments starting with '#'
            line = line.split('#')[0].strip()
            if line: # Only process non-empty lines
                self.execute(line)

        # After running the program, plot analog values
        if self.analog_values:
            operations.plot_dynamic_signal(self.analog_values)

        # Generate .spice file if circuit commands are present
        if self.circuit_commands:
            self.circuit_commands.append(operations.add_simulation_directive())
            with open("generated_circuit.spice", "w") as f:
                f.writelines(self.circuit_commands)
            print("Generated circuit file: generated_circuit.spice")
        else:
            print("No circuit commands found. .spice file not generated.")
