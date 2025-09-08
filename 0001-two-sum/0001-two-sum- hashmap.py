class Solution(object):
    def twoSum(self, nums, target):
        """
        Hashmap approach:
        - Iterate once through nums
        - For each number, check if its complement (target - n) has been seen
        - If yes, return the pair of indices
        - Otherwise, store the number in the hashmap
        
        Time: O(n)  — each lookup/insertion is O(1) average
        Space: O(n) — hashmap may store all elements
        """ 

        prevMap = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in prevMap:
                return [prevMap[difference], i]
            prevMap[n] = i




        
