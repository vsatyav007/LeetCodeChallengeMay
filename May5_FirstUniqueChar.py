# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # for i in s:
        #     if s.count(i)==1:
        #         return s.index(i)
        # return -1
        # dict1={}
        # for i in s:
        #     if i in dict1:
        #         dict1[i]+=1
        #     else:
        #         dict1[i]=1
        # for idx,i in enumerate(s):
        #     if dict1[i]==1:
        #         return idx
        # return -1
        # count = collections.Counter(s)
        # for idx, letter in enumerate(s):
        #     if count[letter] == 1:
        #         return idx
        # return -1
        my_set1 = set()
        for i, c in enumerate(s):
            if c not in my_set1: my_set1.add(c)
            else: continue
            if c in s[i+1:]: continue
            else: return i
        
        return -1
