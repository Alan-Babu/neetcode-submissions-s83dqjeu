class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned+=char
            print(cleaned)
        return cleaned.lower() == cleaned.lower()[::-1]