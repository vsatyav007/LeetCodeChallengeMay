# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Input: J = "aA", S = "aAAbbbb"
# Output: 3

# Input: J = "z", S = "ZZ"
# Output: 0

# Note:

# S and J will consist of letters and have length at most 50.
# The characters in J are distinct.


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        out=0
        l1=[-1 for i in range(52)]
        for i in J:
            if ord(i)>=65 and ord(i)<97:
                l1[ord(i)-65]+=1
            else:
                l1[ord(i)-97+26]+=1
        
        for i in S:
            if ord(i)>=65 and ord(i)<97:
                if l1[ord(i)-65]>=0:
                    out+=1
            elif l1[ord(i)-97+26]>=0:
                    out+=1
        return out           
        # Jset=set(J)
        # for i in S:
        #     if i in Jset:
        #         out+=1
        # return out
