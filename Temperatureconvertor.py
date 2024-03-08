def convert_temperature(temperature, unit):


  if unit.upper() == "F":
    celsius = (temperature - 32) * 5 / 9
  elif unit.upper() == "K":
    celsius = temperature - 273.15
  else:
    celsius = temperature

  
  fahrenheit = (celsius * 9 / 5) + 32
  kelvin = celsius + 273.15

  return {
      "Celsius": celsius,
      "Fahrenheit": fahrenheit,
      "Kelvin": kelvin
  }


while True:
  try:
    temperature = float(input("Enter temperature value: "))
    unit = input("Enter unit (C, F, or K): ").upper()
    if unit not in ("C", "F", "K"):
      raise ValueError("Invalid unit. Please enter C, F, or K.")
    break
  except ValueError as e:
    print("Error:", e)


converted_temps = convert_temperature(temperature, unit)
print("Converted temperatures:")
for unit, value in converted_temps.items():
  print(f"{temperature:.2f} degrees {unit} is equivalent to {value:.2f} degrees {unit}")
