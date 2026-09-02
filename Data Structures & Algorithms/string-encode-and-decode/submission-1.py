class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(string)}_{string}" for string in strs])

    def decode(self, s: str) -> List[str]:
        # I don't know re but that would have been the best way
        strs = []

        read = 0

        while read < len(s):
            for i in range(read, len(s)):
                if s[i] == "_":
                    # length before the waste character
                    length = int(s[read: i])

                    # eliminating the waste character
                    i += 1
                    strs.append(s[i: i + length])

                    # updating length after what was read
                    read = i + length

                    break

        return strs

