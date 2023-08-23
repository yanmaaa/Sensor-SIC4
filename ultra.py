import RPi.GPIO as GPIO
import time
import requests


# Konfigurasi pin GPIO
TRIGGER_PIN = 20
ECHO_PIN = 21
TRIGGER_PIN2 = 19
ECHO_PIN2 = 26
TRIGGER_PIN3 = 6
ECHO_PIN3 = 13
TRIGGER_PIN4 = 24
ECHO_PIN4 = 23
TRIGGER_PIN5 = 3
ECHO_PIN5 = 4
TRIGGER_PIN6 = 17
ECHO_PIN6 = 27

# Inisialisasi GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(TRIGGER_PIN2, GPIO.OUT)
GPIO.setup(ECHO_PIN2, GPIO.IN)
GPIO.setup(TRIGGER_PIN3, GPIO.OUT)
GPIO.setup(ECHO_PIN3, GPIO.IN)
GPIO.setup(TRIGGER_PIN4, GPIO.OUT)
GPIO.setup(ECHO_PIN4, GPIO.IN)
GPIO.setup(TRIGGER_PIN5, GPIO.OUT)
GPIO.setup(ECHO_PIN5, GPIO.IN)
GPIO.setup(TRIGGER_PIN6, GPIO.OUT)
GPIO.setup(ECHO_PIN6, GPIO.IN)

def inven1():
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)
    
    pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Kecepatan suara adalah 343 meter/detik
    distance = round(distance, 2)
    
    return distance

def inven2():
    GPIO.output(TRIGGER_PIN2, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(TRIGGER_PIN2, GPIO.LOW)
    
    pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN2) == GPIO.LOW:
        pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN2) == GPIO.HIGH:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Kecepatan suara adalah 343 meter/detik
    distance = round(distance, 2)
    
    return distance

def inven3():
    GPIO.output(TRIGGER_PIN3, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(TRIGGER_PIN3, GPIO.LOW)
    
    pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN3) == GPIO.LOW:
        pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN3) == GPIO.HIGH:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Kecepatan suara adalah 343 meter/detik
    distance = round(distance, 2)
    
    return distance

def inven4():
    GPIO.output(TRIGGER_PIN4, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(TRIGGER_PIN4, GPIO.LOW)
    
    pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN4) == GPIO.LOW:
        pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN4) == GPIO.HIGH:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Kecepatan suara adalah 343 meter/detik
    distance = round(distance, 2)
    
    return distance

def inven5():
    GPIO.output(TRIGGER_PIN5, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(TRIGGER_PIN5, GPIO.LOW)
    
    pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN5) == GPIO.LOW:
        pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN5) == GPIO.HIGH:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Kecepatan suara adalah 343 meter/detik
    distance = round(distance, 2)
    
    return distance

def inven6():
    GPIO.output(TRIGGER_PIN6, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(TRIGGER_PIN6, GPIO.LOW)

    pulse_start = time.time()
    # pulse_end = pulse_start  # Inisialisasi pulse_end di sini

    while GPIO.input(ECHO_PIN6) == GPIO.LOW:
        pulse_start = time.time()

    while GPIO.input(ECHO_PIN6) == GPIO.HIGH:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Kecepatan suara adalah 343 meter/detik
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
            distance1 = inven1()
            stock1 = calculate_stock(distance1)
            distance2 = inven2()
            stock2 = calculate_stock(distance2)
            distance3 = inven3()
            stock3 = calculate_stock(distance3)
            distance4 = inven3()
            stock4 = calculate_stock(distance4)
            distance5 = inven5()
            stock5 = calculate_stock(distance5)
            distance6 = inven6()
            stock6 = calculate_stock(distance6)
            
            print(f"Ultra 1 - Jarak: {distance1} cm, Stok: {stock1}")
            print(f"Ultra 2 - Jarak: {distance2} cm, Stok: {stock2}")
            print(f"Ultra 3 - Jarak: {distance3} cm, Stok: {stock3}")
            print(f"Ultra 4 - Jarak: {distance4} cm, Stok: {stock4}")
            print(f"Ultra 5 - Jarak: {distance5} cm, Stok: {stock5}")
            print(f"Ultra 6 - Jarak: {distance6} cm, Stok: {stock6}")
                    
            time.sleep(3)  # Interval pembacaan
            
    except KeyboardInterrupt:
        GPIO.cleanup()
