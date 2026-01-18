"""City Population Analyzer"""
cities = {
    "Bengaluru":8443675,
    "Mysuru":920550,
    "Chennai":7090000,
    "Delhi":16787941,
    "Mumbai":12442373
}
filter_cities= {city:pop for city, pop in cities.items() if pop > 8000000}
print(filter_cities)


def add_city(cities,name,population):
    cities[name] = population
    print(f"{name} added successfully.")

def delete_city(cities,name):
    if name in cities:
        del cities[name]
        print(f"{name} deleted successfully.")
    else:
        print("City not found.")

def search_city(cities,name):
    if name in cities:
        print(f"{name} population is {cities[name]}")
    else:
        print("city not found.")

add_city(cities,"K R Nagara",500000)
delete_city(cities,"Mysuru")
search_city(cities,"Bengaluru")
