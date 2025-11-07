class Solution:
    def isValid(self,s):
        d= dict(('()', '[]', '{}'))
        l = []
        for i in s:
            if i in '([{':
                l.append(i)
            elif len(l) == 0 or i != d[l.pop()]:
                return False
        return len(l) == 0