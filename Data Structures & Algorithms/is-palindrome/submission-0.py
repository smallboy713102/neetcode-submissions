class Solution:
    def alphaNum(self, c):
        return (
            'a' <= c <= 'z' or
            '0' <= c <= '9'
        )

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = list(s)
        s = [x for x in s if self.alphaNum(x) == True]

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False

        return True