class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        start, end = {}, {}
        keys = set()
        for i, char in enumerate(s):
            keys.add(char)
            index = start.get(char)
            if index is None:
                start[char] = i
            end[char] = i
        #
        intervals = []
        for key in keys:
            key_start = start[key]
            key_end = end[key]
            #
            i = key_start + 1
            j = key_end
            while i < j:
                curr_start = start[s[i]]
                curr_end = end[s[i]]
                if key_start <= curr_start and curr_end <= key_end:
                    i += 1
                    continue
                key_start = min(key_start, curr_start)
                key_end = max(key_end, curr_end)
                i = key_start
                j = key_end
            interval = (key_start, key_end)
            intervals.append(interval)
        intervals.sort(key=lambda x: (x[1], x[0]))
        curr_interval = intervals.pop(0)
        ans = []
        def add_interval(interval):
            left, right = interval
            ans.append(s[left:right+1])
        while intervals:
            interval = intervals.pop(0)
            if interval[0] > curr_interval[1]:
                add_interval(curr_interval)
                curr_interval = interval
        add_interval(curr_interval)
        return ans