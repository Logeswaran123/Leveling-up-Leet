"""

---
MEDIUM
12. Integer to Roman
---

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

 

Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= num <= 3999


"""

## Solution 1
class Solution(object):
    def DigitToRoman(self, digit, first_char, second_char, third_char):
        roman_num = ""
        if digit == 1:
            roman_num += first_char
        elif digit == 4:
            roman_num += first_char + second_char
        elif digit == 5:
            roman_num += second_char
        elif digit == 9:
            roman_num += first_char + third_char
        elif 1 < digit < 4:
            roman_num += first_char * digit
        else: # 5 < digit < 9:
            roman_num += second_char + (first_char * (digit - 5))
        return roman_num

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_num = ""
        digit_place = 1

        while num > 0:
            digit = num % 10
            num = num // 10
            if digit == 0:
                digit_place += 1
                continue
            if digit_place == 1:
                roman_num = self.DigitToRoman(digit, "I", "V", "X") + roman_num
            if digit_place == 2:
                roman_num = self.DigitToRoman(digit, "X", "L", "C") + roman_num
            if digit_place == 3:
                roman_num = self.DigitToRoman(digit, "C", "D", "M") + roman_num
            if digit_place == 4:
                roman_num = "M" * digit + roman_num
            digit_place += 1
        return roman_num  