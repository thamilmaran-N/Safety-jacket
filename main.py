import network
import urequests
import machine
import time
import dht
from mpu6050 import MPU6050
from machine import I2C, Pin, ADC

# Wi-Fi and Blynk Setup
SSID = 'get password from thamilmaran'
PASSWORD = 'easypassword'
BLYNK_AUTH = 'XvrcJAZjJeF8ZFxKrJzQtnIRxstpVkma'
BLYNK_URL = "http://blynk.cloud/external/api/update"

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        print("Connecting to WiFi...")
        time.sleep(1)
    print("Connected:", wlan.ifconfig())

# Sensor Pins
dht_sensor = dht.DHT22(Pin(15))
mq135 = ADC(Pin(28))
sound_sensor = Pin(27, Pin.IN)
buzzer = Pin(16, Pin.OUT)

# I2C for MPU6050
i2c = I2C(1, scl=Pin(3), sda=Pin(2))
mpu = MPU6050(i2c)

# Alert Function
def trigger_alert():
    print("ALERT: Unsafe condition detected!")
    for _ in range(3):
        buzzer.toggle()
        time.sleep(0.3)
    buzzer.value(0)

# Send to Blynk
def send_to_blynk(vpin, value):
    try:
        url = f"{BLYNK_URL}?token={BLYNK_AUTH}&{vpin}={value}"
        response = urequests.get(url)
        response.close()
        print(f"Sent to Blynk: {vpin} = {value}")
    except Exception as e:
        print("Blynk Send Error:", e)

# Main Loop
def main():
    connect_wifi()
    while True:
        try:
            dht_sensor.measure()
            temperature = dht_sensor.temperature()
            humidity = dht_sensor.humidity()
            gas_level = mq135.read_u16()
            accel = mpu.get_accel_data()
            temp_mpu = mpu.get_temp()

            ax = accel['x']
            sound_detected = sound_sensor.value()

            print("==============================")
            print("Temp (DHT22): {:.2f} °C".format(temperature))
            print("Humidity: {:.2f} %".format(humidity))
            print("Gas Level:", gas_level)
            print("Sound Detected:", sound_detected)
            print("Accel X:", ax)
            print("Temp (MPU6050): {:.2f} °C".format(temp_mpu))

            if temperature > 40 or gas_level > 40000 or sound_detected == 1 or abs(ax) > 1.7:
                trigger_alert()

            send_to_blynk('V0', temperature)
            send_to_blynk('V1', humidity)
            send_to_blynk('V2', gas_level)
            send_to_blynk('V3', sound_detected)
            send_to_blynk('V4', ax)

            time.sleep(2)

        except Exception as e:
            print("Error:", e)
            time.sleep(2)

main()
