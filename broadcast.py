BROADCAST_TO_PORT = 11001
import time

from socket import *
from datetime import datetime
from sense_hat import SenseHat


sense = SenseHat()

red = (255, 0, 0)





s = socket(AF_INET, SOCK_DGRAM)

s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
while True:
	x = sense.get_humidity()

	g= float("{0:.2f}".format(x))
	
	print(g)
	
	data = "Temp " + str(g)
	s.sendto(bytes(data, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
	sense.show_message("%.1f C" % g, scroll_speed=0.1, text_colour=[255, 0, 0])
	time.sleep(0.1)


