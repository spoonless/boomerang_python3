# conversion farenheit en celsius

temp_farenheit_saisie = input("Température Fahrenheit : ")
temp_farenheit = float(temp_farenheit_saisie)

temp_celsius = (temp_farenheit - 32) / 1.8
print(f"Une temperature de {temp_farenheit:.1f}°F "
      f"correspond à {temp_celsius:.1f}°C")