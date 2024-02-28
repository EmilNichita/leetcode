#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from collections import Counter

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashes = [(self.word_to_tuple(word), i) for i, word in enumerate(strs)]
        sorted_hashes = sorted(hashes)
        
        index_groups = [[sorted_hashes[0][1]]]
        curr_hash = sorted_hashes[0][0]
        
        for hash_tuple, i in sorted_hashes[1:]:
            if curr_hash == hash_tuple:
                index_groups[-1].append(i)
            else:
                curr_hash = hash_tuple
                index_groups.append([i])
        
        
        result = [[strs[i] for i in index_group] for index_group in index_groups]
        return result
    
    def word_to_tuple(self, word: str) -> tuple:
        c = Counter(word)
        result = []
        for letter in "abcdefghijklmnopqrstuvwxyz":
            result.append(c[letter] if letter in c else 0)
        return tuple(result)
# @lc code=end

