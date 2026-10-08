class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # optimal solution
        group = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1
            group[tuple(count)].append(word)
        return list(group.values())

        