// gcc -std=c17 -Wall -Wextra -O2 main.c -o /tmp/3693

int climbStairs(int n, int* costs, int costsSize) {
    (void)costsSize;
    int dp[n + 1];
    dp[0] = 0;
    for (int i = 0; i < n; ++i) {
        // j - 1
        int option1 = costs[i] + 1 + dp[i];
        if (i < 1) {
            dp[i + 1] = option1;
            continue;
        }
        int option2 = costs[i] + 4 + dp[i - 1];
        if (i < 2) {
            int option = option1 < option2 ? option1 : option2;
            dp[i + 1] = option;
            continue;
        }
        int option3 = costs[i] + 9 + dp[i - 2];
        int option = option1 < option2 ? option1 : option2;
        option = option < option3 ? option : option3;
        dp[i + 1] = option;
    }
    return dp[n];
}