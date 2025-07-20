# registers.py

class Registers:
    def __init__(self):
        # Separate dictionaries for analog and digital registers
        self.analog_registers = {}
        self.digital_registers = {}

    def set_analog(self, name, value):
        self.analog_registers[name] = value

    def get_analog(self, name):
        return self.analog_registers.get(name, 0.0)

    def set_digital(self, name, value):
        self.digital_registers[name] = int(value)

    def get_digital(self, name):
        return self.digital_registers.get(name, 0)

