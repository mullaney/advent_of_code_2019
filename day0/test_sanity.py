import unittest
import sanity

class TestSanity(unittest.TestCase):

  def test_add(self):
    self.assertEqual(sanity.add(7, 3), 10)

if __name__ == '__main__':
  unittest.main()