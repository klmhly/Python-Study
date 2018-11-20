class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match = {'(': ')', '[': ']', '{': '}'}
        stack = []
        lens = len(s)

        for i in range(lens):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if stack == []:
                    return False
                else:
                    top = stack[-1]
                    if s[i] != match[top]:
                        return False
                    else:
                        stack.pop()
        if stack == []:
            return True
        else:
            return False

test = Solution()
res = test.isValid('()')
print(res)