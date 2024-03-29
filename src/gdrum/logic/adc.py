import pygame
import board
import busio
import time
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


channels_info = {
    "Channel_0": {"name": "Channel 0", "method": None, "isActive": False, "sound": "bass.wav", "intital_value":0,"last_activation_time":0,"threshold_value":3000},
    "Channel_1": {"name": "Channel 1", "method": None, "isActive": False, "sound": "slap.wav", "intital_value":0,"last_activation_time":0,"threshold_value":10000},
    "Channel_2": {"name": "Channel 2", "method": None, "isActive": False, "sound": "tone.wav", "intital_value":0,"last_activation_time":0,"threshold_value":10000},
    "Channel_3": {"name": "Channel 3", "method": None, "isActive": False, "sound": "sound3.wav","intital_value":0,"last_activation_time":0,"threshold_value":0}
}


channels = [ADS.P0,ADS.P1,ADS.P2,ADS.P3]
DEBOUNCE_TIME = 0.2
CHANNEL_THRESHOLD = 4000 # verify if the channel is active
VALUE_THRESHOLD = 12000
pygame.mixer.init()


# Initialize the I2C interface
i2c = busio.I2C(board.SCL, board.SDA)
# Create an ADS1115 object
ads = ADS.ADS1115(i2c)

# Define the analog input channel
#chn0 = AnalogIn(ads, ADS.P0)
#chn1 = AnalogIn(ads, ADS.P1)
#chn2 = AnalogIn(ads, ADS.P2)
#chn3 = AnalogIn(ads, ADS.P3)


def sample_value_channel(channel ,number_samples=10, wait_time= 0.1):
    print("Muestreando valor,Por favor, no golpees el sensor.")
    sample_values = []
    for _ in range(number_samples):
        actual_value = read_sensor_value(channel)  
        sample_values.append(actual_value)
        time.sleep(wait_time)  
 
    average_value= sum(sample_values) / len(sample_values)
    print(f"Sample value :{average_value}")
    return average_value

def read_sensor_value(channel):
	analog_in = AnalogIn(ads, channel)
	return analog_in.value

def verify_channels():
	print("Checking Channels...")
	for i , channel in enumerate(channels):
		initial_value = sample_value_channel(channel, 10)
		if(initial_value < CHANNEL_THRESHOLD):
			print(f"Channel-{i} is active")
			analog_in = AnalogIn(ads, channel)
			channels_info[f"Channel_{i}"]["method"]=lambda ai=analog_in: (ai.value, ai.voltage)
			channels_info[f"Channel_{i}"]["isActive"]= True
			channels_info[f"Channel_{i}"]["initial_value"]= initial_value
		

def read_channels():
	current_time = time.time()
	for channel_key, channel_info in channels_info.items():
		if channel_info["isActive"]:
			elapsed_time = current_time - channel_info.get("last_activation_time", 0)
			if elapsed_time >= DEBOUNCE_TIME:
				value, voltage = channel_info["method"]()
				#print(f"sound value channel {channel_info['name']}: {value}")
				#time.sleep(0.5)
				if value > channel_info['threshold_value']:
					channel_info['last_activation_time'] = current_time
					# Reproducir el sonido asociado
					sound = pygame.mixer.Sound(channel_info['sound'])
					sound.play()
					print(f"sound value channel {channel_info['name']}: {value}")
					channel_info['last_activation_time'] = current_time
	time.sleep(0.05)


def main():
	verify_channels()
	while  True:
		try:
			read_channels() 

if __name__ == "__main__":
    main()
