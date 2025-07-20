# gpio_control.py (new module)
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

def set_gpio_pin(pin, state):
    GPIO.output(pin, GPIO.HIGH if state == "HIGH" else GPIO.LOW)
    print(f"Pin {pin} set to {state}")

def read_gpio_pin(pin):
    GPIO.setup(pin, GPIO.IN)
    return GPIO.input(pin)

