from gpiozero import LED, MotionSensor, LightSensor
from gpiozero.tools import booleanized, all_values
from signal import pause
from time import sleep
import time


luz1 = LightSensor(23)
luz2 = LightSensor(24)
i=0

sensor1=""
sensor2=""

inicio = time.time()

while i<50:
  if luz1.value == 0.0 :
    sensor1='___'
  else:
    sensor1 ='Se interrumpio S1'
  print(sensor1)
  if luz2.value == 0.0 :
    sensor2='___'
  else:
    sensor2 ='Se interrumpio S2'
  print(sensor2)
  i= i+1
  print("Contador de bucle {}".format(i)) 
  sleep(0.05)

fin = time.time()

print("Tiempo de interactividad: {}".format(fin-inicio))
