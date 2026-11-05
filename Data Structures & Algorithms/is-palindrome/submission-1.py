class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Preprocessing
        clean_s = s.replace(" ", "").lower()
        clean_s = ''.join([char for char in clean_s if char.isalnum()])
        print(clean_s)

        # Algorithm
        i = 0
        j = len(clean_s) - 1
        while i < j:
            if clean_s[i] == clean_s[j]:
                i = i + 1
                j = j - 1
            else:
                return False

        return True