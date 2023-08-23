import RPi.GPIO as GPIO
import time

# Konfigurasi pin GPIO
TRIGGER_PIN = 20
ECHO_PIN = 21

# Inisialisasi GPIO
def init_ultrasonic():
    GPIO.setup(TRIGGER_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)

def measure_distance():
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)
    
    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    
    return distance
    
def calculate_stock(distance):
    max_distance = 24  # Maksimal jarak yang diukur adalah 24 cm
    stock_per_unit = 1 / 3  # Satu barang setiap 3 cm
    
    # Batasi jarak maksimal yang diukur
    limited_distance = min(distance, max_distance)
    
    stock = limited_distance * stock_per_unit
    return max(0, int(stock))


if __name__ == "__main__":
    try:
        while True:
            init_ultrasonic()
            distance = measure_distance()
            stock = calculate_stock(distance)
            print(f"Jarak: {distance} cm, Stok: {stock}")
            time.sleep(1)  # Interval pembacaan
            
    except KeyboardInterrupt:
        GPIO.cleanup()
