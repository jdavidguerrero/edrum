import pygame
import board
import busio
import time
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


pygame.mixer.init()

slap = pygame.mixer.Sound('slap.wav')
tone = pygame.mixer.Sound('tone.wav')
bass = pygame.mixer.Sound('bass.wav')
# Initialize the I2C interface
i2c = busio.I2C(board.SCL, board.SDA)
# Create an ADS1115 object
ads = ADS.ADS1115(i2c)
# Define the analog input channel
chn0 = AnalogIn(ads, ADS.P0)
chn1 = AnalogIn(ads, ADS.P1)
chn2 = AnalogIn(ads, ADS.P2)
chn3 = AnalogIn(ads, ADS.P3)


"""
# Loop to read the analog input continuously

#lists to store the time and voltage
#conmg figure to graph

plt.ion()
fig, ax = plt.subplots()
times = []
voltages = []
line, = ax.plot(times, voltages, '-')

def update_graph(frame):
    global times, voltages
    #read voltage
    voltage = chn0.value
    times.append(time.time())
    voltages.append(voltage)
    #limit the points 
    times = times[-50:]
    voltages = voltages[-50:]
    #update line
    line.set_data(times,voltages)
    #adjust limits
    ax.relim()
    ax.autoscale_view()
    #draw
    plt.draw()

#funcAnimation will do that the update_graph is call perodically
ani = FuncAnimation(fig,update_graph, interval=100)

plt.show(block=True)

"""

THRESHOLD = 500
THRESHOLD_BASS = 750





while True:
	
	try:
		# initial checking
		print("Analog Value 0: ", chn0.value, "Voltage 0: ", chn0.voltage)
		print("Analog Value 1: ", chn1.value, "Voltage 1: ", chn1.voltage)
		print("Analog Value 2: ", chn2.value, "Voltage 2: ", chn2.voltage)
		print("Analog Value 3: ", chn3.value, "Voltage 3: ", chn3.voltage)
		
		for i in range(3):
			
		
		
		"""
		if chn0.value > THRESHOLD:
			slap.play()
			time.sleep(0.1)
			print("Slap")
		if chn1.value > THRESHOLD:
			tone.play()
			time.sleep(0.1)
			print("Tone")
		if chn2.value > THRESHOLD_BASS:
			bass.play()
			time.sleep(0.1)
			print("Bass")
			"""
		time.sleep(0.2)
	except Exception as e:
		print(f"Error al leer del ADC: {e}")
		time.sleep(0.1) 
   

