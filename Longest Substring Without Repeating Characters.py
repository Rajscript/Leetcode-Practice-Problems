class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        new=''
        old=''
        while r<len(s):
            if s[r] not in new:
                new= new+s[r]
                r+=1
            elif s[r] in new:
                new =new[1::]
                l+=1
            if len(old)<len(new):
                old=new
        return len(old)           
