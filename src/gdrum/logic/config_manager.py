import json
import adafruit_ads1x15.ads1115 as ADS

def load_config(filename="config.json"):
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

def save_config(config, filename="config.json"):
    """Save the configuration in the json file."""
    with open(filename, "w") as file:
        json.dump(config, file, indent=4) 