class Solution():
    def isPowerOfThree(self, x:int) -> bool():
    
        if x == 0:
            return False

        if x == 1:
            return True
        
        if (x % 3 != 0):
            return False

        else:
            return self.isPowerOfThree(x/3)

examples = Solution()
print(examples.isPowerOfThree(27))
print(examples.isPowerOfThree(0))
print(examples.isPowerOfThree(-1))

