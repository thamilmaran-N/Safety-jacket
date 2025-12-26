# mpu6050.py – MicroPython library for MPU6050

from machine import I2C
import struct
import time

MPU6050_ADDR = 0x68

# Registers
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B
TEMP_OUT_H = 0x41
GYRO_XOUT_H = 0x43

class MPU6050:
    def __init__(self, i2c: I2C, addr=MPU6050_ADDR):
        self.i2c = i2c
        self.addr = addr
        # Wake up the MPU6050
        self.i2c.writeto_mem(self.addr, PWR_MGMT_1, b'\x00')
        time.sleep_ms(100)

    def _read_i16(self, reg):
        data = self.i2c.readfrom_mem(self.addr, reg, 2)
        return struct.unpack('>h', data)[0]

    def get_accel_data(self):
        ax = self._read_i16(ACCEL_XOUT_H) / 16384.0
        ay = self._read_i16(ACCEL_XOUT_H + 2) / 16384.0
        az = self._read_i16(ACCEL_XOUT_H + 4) / 16384.0
        return {'x': ax, 'y': ay, 'z': az}

    def get_gyro_data(self):
        gx = self._read_i16(GYRO_XOUT_H) / 131.0
        gy = self._read_i16(GYRO_XOUT_H + 2) / 131.0
        gz = self._read_i16(GYRO_XOUT_H + 4) / 131.0
        return {'x': gx, 'y': gy, 'z': gz}

    def get_temp(self):
        temp_raw = self._read_i16(TEMP_OUT_H)
        return (temp_raw / 340.0) + 36.53
