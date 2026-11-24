import random

# Generate 20 random correct answer counts
a = [random.randint(1, 20) for i in range(20)]

print("Answer counts:", a)

# Sorted version for comparison
print("Sorted:", sorted(a))

# DP for Longest Increasing Subsequence
dp = [1] * 20

for i in range(20):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print("Longest improvement streak:", max(dp))