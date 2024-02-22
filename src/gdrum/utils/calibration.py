import time
import busio
import board
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from gdrum.logic.config_manager import load_config, save_config, update_channel_calibration

# Inicialización del ADS1115
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

# Definición de la función para leer el valor del sensor
def read_sensor_value(channel):
    analog_in = AnalogIn(ads, channel)
    return analog_in.value

# Función de calibración que calcula el debouncing y el umbral
def calibrate_debouncing(channel, sample_rate=0.01, max_duration=1, num_hits=3, hit_threshold=8000):
    print(f"\nPrepárate para golpear el sensor {num_hits} veces.")
    hit_values = []  # Almacena los valores de cada golpe válido
    bounce_durations = []  # Almacena la duración de los rebotes de cada golpe

    for hit in range(num_hits):
        print(f"Golpe {hit+1} en 3 segundos...")
        time.sleep(3)  # Espera antes de registrar el golpe
        print("¡Golpea el sensor ahora!")
        
        start_time = time.time()
        hit_detected = False

        # Ciclo de detección de golpes
        while time.time() - start_time < max_duration:
            current_value = read_sensor_value(channel)
            if current_value >= hit_threshold:
                if not hit_detected:
                    bounce_start_time = time.time()
                    hit_detected = True
                    hit_values.append(current_value)  # Registra el valor del golpe
            else:
                if hit_detected:
                    bounce_end_time = time.time()
                    bounce_durations.append(bounce_end_time - bounce_start_time)
                    break
            time.sleep(sample_rate)
    
    # Calcular y devolver el umbral promedio y el tiempo de debouncing
    if hit_values:
        average_threshold = sum(hit_values) / len(hit_values)
        max_bounce_duration = max(bounce_durations, default=0)
        recommended_debounce_time = max_bounce_duration + 0.02
        print(f"Umbral promedio calculado: {average_threshold}")
        print(f"Recomendación de debouncing basada en el rebote más largo: {recommended_debounce_time:.3f} segundos")
        return average_threshold, recommended_debounce_time
    else:
        print("No se detectaron golpes significativos.")
        return None, None

# Función principal que ejecuta la calibración para todos los canales
def main():
    config = load_config()

    for channel_config in config["channels"]:
        channel_const = getattr(ADS, channel_config["channel"])  # Convierte el nombre del canal a la constante ADS
        threshold, debounce_time = calibrate_debouncing(channel_const)

        if threshold is not None and debounce_time is not None:
            update_channel_calibration(config, channel_config["name"], threshold, debounce_time, True)
        else:
            update_channel_calibration(config, channel_config["name"], is_active=False)

    print("Updating Configuration...")
    save_config(config)

if __name__ == "__main__":
    main()