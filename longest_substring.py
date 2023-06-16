class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print(len(s))
        list1 = []
        length = 0
        sums = []
        if s == "":
            return 0
        elif s == " ":
            return 1
        elif len(s) == 1:
            return 1
        for s1 in s:
            if s1 not in list1:
                list1.append(s1)
                length += 1
            else:
                # length += 1
                sums.append(length)
                length = 1
        if len(sums) == 0:
            return len(s)
        return max(sums)
    
s1 = Solution()
print(s1.lengthOfLongestSubstring(s="au"))