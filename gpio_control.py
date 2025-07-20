try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
except ImportError:
    print("RPi.GPIO not available. Running without GPIO control.")

def set_gpio_pin(pin, state):
    # Only execute if GPIO is imported
    if 'GPIO' in globals():
        GPIO.output(pin, GPIO.HIGH if state == "HIGH" else GPIO.LOW)
        print(f"Pin {pin} set to {state}")
    else:
        print(f"Simulated setting Pin {pin} to {state}")

def read_gpio_pin(pin):
    if 'GPIO' in globals():
        GPIO.setup(pin, GPIO.IN)
        return GPIO.input(pin)
    else:
        print(f"Simulated reading Pin {pin}")
        return 0  # Simulate a LOW value

