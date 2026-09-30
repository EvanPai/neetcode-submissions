class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # method 1:
        # 一個pointer從頭開始，另一個從尾巴開始，如果都一樣就繼續，直到撞到中間
        # 阿不對，搞錯題目了不是頭尾相連

        # method : 
        # 是用python dict，有出現的元素就++，最後在每個元素對比
        from collections import defaultdict

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for char in s:
            s_dict[char] += 1

        for char in t:
            t_dict[char] += 1

        # compare 兩個dict
        return s_dict == t_dict