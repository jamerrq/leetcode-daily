// gcc -std=c17 -Wall -Wextra -O2 main.c -o /tmp/3041

#include <stdio.h>

void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    int L[n1], R[n2];

    for (int i = 0; i < n1; i++) L[i] = arr[left + i];

    for (int j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j])
            arr[k++] = L[i++];
        else
            arr[k++] = R[j++];
    }

    while (i < n1) arr[k++] = L[i++];

    while (j < n2) arr[k++] = R[j++];
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
        if (dp[num] > ans)
            ans = dp[num];
        if (dp[num + 1] > ans)
            ans = dp[num + 1];
    }
    return ans;
}
