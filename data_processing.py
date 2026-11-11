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
print()

print("-" * 50)
print("Refactoring")
print("-" * 50)
print()

def filter_items(condition, dict_list):
    """
    Return a new list containing only the dictionaries that satisfy
    the given condition function.

    Args:
        condition: A function that takes a dictionary and returns True or False.
        dict_list: A list of dictionaries.

    Returns:
        A list of dictionaries for which condition(item) is True.

    Examples:
        >>> students = [
        ...     {"name": "Alice", "score": 90},
        ...     {"name": "Bob", "score": 70},
        ...     {"name": "Charlie", "score": 85}
        ... ]
        >>> filter_items(lambda s: s["score"] >= 85, students)
        [{'name': 'Alice', 'score': 90}, {'name': 'Charlie', 'score': 85}]

        >>> filter_items(lambda s: s["name"].startswith("A"), students)
        [{'name': 'Alice', 'score': 90}]

        >>> filter_items(lambda s: s["score"] > 100, students)
        []
    """
    return [item for item in dict_list if condition(item)]


def aggregate(aggregation_key, aggregation_function, dict_list):
    """
    Aggregate values associated with aggregation_key using the
    provided aggregation function.

    Args:
        aggregation_key: The dictionary key whose values should be aggregated.
        aggregation_function: A function such as sum, max, min, etc.
        dict_list: A list of dictionaries.

    Returns:
        The aggregated result.

    Examples:
        >>> students = [
        ...     {"name": "Alice", "score": 90},
        ...     {"name": "Bob", "score": 70},
        ...     {"name": "Charlie", "score": 85}
        ... ]

        >>> aggregate("score", sum, students)
        245

        >>> aggregate("score", max, students)
        90

        >>> aggregate("score", min, students)
        70

        >>> aggregate(
        ...     "score",
        ...     lambda scores: sum(scores) / len(scores),
        ...     students
        ... )
        81.66666666666667
    """
    value = [item[aggregation_key] for item in dict_list]
    return aggregation_function(value)

# Print the average temperature of all the cities
print("The average temperature of all the cities")
avg_temp = aggregate(("temperature"), lambda temp: sum(float(x)for x in temp) / len(temp), cities)
print(avg_temp)
print()

# Print all cities in Germany
print("All cities in Germany")
cities_germany = filter_items(lambda city: city['country'] == 'Germany', cities)
print(city_in_germany)
print()

# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C")
cities_germany = filter_items(lambda city: city['country'] == 'Spain' and float(city['temperature']) > 12, cities)
print(city_in_spain)
print()

# Count the number of unique countries
print("The number of unique countries")
num_of_uniq_country = len(set(aggregate("country", lambda country: country, cities)))
print(num_of_uniq_country)
print()

# Print the average temperature for all the cities in Germany
print("The average temperature for all the cities in Germany")
germany = filter_items(lambda city: city["country"] == "Germany", cities)
avg_temp_in_germany = aggregate("temperature", lambda temp: sum(float(x) for x in temp) / len(germany), germany)
print(avg_temp_in_germany)
print()

# Print the max temperature for all the cities in Italy
print("The max temperature for all the cities in Italy")
italy = filter_items(lambda city: city["country"] == "Italy", cities)
max_temp_italy = aggregate("temperature", lambda temp: max(float(x) for x in temp), italy)
print(max_temp_italy)
print()


print("-" * 50)
print("OOP")
print("-" * 50)
print()

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load(self):
        cities = []
        with open(self.filepath, mode='r', encoding='utf-8') as f:
            rows = csv.DictReader(f)
            for r in rows:
                cities.append(dict(r))
        return cities

class Table:
    def __init__(self, data):
        self._data = data

    def filter_item(self, condition):
        filtered_data = [item for item in self._data if condition(item)]
        return Table(filtered_data) 

    def aggregate(self, aggregation_key, aggregation_function):
        values = []
        for item in self._data:
            val = item[aggregation_key]
            try:
                val = float(val)
            except ValueError:
                pass
            values.append(val)
        return aggregation_function(values)

    def get_data(self):
        return self._data

# main
csv_path = os.path.join(__location__, "Cities.csv")
loader = DataLoader(csv_path)
raw_data = loader.load()
cities_table = Table(raw_data)

# Print the average temperature of all the cities
print("The average temperature of all the cities")
avg_temp = cities_table.aggregate("temperature", lambda temp: sum(temp) / len(temp))
print(avg_temp)
print()

# Print all cities in Germany
print("All cities in Germany")
germany_table = cities_table.filter_item(lambda city: city["country"] == 'Germany')
print([c["city"] for c in germany_table.get_data()])
print()

# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C")
spain_warm_table = cities_table.filter_item(lambda city: city['country'] == 'Spain' and float(city['temperature']) > 12)
print([city['city'] for city in spain_warm_table.get_data()])
print()

# Count the number of unique countries
print("The number of unique countries")
uniq = len(set(cities_table.aggregate("country", lambda country: country)))
print(uniq)
print()

# Print the average temperature for all the cities in Germany
print("The average temperature for all the cities in Germany")
avg_german_temp = germany_table.aggregate("temperature", lambda temp: sum(temp) / len(temp))
print(avg_german_temp)
print()

# Print the max temperature for all the cities in Italy
print("The max temperature for all the cities in Italy")
italy_table = cities_table.filter_item(lambda c: c["country"] == 'Italy')
max_italy_temp = italy_table.aggregate("temperature", max)
print(max_italy_temp)
print()
