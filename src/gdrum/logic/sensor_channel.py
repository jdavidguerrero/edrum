import pygame
from adafruit_ads1x15.analog_in import AnalogIn

class SensorChannel:
    def __init__(self, ads, channel, sound_file, threshold_value, is_active, debounce_time):
        self.analog_in = AnalogIn(ads, channel)
        self.sound_file = sound_file
        self.threshold_value = threshold_value
        self.is_active = is_active
        self.debounce_time = debounce_time
        self.last_activation_time = 0
        pygame.mixer.init()

    def check_and_activate(self, current_time):
        if not self.is_active:
            return
        if (current_time - self.last_activation_time) >= self.debounce_time:
            value = self.analog_in.value
            if value > self.threshold_value:
                self.play_sound()
                self.last_activation_time = current_time

    def play_sound(self):
        sound = pygame.mixer.Sound(self.sound_file)
        sound.play()
        print(f"Playing {self.sound_file}")
