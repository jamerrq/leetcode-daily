// gcc -std=c17 -Wall -Wextra -O2 main.c -o /tmp/4111

int countConsistent(int* nums, int numsSize) {
    int ans = 0;
    for (int i = 0; i < numsSize; ++i) {
        unsigned bit = (unsigned)nums[i];
        int min = nums[i];
        ans++;
        for (int j = i + 1; j < numsSize; ++j) {
            bit &= (unsigned)nums[j];
            min = min < nums[j] ? min : nums[j];
            if ((int)bit == min)
                ans++;
        }
    }
    return ans;
}