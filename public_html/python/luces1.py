from gpiozero import LED, MotionSensor, LightSensor
from gpiozero.tools import booleanized, all_values
from signal import pause
from time import sleep

#garden = LED(16)
#motion = MotionSensor(4)

luz1 = LightSensor(23)
i1=0
sensor1=""
while i1<100:
  if luz1.value == 0.0 :
    sensor1='Sin interrumpir S1'   
  else:
    sensor1 ='Se interrumpio S1' 
  print(sensor1)

  print("Contando: {}".format(i1))
  i1= i1+1
  sleep(1)


luz2 = LightSensor(24)
i2=0
sensor2=""
while i2<100:
  if luz2.value == 0.0 :
    sensor2='Sin interrumpir S2'   
  else:
    sensor2 ='Se interrumpio S2' 
  print(sensor2)

  print("Contando: {}".format(i2))
  i2= i2+1
  sleep(1)

#garden.source = all_values(booleanized(light, 0, 0.1), motion)
#pause()
