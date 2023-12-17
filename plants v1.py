from datetime import datetime
now=datetime.now()
dt=now.strftime("%d/%m/%Y %H:%M:%S")
print(dt)
startdate=datetime.now()

import board
from AtlasI2C import AtlasI2C
import time
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from time import *
import csv




light_address = 0x29
bme_address = 0x77
soil_address = 0x48
co2_address = 0x62
lcd_address = 0x27
i2c = board.I2C()
i2c_port = 1
pump_address = 0x63
ads = ADS.ADS1115(i2c)
ads = ADS.ADS1115(i2c)

pump = AtlasI2C()
pump.set_i2c_address(103)
#2 pump
cal = 50/43.8

ads = ADS.ADS1115(i2c)
soil_sensor = AnalogIn(ads, ADS.P0)
#soil_sensor.value
value = soil_sensor.value
print(value)


#Wet soil value = 13866
#Water value = 8290, 8197, 8205
#Bone-dry soil value = 17964, 17922, 17907

#must add logs.txt in home directory

while True:
    if  value >= 14500:
        currentdate=datetime.now()
        td=currentdate-startdate
        mtd=round(td.total_seconds()/60)

        with open('logs.csv', 'w') as f:
                        writer = csv.writer(f)
                        writer.writerow([mtd,value])
        pump.write("D,57")
        print(value)
        f = open("logs.txt", "a")
        f.write("Plants watered at " + dt + " with soil moisture at " + str(value))
        
        f.close()
        sleep(300)        
        f.write("checking in on 5m plants after watering, currnet soil is at " + str(value))
        currentdate=datetime.now()
        td=currentdate-startdate
        mtd=round(td.total_seconds()/60)

        with open('logs.csv', 'w') as f:
                        writer = csv.writer(f)
                        writer.writerow([mtd,value])
    else:
        sleep(300)
        f = open("logs.txt", "a")
        f.write("Plants unwatered at " + dt + " with soil moisture at " + str(value))
        currentdate=datetime.now()
        td=currentdate-startdate
        mtd=round(td.total_seconds()/60)

        with open('logs.csv', 'w') as f:
                        writer = csv.writer(f)
                        writer.writerow([mtd,value])

