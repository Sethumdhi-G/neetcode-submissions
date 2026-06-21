class Solution:
    def isPalindrome(self, s: str) -> bool:
        line =''
        for c in s:
            if c.isalnum():
                line += c.lower()

        return line == line [::-1]