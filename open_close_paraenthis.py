open_brackets = ["(","{","["]
close_brackets = [")","}","]"]
d = {"(":")","{":"}","[":"]"}
stack = []
class Solution:
    def isValid(self, s: str) -> bool:
        for string in s:
            if string in open_brackets:
                stack.append(string)
            elif string in close_brackets:
                if len(stack)>0 and string == d[stack[-1]]:
                    stack.pop()
                    continue
                return False
                
        return not stack


s1 = Solution()
print(s1.isValid(s="][]"))