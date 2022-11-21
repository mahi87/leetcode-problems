import unittest

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(list(set(nums)))
    

class SolutionTest(unittest.TestCase):
    def testContainsDuplicate(self):
        s = Solution()
        test_cases = [
            ([1,2,3,1], True),
            ([1,2,3,4], False),
            ([1,1,1,3,3,4,3,2,4,2], True)
        ]
        
        for args,expected in test_cases:
            self.assertEqual(s.containsDuplicate(args), expected)
            
if __name__ == '__main__':
    unittest.main()