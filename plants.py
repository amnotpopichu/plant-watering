from datetime import UTC
from AtlasI2C import AtlasI2C

pump = AtlasI2C()
import time
pump.set_i2c_address(103)
#2 pump
cal = 50/43.8
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
ads = ADS.ADS1115(i2c)
soil_sensor = AnalogIn(ads, ADS.P0)
#soil_sensor.value
value = soil_sensor.value
#Wet soil value = 13866
#Water value = 8290, 8197, 8205
#Bone-dry soil value = 17964, 17922, 17907


#must add logs.txt in home directory

while True:
    if  value >= 15000:
        pump.write("D,114")
        print(value)
        f = open("logs.txt", "a")
        f.write("Plants watered at " + str(UTC) + " with soil moisture at " + str(value))
        f.close()
        time.sleep(300)        
        f.write("checking in on plants after watering, currnet soil is at " + str(value))
        time.sleep(300)
    else:
        time.sleep(300)