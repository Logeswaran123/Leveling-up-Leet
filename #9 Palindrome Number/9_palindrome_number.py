"""

---
EASY
9. Palindrome Number
---

Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?

"""

## Solution 1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        right_pointer = len(x) - 1
        for left_pointer in range(len(x)//2):
            if x[left_pointer] != x[right_pointer]:
                return False
            right_pointer -= 1
        return True


## Solution 2
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]


## Solution 3
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num_digits = int(math.log10(x)) + 1 if x > 0 else 1
        for i in range(num_digits // 2):
            num1 = x // math.pow(10, num_digits - i-1) % 10
            num2 = x % math.pow(10, i+1) // math.pow(10, i)
            if num1 != num2:
                return False
        return True

## Solution 4
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = 0
        orig_x = x
        while x>0:
            num = num * 10 + x % 10
            x = x // 10
        return num == orig_x

## Solution 5
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x>0 and x%10 == 0):
            return False
        num = 0
        while x > num:
            num = num * 10 + x % 10
            x = x // 10
        return (num//10 == x) or (num == x)