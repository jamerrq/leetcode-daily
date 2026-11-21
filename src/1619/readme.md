# [1619. Mean of Array After Removing Some Elements](https://leetcode.com/problems/mean-of-array-after-removing-some-elements/description)

**Level**: <span style="color:cyan">Easy</span>

Given an integer array `arr`, return *the mean of the remaining integers after removing the smallest `5%` and the largest `5%` of the elements.*

Answers within `10^-5` of the **actual answer** will be considered accepted.

## Examples

### Example 1:

`Input: arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]`

`Output: 2.00000`

#### Explanation:

After erasing the minimum and the maximum values of this array, all elements are equal to 2, so the mean is 2.

### Example 2:

`Input: arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]`

`Output: 4.00000`

### Example 3:

`Input: arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]`

`Output: 4.77778`

## Constraints

- `20 <= arr.length <= 1000`
- `arr.length`**** **is a multiple** of `20`.
- `0 <= arr[i] <= 10^5`

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

double trimMean(int* arr, int arrSize) {
    // mergeSort(arr, 0, arrSize - 1);
    int five_percent = arrSize * 5 / 100;
    double sum = 0;
    for (int i = five_percent; i < arrSize - five_percent; ++i)
        sum += arr[i];
    double mean = sum / (arrSize - five_percent * 2);
    return mean;
}
```

## Runtime
1 ms | Beats 73.53% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory
8.88 MB | Beats 70.59% ![clapping_hands](../../lib/clapping_hands.svg)

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/mean-of-array-after-removing-some-elements/description)
