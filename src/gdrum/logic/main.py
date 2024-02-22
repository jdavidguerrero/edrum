import time
import busio
import board
import adafruit_ads1x15.ads1115 as ADS
from config_manager import load_config, get_channel_config
from sensor_channel import SensorChannel

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

config = load_config()

channels = []
for ch_config in config["channels"]:
    channel_params = get_channel_config(ads, ch_config)
    channel = SensorChannel(**channel_params)
    channels.append(channel)


while True:
    current_time = time.time()
    for channel in channels:
        channel.check_and_activate(current_time)
    #time.sleep(0.01) 