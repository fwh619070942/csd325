def get_city_name_function(city, country, population='', language=''):
    """Generate a neatly formatted population"""
    if population:
        if language:
            city_country = f"{city}, {country} - population {population}, {language}"
        else:
            city_country = f"{city}, {country} - population {population}"
    else:
        if language:
            city_country = f"{city}, {country}, {language}"
        else:
            city_country = f"{city}, {country}"

    return city_country


def multiple_cities_name():
    """Passing parameters using get_city_name_function"""
    city1 = get_city_name_function("Miami", "USA", "50000000", "Spanish")

    print(city1)



if __name__ == "__main__":
    multiple_cities_name()
