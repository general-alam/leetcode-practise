class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        seen = set() # sets are an unordered collection of unique data 
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False

        # another solution: use the set constructor to automatically remove duplicates 
        # if set(nums) < len(nums):
        #   return True

        