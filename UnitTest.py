from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.testCases = {
            1: {'nums': [6,0,8,2,1,5], 'output': 4},
            2: {'nums': [9,8,1,0,1,9,4,0,4,1], 'output': 7}
        }
        self.obj = Solution()
        return super().setUp()
    
    def test_Case1(self):
        nums, output = self.testCases[1].values()
        result = self.obj.maxWidthRamp(nums)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    def test_Case2(self):
        nums, output = self.testCases[2].values()
        result = self.obj.maxWidthRamp(nums)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()