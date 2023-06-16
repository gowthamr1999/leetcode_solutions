nums = [1,2,3,4,5]
d = {}
class Solution:    
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in nums:
            if i in d:
                return True
            else:
                d[i] = True
        return False
    

print(d)
s1 = Solution()
print(s1.containsDuplicate(nums))