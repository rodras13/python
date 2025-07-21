# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

x = 1234321

def is_palindrome(interger):
  int_str = str(interger)
  for i in range(len(int_str)):
    if int_str[i] != int_str[len(int_str) - (i + 1)]:
      return "false"
  return "true"

print(is_palindrome(x))

# ✅ Reolved in 16ms