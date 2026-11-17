class Solution:
    def isValid(self, s: str) -> bool:
        #Brute force method --> parenthesis come in pairs. If the string is valid then remove all teh pairs of parenthesis until nothing is left, 
        #If after removing everything the string is empty, then there is a mathch, else its not a match 


        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        
        #True if s is empty else false
        return s == ''


        