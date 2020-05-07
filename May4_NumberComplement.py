# Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.

# Input: num = 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

#Input: num = 1
# Output: 0
#Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 
#Constraints:

#The given integer num is guaranteed to fit within the range of a 32-bit signed integer.
#num >= 1
#You could assume no leading zero bit in the integer’s binary representation.
#This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/

class Solution:
    def findComplement(self, num: int) -> int:        
        # k="{0:b}".format(num)       
        # l=['0' if i =='1' else '1'for i in k]
        # l1=''.join(l)
        # return int(l1,base=2)
        # bit=1
        # temp=num
        # while temp:
        #     num=num ^ bit
        #     bit=bit<<1
        #     temp=temp>>1
        # return num
        # i=1
        # while i<=num:
        #     i=i*2
        # if i==num:
        #     return num-1
        # else:
        #     return i-1-num
        b_str = bin(num).replace('0b', '')
        mask_str = ''.join(['1'] * len(b_str))
        return num ^ int(mask_str, 2)
