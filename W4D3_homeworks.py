# Codewars question 1 (https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c):
# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
def max_sequence(array):
    max = 0 
    current = 0
    if array == []:
        return 0
    for num in array:
        current += num
        if current < 0:
            current = 0
        if current > max:
            max = current
    return max

# The time complexity of my code is O(n), where n is the length of the input array
# because the number of operations scales linearly with the size of the input array.
# Because this question required a maximum sum of an array so the function need to go through each elements
# in an array, it is impossible to change the time complexity to O(1)

# Codewars question 2: https://www.codewars.com/kata/56606694ec01347ce800001b

def is_triangle(a, b, c):
    x = max(a,b,c)
    if x == a:
        if b + c > a:
            return True
        else:
            return False
    if x == b:
        if a + c > b:
            return True
        else:
            return False
    if x == c:
        if a + b > c:
            return True
        else:
            return False

# For this solution, the time complexity is O(1). The time complexity of your `is_triangle` algorithm is O(1).
# The algorithm consists of a series of conditional statements that compare the input values `a`, `b`, and
# `c` to find the maximum value `x`. These comparisons take constant time.

# Codewars question 3: https://www.codewars.com/kata/52e88b39ffb6ac53a400022e
import ipaddress
def int32_to_ip(int32):
    return str(ipaddress.ip_address(int32))
# For this solution, I imported the built-in function ipaddress to help me convert int32 to IPv4. The time
# complexity is O(1)


