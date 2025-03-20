# Dictionary of planets and their gravity percentage compared to Earth's gravity
planet_gravity = {
    "Mercury": 37.6,
    "Venus": 88.9,
    "Mars": 37.8,
    "Jupiter": 236.0,
    "Saturn": 108.1,
    "Uranus": 81.5,
    "Neptune": 114.0
}

# Get user input for their weight on Earth
earth_weight = float(input("Enter a weight on Earth: "))

# Get user input for the planet name
planet = input("Enter a planet: ")

# Check if the planet is in the dictionary
if planet in planet_gravity:
    # Calculate the weight on the selected planet
    planet_weight = earth_weight * (planet_gravity[planet] / 100)
    # Print the equivalent weight rounded to 2 decimal places
    print(f"The equivalent weight on {planet}: {round(planet_weight, 2)}")
else:
    print("Planet not recognized.")
