import unittest
import fuel_required

class TestFuelRequired(unittest.TestCase):

  def test_fuel_required(self):
    self.assertEqual(fuel_required.fuel_required(12), 2)
    self.assertEqual(fuel_required.fuel_required(14), 2)
    self.assertEqual(fuel_required.fuel_required(1969), 654)
    self.assertEqual(fuel_required.fuel_required(100756), 33583)

  def test_total_fuel_required(self):
    self.assertEqual(fuel_required.total_fuel_required(12), 2)
    self.assertEqual(fuel_required.total_fuel_required(1969), 966)
    self.assertEqual(fuel_required.total_fuel_required(100756), 50346)


if __name__ == '__main__':
  unittest.main()
