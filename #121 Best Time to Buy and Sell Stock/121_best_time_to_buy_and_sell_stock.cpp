/*

---
EASY
121. Best Time to Buy and Sell Stock
---

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

*/

// Solution 1
// Sliding Window
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0, r = 1; // Left and right pointers
        int max_profit = 0;

        while (r < prices.size()) {
            if (prices[l] < prices[r]) {
                int profit = prices[r] - prices[l];
                max_profit = std::max(max_profit, profit);
                r++;
            } else {
                l = r;
                r++;
            }
        }

        return max_profit;
    }
};


// Solution 2
// Dynamic Programming
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_price = prices[0]; // Track the minimum price so far
        int max_profit = 0;       // Track the maximum profit

        for (int i = 1; i < prices.size(); ++i) {
            // Update the maximum profit
            max_profit = std::max(max_profit, prices[i] - min_price);
            // Update the minimum price
            min_price = std::min(min_price, prices[i]);
        }

        return max_profit;
    }
};