class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d = {}
        for i in s:
            if i in s_d:
                s_d[i] += 1
            else:
                s_d[i] = 1
        t_d = {}
        for i in t:
            if i in t_d:
                t_d[i] +=1
            else:
                t_d[i] = 1
        if s_d == t_d:
            return True
        else:
            return False

