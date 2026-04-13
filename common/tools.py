# 1. W pliku tools utwórz funkcję, która przekonwertuje stopnie kelvina w wyłapanej pogodzie na stopnie Celsjusza

def kelvin_to_celsius(temp_k):
    return round(temp_k - 273.15, 1)


# 2. W pliku tools utwórz funkcję, która przekonwertuje metry na sekundę na kilometry na godzine (wiatr)

def ms_to_kmhm(speed_ms):
    kmh = speed_ms * 3.6
    return round(kmh, 2)

# 3. Z informacji pogodowych wydobądź:
# - wilgotność
# - ciśnienie
# - słowny opis pogody
