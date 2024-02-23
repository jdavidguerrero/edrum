import time
import busio
import board
import adafruit_ads1x15.ads1115 as ADS
from config_manager import load_config, get_channel_config
from sensor_channel import SensorChannel
import pygame


i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c, gain=1, data_rate=860)

pygame.mixer.init()

config = load_config()

channels = []
for ch_config in config["channels"]:
    channel_params = get_channel_config(ads, ch_config)
    print(channel_params)
    channel = SensorChannel(**channel_params)
    channels.append(channel)


while True:
    current_time = time.time()
    for channel in channels:
        channel.check_and_activate(current_time)
    #time.sleep(0.01) 