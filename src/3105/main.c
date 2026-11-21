// gcc -std=c17 -Wall -Wextra -O2 main.c -o /tmp/3105

int longestMonotonicSubarray(int* nums, int numsSize) {
    int longDec = 1, longInc = 1, currDec = 1, currInc = 1;
    int prev = nums[0];
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] > prev) {
            currInc++;
            currDec = 1;
            if (currInc > longInc)
                longInc = currInc;
        } else if (nums[i] < prev) {
            currDec++;
            currInc = 1;
            if (currDec > longDec)
                longDec = currDec;
        } else {
            currInc = 1;
            currDec = 1;
        }
        prev = nums[i];
    }
    return longInc > longDec ? longInc : longDec;
}
