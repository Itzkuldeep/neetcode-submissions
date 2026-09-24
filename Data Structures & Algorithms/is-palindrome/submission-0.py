class Solution:
    def isPalindrome(self, s: str) -> bool:
        # newStr = ""
        # for c in s:
        #     if c.isalnum():
        #         newStr += c.lower()
        # return newStr == newStr[::-1]
        i, j = 0, (len(s)-1)
        while i<j:
            while i<j and not self.alphanum(s[i]):
                i += 1
            while j > i and not self.alphanum(s[j]):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i,j = i+1, j-1
        return True

    def alphanum(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))