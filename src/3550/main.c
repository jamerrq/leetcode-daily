static int digitsSum(int num) {
    int sum = 0;
    while (num > 0) {
        sum += num % 10;
        num /= 10;
    }
    return sum;
}

int smallestIndex(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; ++i) {
        if (digitsSum(nums[i]) == i) {
            return i;
        }
    }
    return -1;
}