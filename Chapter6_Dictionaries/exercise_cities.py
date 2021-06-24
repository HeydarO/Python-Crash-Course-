cities = {
    'baku': {
        'country': 'Azerbaijan',
        'population': '2.236 million',
        'fact': 'home city',
        },

    'moscow': {
        'country': 'Russia',
        'population': '11.92 million',
        'fact': 'birthplace',
        },

    'Houston': {
        'country': 'USA',
        'population': '2.31 million',
        'fact': 'second home city',
        },
    }

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print(f"\tCountry the city located is {country.title()}.")
    print(f"\tPopulaton of this city is {population}.")
    print(f"\tThis city is my {fact}.")
