# Prompt user for temperature in Fahrenheit
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert to Celsius
celsius = (fahrenheit - 32) * 5.0 / 9.0

# Print the result
print(f"Temperature: {fahrenheit}F = {celsius}C")
