class Solution(object):
    def addBinary(self, a, b):
       #the one liner
        return bin(int(a, 2) + int(b, 2))[2:]