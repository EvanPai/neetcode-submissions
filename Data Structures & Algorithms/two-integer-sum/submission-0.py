class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # intution：
        # check every pair of number whether they match the target
        # O(n^2)

        # better solution:
        # using dict to store the number
        # O(n)

        seen = dict()
        for i, num in enumerate(nums):
            # if the target - num in seen, means it is a match
            # ex: 7 - 4 = 3, and 3 is in seen, which is seen[3] = 0
            if (target - num) in seen: 
                return [seen[target - num], i]

            # add into the dict
            seen[num] = i # the index
