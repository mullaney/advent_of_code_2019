import unittest
import day_02

class TestDay02(unittest.TestCase):

  def test_fuel_required(self):
    init_state = [1,9,10,3,2,3,11,0,99,30,40,50]
    final_state = [3500,9,10,70,2,3,11,0,99,30,40,50]
    self.assertEqual(day_02.opcode(init_state.copy()), final_state)

    init_state = [1,1,1,4,99,5,6,0,99]
    final_state = [30,1,1,4,2,5,6,0,99]
    self.assertEqual(day_02.opcode(init_state.copy()), final_state)

    init_state = [2,4,4,5,99,0]
    final_state = [2,4,4,5,99,9801]
    self.assertEqual(day_02.opcode(init_state.copy()), final_state)

if __name__ == '__main__':
  unittest.main()
