class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # optimal solution : 
        # 用len = 26的array，儲存所有小寫英文字母
        # 用ord(char) - ord('a') 取得對應的數字位置
        # 通常coding test時可以用from collections import defaultdict 
        if len(s) != len(t): 
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for num in count:
            if num != 0:
                return False

        return True