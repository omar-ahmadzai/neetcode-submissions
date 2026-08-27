class Solution:
    def groupAnagrams(self, array: List[str]) -> List[List[str]]:
        anagram_dicts = {}
        length = len(array)

        for index, value in enumerate(array):
            anagram_dicts[index] = {i: value.count(i) for i in set(value)}

        pairs = []
        checked = []

        for i in range(length):
            if i in checked:
                continue
            pairs.append([array[i]])
            checked.append(i)
            for j in range(i + 1, length):
                if j in checked:
                    continue
                if anagram_dicts.get(i) == anagram_dicts.get(j):
                    pairs[-1].append(array[j])
                    checked.append(j)

        return pairs