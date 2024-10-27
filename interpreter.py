from registers import Registers
import operations
import error_correction

class Interpreter:
    def __init__(self):
        self.registers = Registers()
        self.analog_values = []  # To track analog changes for plotting

    def execute(self, command):
        parts = command.split()
        if not parts:
            return

        op = parts[0].upper()
        args = parts[1:]

        if op == "AND":
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

    def run_program(self, program):
        for line in program:
            self.execute(line.strip())

        # After running the program, plot analog values
        if self.analog_values:
            operations.plot_signal(self.analog_values)

