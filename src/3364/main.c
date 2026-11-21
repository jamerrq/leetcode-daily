// gcc -std=c17 -Wall -Wextra -O2 main.c -o /tmp/3364

int minimumSumSubarray(int* nums, int numsSize, int l, int r) {
    int ans = -1;
    for (int i = 0; i < numsSize; ++i) {
        int stop = numsSize < i + r ? numsSize : i + r;
        for (int j = i + l - 1; j < stop; ++j) {
            int curr_sum = 0;
            for (int index = i; index < j + 1; ++index) curr_sum += nums[index];
            if (curr_sum > 0) {
                ans = ans == -1 && curr_sum > 0 ? curr_sum : ans;
                ans = ans < curr_sum ? ans : curr_sum;
            }
        }
    }
    return ans;
}
