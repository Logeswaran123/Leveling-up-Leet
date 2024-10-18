"""

---
MEDIUM
322. Coin Change
---

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

"""

## Solution 1
## Bottom-up Dynamic Programming
#
# Example:
# coins = [1, 2, 5]
# amount = 11
#
# - Initialize dp = [0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
# - dp[0] = 0 since 0 coins are needed for amount 0.
# - Loop through amounts from 1 to 11.
#
# For amount = 1:
# - Using coin 1, dp[1] = min(dp[1], 1 + dp[1 - 1]) = min(12, 1 + 0) = 1.
# - Coins 2 and 5 are greater than 1, so we skip them.
# - dp becomes [0, 1, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12].
#
# For amount = 2:
# - Using coin 1, dp[2] = min(dp[2], 1 + dp[2 - 1]) = min(12, 1 + 1) = 2.
# - Using coin 2, dp[2] = min(dp[2], 1 + dp[2 - 2]) = min(2, 1 + 0) = 1.
# - Coin 5 is greater than 2, so we skip it.
# - dp becomes [0, 1, 1, 12, 12, 12, 12, 12, 12, 12, 12, 12].
#
# Continue this for all amounts up to 11.
# For amount = 11, the minimum number of coins needed is 3 (using coins [5, 5, 1]).
# The final dp array becomes: [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3].
#
# Return dp[11] = 3.
#
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Set initial to some large value.
        # List of size (amount + 1) as we subtract from the amount value to construct dp cache.
        # dp[i] will store the minimum number of coins needed to make up amount 'i'.
        init = amount + 1
        dp = [init] * (amount + 1)
        dp[0] = 0   # When amount is zero, it take zero coins.

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    # Choose the minimum between the current value of dp[a] and 1 + dp[a - c].
                    # 1 + dp[a - c] means we are using one more coin (the current coin 'c')
                    # and adding it to the solution for amount 'a - c'.
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != init else -1


## Solution 2
## Top-down Dynamic Programming i.e. Memoization
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Memoization cache
        memo = {}

        def dp(remaining):
            # Base case: if remaining amount is 0, no coins are needed
            if remaining == 0:
                return 0
            # If the remaining amount is negative, it's an invalid case
            if remaining < 0:
                return float('inf')

            # If the result for this amount is already computed, return it from the memo
            if remaining in memo:
                return memo[remaining]

            # Initialize
            min_coins = float('inf')

            # Try every coin and recursively find the solution
            for coin in coins:
                result = dp(remaining - coin)
                if result != float('inf'):
                    min_coins = min(min_coins, result + 1)

            # Cache the result
            memo[remaining] = min_coins

            return memo[remaining]

        result = dp(amount)

        return result if result != float('inf') else -1
