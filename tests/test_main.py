import unittest
from main import map_country_to_continent

class TestCountryToContinentMapping(unittest.TestCase):
    def test_valid_country(self):
        
        self.assertEqual(map_country_to_continent("United States"), "North America")
        self.assertEqual(map_country_to_continent("India"), "Asia")
        self.assertEqual(map_country_to_continent("France"), "Europe")
    
    def test_invalid_country(self):
        
        self.assertEqual(map_country_to_continent("Atlantis"), "Unknown")
    
    def test_empty_country(self):
      
        self.assertEqual(map_country_to_continent(""), "Unknown")
    
    def test_null_input(self):
       
        self.assertEqual(map_country_to_continent(None), "Unknown")
    
    def test_case_insensitivity(self):
        
        self.assertEqual(map_country_to_continent("united states"), "North America")
        self.assertEqual(map_country_to_continent("INDIA"), "Asia")
        self.assertEqual(map_country_to_continent("france"), "Europe")

if __name__ == "__main__":
    unittest.main()
