# Smart Jacket for Industrial Workers

## Project Overview
The Smart Jacket for Industrial Workers is a wearable safety system designed to monitor hazardous environmental and physical conditions in real time. It detects toxic gases, abnormal temperature and humidity, high noise levels, and accidental falls, and alerts the worker immediately while sending live data to a cloud dashboard.

---

## Objectives
- Monitor worker safety parameters continuously  
- Detect toxic gases using MQ-135  
- Measure temperature and humidity using DHT22  
- Identify dangerous noise levels using KY-038  
- Detect falls and sudden movements using MPU6050  
- Provide instant alerts using a buzzer  
- Enable remote monitoring through Blynk IoT  

---

## Hardware Components
- Raspberry Pi Pico W  
- MQ-135 Gas Sensor  
- DHT22 Temperature & Humidity Sensor  
- KY-038 Sound Sensor  
- MPU6050 Accelerometer & Gyroscope  
- Buzzer  
- 5V Rechargeable Battery  

---

## Pin Configuration

### DHT22
| Signal | Pico Pin |
|------|----------|
| DATA | GP15 |
| VCC  | 3.3V |
| GND  | GND |

### MQ-135
| Signal | Pico Pin |
|------|----------|
| AOUT | GP28 (ADC2) |
| VCC  | 3.3V |
| GND  | GND |

### KY-038
| Signal | Pico Pin |
|------|----------|
| DO   | GP27 |
| VCC  | 3.3V |
| GND  | GND |

### MPU6050 (I2C)
| Signal | Pico Pin |
|------|----------|
| SDA  | GP2 |
| SCL  | GP3 |
| VCC  | 3.3V |
| GND  | GND |

### Buzzer
| Signal | Pico Pin |
|------|----------|
| +    | GP16 |
| −    | GND |

---

## Software Requirements
- MicroPython (Raspberry Pi Pico W)
- Thonny IDE
- Blynk IoT Platform
- Libraries Used:
  - `network`
  - `urequests`
  - `machine`
  - `dht`
  - `mpu6050`

---

## Working Principle
The Raspberry Pi Pico W continuously reads data from all connected sensors. If any parameter exceeds predefined safety thresholds, the buzzer is activated to alert the worker. At the same time, all sensor values are uploaded to the Blynk cloud platform via Wi-Fi for real-time remote monitoring.

---

## Blynk Virtual Pins
| Virtual Pin | Parameter |
|------------|----------|
| V0 | Temperature |
| V1 | Humidity |
| V2 | Gas Level |
| V3 | Sound Detection |
| V4 | Acceleration (Fall Detection) |

---

## Output
- Instant audible alert during unsafe conditions  
- Live monitoring through Blynk dashboard  
- Reliable detection of gas leaks, heat stress, noise hazards, and falls  

---

## Applications
- Industrial worker safety systems  
- Factories and chemical plants  
- Construction sites  
- Mining industries  
- Smart Personal Protective Equipment (PPE)  

---

## Conclusion
The Smart Jacket for Industrial Workers is a low-cost, portable, and effective safety solution. It enhances workplace safety by combining real-time sensing, immediate alerts, and cloud-based monitoring.
