class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        roman = { "I": 1, "V": 5, "X": 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000} #Writing Dictionary to define the Integer values for Roman numbers
        for i, c in enumerate(s):
            if (c == "I" and len(s)>i+1 and s[i+1] in ["V", "X"]) or (c == "X" and len(s)>i+1 and s[i+1] in ["L", "C"]) or (c =="C" and len(s)>i+1 and s[i+1] in ["D", "M"]) :
                val=-roman[s[i]]
                
            else:
                val = roman[s[i]]
            sum=sum+val 
        return sum
            
                
