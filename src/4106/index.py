class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        n = len(s1)
        segments: list[list[str]] = []
        index = 0
        cs1, cs2 = "", ""
        while index < n:
            s1c, s2c = s1[index], s2[index]
            if s1c != s2c:
                cs1 += s1c
                cs2 += s2c
            else:
                if cs1:
                    segments.append([cs1, cs2])
                cs1 = ""
                cs2 = ""

            index += 1

        if cs1:
            segments.append([cs1, cs2])

        return segments
