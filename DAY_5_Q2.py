# Q2 : https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # converting the whole string to lowercase
        s = s.lower()
        # to remove all non alphanumeric we'll use the filter method and isalnum method of Python.
        s = ''.join(filter(str.isalnum, s))
        # if the original string is same as the reverse of it then it's a valid palindrome and we'll return True in that case otherwise return False
 
        if(s==s[::-1]):
            return True
        else:
            return False
