from gpiozero import LED, MotionSensor, LightSensor
from gpiozero.tools import booleanized, all_values
from signal import pause
from time import sleep
import time

luz1 = LightSensor(23)
luz2 = LightSensor(24)
i=0
inicio=0.0
fin=0.0

sensor1=""
sensor2=""

while True:
  if luz1.value != 0.0 :
    sensor1 ='Se interrumpio S1'
    inicio = time.time()
    print(sensor1)
  if luz2.value != 0.0 :
    sensor2 ='Se interrumpio S2'
    fin = time.time()
    print(sensor2)
  i= i+1
  print("Contador de bucle {}".format(i)) 
  sleep(0.01)

print("Tiempo de interactividad: {}".format(fin-inicio))
