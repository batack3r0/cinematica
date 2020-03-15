from gpiozero import LED, MotionSensor, LightSensor
from gpiozero.tools import booleanized, all_values
from signal import pause
from time import sleep

#garden = LED(16)
#motion = MotionSensor(4)

luz1 = LightSensor(23)
luz2 = LightSensor(24)
i=0

sensor1=""
sensor2=""


while i<100:
  if luz1.value == 0.0 :
    sensor1='Sin interrumpir S1'
  else:
    sensor1 ='Se interrumpio S1'
  print(sensor1)
  if luz2.value == 0.0 :
    sensor2='Sin interrumpir S2'
  else:
    sensor2 ='Se interrumpio S2'
  print(sensor2)
  i= i+1
  print("Contador de bucle {}".format(i)) 
  sleep(1)

