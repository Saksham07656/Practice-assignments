def climb(n, dp):
    if n == 0 or n == 1:
        return 1

    if dp[n] != -1:
        return dp[n]

    dp[n] = climb(n - 1, dp) + climb(n - 2, dp)

    return dp[n]


n = int(input("Enter number of steps: "))

dp = [-1] * (n + 1)

print("Number of ways:", climb(n, dp))