import time
import requests
import json
import double_digits
from sense_hat import SenseHat
from datetime import datetime
BROADCAST_TO_PORT = 11001
from socket import *

sense = SenseHat()
sense.clear()

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

def doIt(updatedEvery):
 now = datetime.now().time().minute
 if True: #now % updatedEvery == 0:
  response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Roskilde,DK&APPID=f0f18be3bdaa24b17b922c92f5cd9279")
  data = response.json()
  outhum = data["main"]["humidity"]
  s.sendto(bytes("o"+str(outhum), "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
  s.sendto(bytes(hum, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
  print(hum)
  print("o"+str(outhum))
  time.sleep(10)

while True:
 hum = str(sense.get_humidity())
 sense.set_pixels(double_digits.get_digit_array(int(sense.get_humidity()), (255,0,0)))
 
 doIt(15)

 

 #time.sleep(10)
