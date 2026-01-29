# Exercise 3: Managing Cities and Populations (Nested)

world_cities = {
    "USA": {
        "New York": 8419000,
        "Los Angeles": 3980000,
        "Chicago": 2705000
    },
    "Canada": {
        "Toronto": 2930000,
        "Vancouver": 675000
    }
}

# Adding a new country (United Kingdom) with cities
world_cities["United Kingdom"] = {
    "London": 9304000,
    "Manchester": 553230
}

# Accessing the population of New York
ny_population = world_cities["USA"]["New York"]
print(f"Population of New York: {ny_population}")

# Accessing the population of Vancouver
van_population = world_cities["Canada"]["Vancouver"]
print(f"Population of Vancouver: {van_population}")

# Accessing population of a newly added city (London)
london_population = world_cities["United Kingdom"]["London"]
print(f"Population of London: {london_population}")

# Adding a new city to Canada
world_cities["Canada"]["Montreal"] = 1780000
print(f"Montreal's population added to Canada: {world_cities['Canada']['Montreal']}")

print("-" * 30)

# Loop to print all cities and populations of USA
print("Cities and populations in the USA:")
for city, population in world_cities["USA"].items():
    print(f"{city}: {population}")
