#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start

import random

class RandomizedSet:

    def __init__(self):
        self.d, self.l = {}, []

    def insert(self, val: int) -> bool:

        if val in self.d:
            return False
        
        self.d[val] = len(self.l)
        self.l.append(val)

        return True


    def remove(self, val: int) -> bool:

        if val not in self.d:
            return False
        
        last_elem_in_list = self.l[-1]
        index_of_elem_to_remove = self.d[val]

        self.d[last_elem_in_list] = index_of_elem_to_remove
        self.l[index_of_elem_to_remove] = last_elem_in_list
        self.l[-1] = val
        self.l.pop()
        self.d.pop(val)

        return True

    def getRandom(self) -> int:
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

