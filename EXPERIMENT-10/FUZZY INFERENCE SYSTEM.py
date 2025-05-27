import numpy as np

# 1. Define fuzzy membership functions for inputs and output

# Temperature (Low, Medium, High)
def temperature_membership(temp):
    low = max(0, min(1, (25 - temp) / 25))  # Low temperature (0 to 25°C)
    medium = max(0, min(1, (temp - 15) / 10, (30 - temp) / 10))  # Medium (15 to 30°C)
    high = max(0, min(1, (temp - 25) / 15))  # High temperature (25°C and above)
    return low, medium, high

# Humidity (Low, High)
def humidity_membership(humidity):
    low = max(0, min(1, (50 - humidity) / 50))  # Low humidity (0 to 50%)
    high = max(0, min(1, (humidity - 50) / 50))  # High humidity (50% and above)
    return low, high

# Fan Speed membership values (for defuzzification reference points)
def fan_speed_membership(fan_speed):
    # This function is not strictly needed here; we use crisp values directly.
    low = max(0, min(1, (50 - fan_speed) / 50))  # Low fan speed (0 to 50%)
    high = max(0, min(1, (fan_speed - 50) / 50))  # High fan speed (50% and above)
    return low, high

# 2. Define the fuzzy inference system
def fuzzy_inference(temp, humidity):
    # Get fuzzy membership values for temperature and humidity
    low_temp, medium_temp, high_temp = temperature_membership(temp)
    low_hum, high_hum = humidity_membership(humidity)

    # Rule 1: If temperature is low AND humidity is low, then fan speed is low
    rule1 = min(low_temp, low_hum)

    # Rule 2: If temperature is high AND humidity is high, then fan speed is high
    rule2 = min(high_temp, high_hum)

    # For simplicity, ignore medium temp rules here or you can extend later

    # 3. Aggregate the rule outputs (firing strengths)
    # For defuzzification, choose representative fan speeds:
    fan_speed_low = 25  # representative crisp value for low fan speed
    fan_speed_high = 75  # representative crisp value for high fan speed

    # Weighted sum for defuzzification (centroid method)
    numerator = rule1 * fan_speed_low + rule2 * fan_speed_high
    denominator = rule1 + rule2

    if denominator == 0:
        return 0  # No rules fired, fan off

    return numerator / denominator

# 4. Test the system
temp_input = 28      # Temperature in °C
humidity_input = 60  # Humidity in %

fan_speed_output = fuzzy_inference(temp_input, humidity_input)
print(f"Fan Speed Output (Crisp Value): {fan_speed_output:.2f}%")
