class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if self.count_letters(s) == self.count_letters(t):
            return True
        return False

    def count_letters(self, string: str):
        count = {}

        for letter in string:
            count[letter] = count.get(letter, 0) + 1
        
        return count