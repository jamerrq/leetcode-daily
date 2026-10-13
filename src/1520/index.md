# [1520. Maximum Number of Non-Overlapping Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/description)

**Level**: <span style="color:red">Hard</span>

Given a string `s` of lowercase letters, you need to find the maximum number of non-empty substrings of `s` that meet the following conditions:

1. The substrings do not overlap, that is for any two substrings `s[i..j]` and `s[x..y]`, either `j < x` or `i > y` is true.
2. A substring that contains a certain character `c` must also contain all occurrences of `c`.

Find *the maximum number of substrings that meet the above conditions*. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in **any order**.

## Examples

### Example 1:

`Input: s = "adefaddaccc"`

`Output: ["e","f","ccc"]`

#### Explanation

The following are all the possible substrings that meet the conditions:

`["adefaddaccc", "adefadda", "ef", "e", "f", "ccc"]`

If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.

### Example 2:

`Input: s = "abbaccd"`

`Output: ["d","bb","cc"]`

#### Explanation

Notice that while the set of substrings `["d","abba","cc"]` also has length 3, it's considered incorrect since it has larger total length.

## Constraints

- `1 <= s.length <= 10^5`
- `s` contains only lowercase English letters.

## My Solution
[index.py](./index.py)

```python
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
```

## Brief Explanation

This was highly induced by the hints.

We first start by saving the first and last appearance of each letter in the string, this would create an interval for each character. Then we iterate over these intervals to expand them if they have other characters inside whose range starts before or finish later.

With these processed intervals, we choose greedily starting from the one that finish first and then only choosing the ones that start after the current interval ends.

## Runtime
887 ms | Beats 22.65%

## Memory
20.33 MB | Beats 57.22% ![clapping_hands](../../lib/clapping_hands.svg)

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/description)
