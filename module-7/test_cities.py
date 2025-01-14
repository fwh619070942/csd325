import unittest
import city_functions

class TestCityCountry(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        """Assert city, country, population, and language are correct"""
        formatted_city_country = city_functions.get_city_name_function("Miami", "USA", "50000000")
        print(formatted_city_country)
        self.assertEqual(formatted_city_country, "Miami, USA - population 50000000")

        formatted_city_country = city_functions.get_city_name_function("Omaha", "USA", language="English")
        print(formatted_city_country)
        self.assertEqual(formatted_city_country, "Omaha, USA, English")
                
        formatted_city_country = city_functions.get_city_name_function("Los Angeles", "USA", "500000000", "English")
        print(formatted_city_country)
        self.assertEqual(formatted_city_country, "Los Angeles, USA - population 500000000, English")




if __name__ == '__main__':
    unittest.main()