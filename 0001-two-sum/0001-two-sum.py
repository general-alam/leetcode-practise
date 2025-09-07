class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        A = []
        for i, num in enumerate(nums):
            A.append([num,i])
        # creates a list of an integer and it's corresponding index 

        A.sort()
        i = 0
        j = len(nums) - 1
        while i < j: 
            current = A[i][0] + A[j][0]
            if current == target: 
                # returns it in the correct order - smallest index first
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
            
            # moves across the sorted list appropriately to meet the match quicker
            elif current < target:
                i += 1
            elif current > target:
                j -= 1 
        return []

        # Time Complexity: O(n log n)
        # Space Complexity: O(n)
        