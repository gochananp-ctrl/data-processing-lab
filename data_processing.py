import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print("All cities in Germany")
city_in_germany = list(map(lambda city: city['city'], filter(lambda city: city['country'] == 'Germany', cities)))
print(city_in_germany)
print()

# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C")
city_in_spain = list(map(lambda city: city['city'], filter(lambda city: city['country'] == 'Spain' and float(city['temperature']) > 12, cities)))
print(city_in_spain)
print()

# Count the number of unique countries
print("Count the number of unique countries")
uniq_countries = set(map(lambda city: city['country'], cities))
print(len(uniq_countries))
print()

# Print the average temperature for all the cities in Germany
print("The average temperature for all the cities in Germany")
temp_city_in_germany = list(map(lambda city: float(city['temperature']), filter(lambda city: city['country'] == 'Germany', cities)))
print(sum(temp_city_in_germany)/len(temp_city_in_germany))
print()

# Print the max temperature for all the cities in Italy
print("The max temperature for all the cities in Italy")
temp_city_in_itaiy = list(map(lambda city: float(city['temperature']), filter(lambda city: city['country'] == 'Italy', cities)))
print(max(temp_city_in_itaiy))