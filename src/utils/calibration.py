import time
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import busio
import board

channels = [ADS.P0, ADS.P1, ADS.P2, ADS.P3]  # Lista de canales

# Configuración inicial del ADS1115
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)



def read_sensor_value(channel):
    """Lee el valor actual del sensor."""
    analog_in = AnalogIn(ads, channel)
    return analog_in.value

def calibrate_debouncing(channel, sample_rate=0.005, max_duration=1, num_hits=4, hit_threshold=8000):
    """
    Calibra el tiempo de debouncing para un canal con múltiples golpes considerando un umbral.
    :param channel: Canal a calibrar.
    :param sample_rate: Tasa de muestreo en segundos.
    :param max_duration: Duración máxima en segundos para escuchar el rebote.
    :param num_hits: Número de golpes a realizar para la calibración.
    :param hit_threshold: Umbral mínimo de valor para considerar un golpe válido.
    :return: Tiempo en segundos recomendado para debouncing.
    """
    print(f"\nPrepárate para golpear el sensor {num_hits} veces a intervalos regulares.")
    time.sleep(1)  # Da tiempo al usuario para prepararse.

    bounce_durations = []  # Almacena la duración de los rebotes de cada golpe

    for hit in range(num_hits):
        for i in range(3):
            print(f"En {3-i}...")
            time.sleep(1); 
        print(f"Golpe {hit+1}. ¡Golpea el sensor ahora!")
        hit_detected = False
        start_time = time.time()

        # Ciclo de detección de rebotes y golpes
        while time.time() - start_time < max_duration:
            current_value = read_sensor_value(channel)
            if current_value >= hit_threshold and not hit_detected:
                bounce_start_time = time.time()
                hit_detected = True
            elif hit_detected and current_value < hit_threshold:
                bounce_end_time = time.time()
                bounce_durations.append(bounce_end_time - bounce_start_time)
                break
            time.sleep(sample_rate)
        time.sleep(1)  # Espera un poco antes de comenzar a registrar para el siguiente golpe

    if bounce_durations:
        max_bounce_duration = max(bounce_durations)
        recommended_debounce_time = max_bounce_duration + 0.02  # Añade un margen
        print(f"Recomendación de debouncing basada en el rebote más largo: {recommended_debounce_time:.3f} segundos")
        return recommended_debounce_time
    else:
        print("No se detectaron rebotes significativos. Considera ajustar manualmente.")
        return None

# Ejemplo de cómo calibrar un canal
for channel in channels:
    print(f"sensor {channel}")
    calibrate_debouncing(channel, sample_rate=0.01, max_duration=2)
