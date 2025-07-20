# run_simulation.py

from interpreter import Interpreter

# Load a sample program
with open("test_programs/sample_program.txt", "r") as f:
    program = f.readlines()

# Initialize interpreter and run program
interpreter = Interpreter()
interpreter.run_program(program)

