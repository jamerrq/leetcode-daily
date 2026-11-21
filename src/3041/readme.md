# [3041. Maximize Consecutive Elements in an Array After Modification](https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/description)

**Level**: <span style="color:red">Hard</span>

You are given a **0-indexed** array `nums` consisting of **positive** integers.

Initially, you can increase the value of **any** element in the array by **at most** `1`.

After that, you need to select **one or more** elements from the final array such that those elements are **consecutive** when sorted in increasing order. For example, the elements `[3, 4, 5]` are consecutive while `[3, 4, 6]` and `[1, 1, 2, 3]` are not.

Return *the **maximum** number of elements that you can select*.

## Examples

### Example 1:

`Input: nums = [2,1,5,1,1]`

`Output: 3`

#### Explanation:

- We can increase the elements at indices 0 and 3. The resulting array is nums = [3,1,5,2,1].
- We select the elements [3,1,5,2,1] and we sort them to obtain [1,2,3], which are consecutive.
- It can be shown that we cannot select more than 3 consecutive elements.

### Example 2:

`Input: nums = [1,4,7,10]`

`Output: 1`

#### Explanation:

The maximum consecutive elements that we can select is 1.

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^6`

## My Solution
[main.c](./main.c)

```C
#include <stdio.h>

void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    int L[n1], R[n2];

    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];

    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j])
            arr[k++] = L[i++];
        else
            arr[k++] = R[j++];
    }

    while (i < n1)
        arr[k++] = L[i++];

    while (j < n2)
        arr[k++] = R[j++];
}

void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        merge(arr, left, mid, right);
    }
}

int maxSelectedElements(int* nums, int numsSize) {
    mergeSort(nums, 0, numsSize - 1);
    int dp[(int)1e6 + 1] = {0};
    int ans = 1;
    for (int i = 0; i < numsSize; ++i) {
        int num = nums[i];
        dp[num + 1] = dp[num] + 1;
        dp[num] = dp[num - 1] + 1;
        if (dp[num] > ans) ans = dp[num];
        if (dp[num + 1] > ans) ans = dp[num + 1];
    }
    return ans;
}
```

## Runtime
149 ms | Beats 100% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory
18.26 MB | Beats 100% ![clapping_hands](../../lib/clapping_hands.svg)

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/description)
