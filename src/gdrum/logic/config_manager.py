import json
import adafruit_ads1x15.ads1115 as ADS


FILE_NAME = "/home/pi/Documents/edrum/src/gdrum/logic/config.json"
def load_config(filename= FILE_NAME):
    """Load json config."""
    with open(filename, "r") as file:
        return json.load(file)

def get_channel_config(ads, channel_config):
    """obtains the conf per channel according to the channel."""
    channel = getattr(ADS, channel_config["channel"]) 
    return {
        "ads": ads,
        "channel": channel,
        "sound_file": channel_config["sound"],
        "threshold_value": channel_config["threshold_value"],
        "is_active": channel_config["isActive"],
        "debounce_time": channel_config.get("debounce_time", 0.1) 
    }

def update_channel_calibration(config, channel_name, threshold=None, debounce_time=None, is_active=None):
    """Actualiza la configuración de un canal específico en la configuración."""
    print(f"Updating {channel_name} calibration")
    found = False
    for channel in config['channels']:
        if channel['name'] == channel_name:
            if threshold is not None:
                channel['threshold_value'] = threshold
            if debounce_time is not None:
                channel['debounce_time'] = debounce_time
            if is_active is not None:
                channel['isActive'] = is_active
            found = True
            break
    if not found:
        print(f"Advertencia: Canal '{channel_name}' no encontrado en la configuración.")

def save_config(config, filename=FILE_NAME):
    """Save the configuration in the json file."""
    with open(filename, "w") as file:
        json.dump(config, file, indent=4) 