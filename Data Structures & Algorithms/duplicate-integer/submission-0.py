class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # method 1:
        # 建立一個hash table, 像是用python的set，把元素丟進去，如果沒有的元素就丟
        # 遇到有的話就直接回傳True, 結束程式
        hash_table = set() # set
        for num in nums:
            if num not in hash_table:
                hash_table.add(num)
            else:
                return True

        return False

        