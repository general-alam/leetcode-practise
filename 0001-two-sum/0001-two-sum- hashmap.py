class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        prevMap = {} # create a hashmap of the integers we've explored from the nums list

        for i, n in enumerate(nums):
            difference = target - n
            if difference in prevMap:
                return [prevMap[difference], i]
            prevMap[n] = i #if the needed value to obtain the target is not found, add i to the hashmap of explored integers



        # Time complexity - O(n)
        # Space complexity - O(n)



        