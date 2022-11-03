"""

---
MEDIUM
7. Reverse Integer
---


Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1

"""

## Solution 1
import math
class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        orig_x = x
        x = abs(x)
        while x > 0:
            num = num * 10 + x % 10
            x = x // 10
        num = int(math.copysign(num, orig_x))
        if -(2 ** 31) <= num <= 2**31 - 1:
            return num
        return 0


## Solution 2
class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            num = int(str(x)[::-1])
        else:
            num = int(str(x * -1)[::-1]) * -1
        
        if -(2**31) <= num <= 2**31 - 1:
            return num
        return 0