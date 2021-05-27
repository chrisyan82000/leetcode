def findTheLongestSubstring(self, s: str) -> int:
        vowels={'a':1,'e':2,'i':4,'o':8,'u':16}
        n=0
        d={0:-1}
        res=0
        for i,ch in enumerate(s):
            if(ch in vowels):
                n^=vowels[ch]
            if(n not in d):
                d[n]=i
            else:
                res=max(res,i-d[n])
        return res
