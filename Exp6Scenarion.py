import random

# Generate 2D matrix of travel times
n = 4
matrix = [[random.randint(1, 9) for j in range(n)] for i in range(n)]

print("Travel Time Matrix:")
for row in matrix:
    print(row)

# DP table
dp = [[0] * n for i in range(n)]

dp[0][0] = matrix[0][0]

# First row
for j in range(1, n):
    dp[0][j] = dp[0][j-1] + matrix[0][j]

# First column
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + matrix[i][0]

# Minimum path
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i][j-1])

print("Minimum delivery time:", dp[n-1][n-1])