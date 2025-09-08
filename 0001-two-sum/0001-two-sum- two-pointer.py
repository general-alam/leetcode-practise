class Solution(object):
    def twoSum(self, nums, target):
        """
        Two-pointer approach after sorting:
        - Build a list of [value, index] pairs to note original indices
        - Sort the list by value (ascending)
        - Use two pointers (left, right) to adjust sum toward the target
        - Return the indices in ascending order
        
        Time:  O(n log n) - dominated by sorting
        Space: O(n) - for the list of pairs
        """
        
        A = [[num, i] for i, num in enumerate(nums)]
        A.sort()

        i, j = 0, len(nums) - 1
        while i < j: 
            current = A[i][0] + A[j][0]
            if current == target: 
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
            elif current < target:
                i += 1
            else:
                j -= 1 
        return []
        
