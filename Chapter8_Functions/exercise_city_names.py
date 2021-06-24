def city_country(city_name, country_name):
    location_name = f'"{city_name.title()}, {country_name.title()}"'
    return location_name.title()

while True:
    print("\nAdd name of the city and country")
    city_input = input("City Name: ")

    if city_input == 'q':
        break

    country_input = input("Country Name: ")
    if country_input == 'q':
        break

    location = city_country(city_input, country_input)
    print(location)
