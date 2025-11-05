"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""
temperatures = [15.3, 17.1, 18.4, 19.2, 16.8, 14.9, 15.7]
city_population = {
    "Vilnius": 592000,
    "Kaunas": 295000,
    "Klaipėda": 152000,
    "Šiauliai": 101000,
    "Panevėžys": 87000
}

average_temperature = sum(temperatures) / len(temperatures)
largest_city = max(city_population.items(), key=lambda item: item[1])[0]
largest_population = city_population[largest_city]
smallest_city = min(city_population.items(), key=lambda item: item[1])[0]
smallest_population = city_population[smallest_city]
total_population = sum(city_population.values())

print("=== Weekly Temperature Report ===")
print(f"Average temperature: {average_temperature:.2f}°C")
print(f"Highest temperature: {max(temperatures):.1f}°C")
print(f"Lowest temperature: {min(temperatures):.1f}°C")
print()
print("=== City Population Report ===")
print(f"Largest city: {largest_city} - {largest_population:,} people")
print(f"Smallest city: {smallest_city} - {smallest_population:,} people")
print(f"Total population: {total_population:,} people")
