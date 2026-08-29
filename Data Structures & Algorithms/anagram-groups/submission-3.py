class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for name in strs:
            count = self.count_letters(name)
            if count in groups:
                groups[count].append(name)
            else:
                groups[count] = [name]

        return list(groups.values())

    def count_letters(self, string: str):
        count = [0 for i in range(26)]

        for letter in string:
            count[97 - ord(letter)] += 1

        return tuple(count)
