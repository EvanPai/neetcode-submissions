class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagrams -> using set to count the alphabet

        from collections import defaultdict


        # the dict using every word's frequency set as key, and the word as value.
        # because the anagrams will have same frequency, so the anagrams will be add into the same group
        group = defaultdict(list) 


        # for every word, there is a set for it, and store the word in the dict as value using the set as key
        # like group[tuple()]
        for word in strs:

            # count the frequency for the word
            count = [0] * 26 
            for j in range(len(word)):
                count[ord(word[j]) - ord("a")] += 1

            # add into the dict using tuple(count) as key, and word as value

            group[tuple(count)].append(word)

        return list(group.values())


        