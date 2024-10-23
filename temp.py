def convert_temperature(temperature, unit):
    if unit == "F":
        return fahrenheit_to_others(temperature)
    elif unit == "C":
        return celsius_to_others(temperature)
    elif unit == "K":
        return kelvin_to_others(temperature)
    else:
        return "Invalid unit"

def fahrenheit_to_others(temperature):
    celsius = fahrenheit_to_celsius(temperature)
    if celsius is None:
        return "Invalid temperature"
    kelvin = celsius_to_kelvin(celsius)
    if kelvin is None:
        return "Invalid temperature"
    return celsius, kelvin

def celsius_to_others(temperature):
    fahrenheit = celsius_to_fahrenheit(temperature)
    if fahrenheit is None:
        return "Invalid temperature"
    kelvin = celsius_to_kelvin(temperature)
    if kelvin is None:
        return "Invalid temperature"
    return fahrenheit, kelvin

def kelvin_to_others(temperature):
    celsius = kelvin_to_celsius(temperature)
    if celsius is None:
        return "Invalid temperature"
    fahrenheit = celsius_to_fahrenheit(celsius)
    if fahrenheit is None:
        return "Invalid temperature"
    return celsius, fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    if celsius < -273.15:
        return None
    return celsius

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    if kelvin < 0:
        return None
    return kelvin

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * (9 / 5)) + 32
    if fahrenheit < -459.67:
        return None
    return fahrenheit

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    if celsius < -273.15:
        return None
    return celsius

print(convert_temperature(25, "C"))