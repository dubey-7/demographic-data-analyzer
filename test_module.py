import unittest
from demographic_data_analyzer import calculate_demographic_data


class DemographicAnalyzerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = calculate_demographic_data(print_data=False)

    def test_race_count(self):
        self.assertEqual(self.data['race_count']['White'], 27816)
        self.assertEqual(self.data['race_count']['Black'], 3124)

    def test_average_age_men(self):
        self.assertAlmostEqual(self.data['average_age_men'], 39.4, places=1)

    def test_percentage_bachelors(self):
        self.assertAlmostEqual(self.data['percentage_bachelors'], 16.4, places=1)

    def test_higher_education_rich(self):
        self.assertAlmostEqual(self.data['higher_education_rich'], 46.5, places=1)

    def test_lower_education_rich(self):
        self.assertAlmostEqual(self.data['lower_education_rich'], 17.4, places=1)

    def test_min_work_hours(self):
        self.assertEqual(self.data['min_work_hours'], 1)

    def test_rich_percentage(self):
        self.assertAlmostEqual(self.data['rich_percentage'], 10.0, places=1)

    def test_highest_earning_country(self):
        self.assertEqual(self.data['highest_earning_country'], "Iran")

    def test_highest_earning_country_percentage(self):
        self.assertAlmostEqual(
            self.data['highest_earning_country_percentage'], 41.9, places=1
        )

    def test_top_IN_occupation(self):
        self.assertEqual(self.data['top_IN_occupation'], "Prof-specialty")


if __name__ == "__main__":
    unittest.main()
