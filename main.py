'''
Given a list of integers, determine whether the sum of its elements is odd or even.

Give your answer as a string matching "odd" or "even".

If the input array is empty consider it as: [0] (array with a zero).
'''
#----------------- 1 ------------------------------
def odd_or_even(arr):
    total = 0
    for x in arr:
        total += x
    if total % 2 == 0:
        return "even"
    else:
        return "odd"

#Better answer:
def oddOrEven(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'



#------------------- 2 ----------------------------------

'''
Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.

For example:

solution([1,2,3,10,5]) # should return [1,2,3,5,10]
solution(None) # should return []
'''
def solution(nums):
    return [] if nums == None else sorted(nums)

#Better answer:
def solution(nums):
    return sorted(nums) if nums else []

#------------------- 3 ----------------------------------

'''
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.
'''

import math
def find_next_square(sq):
    if math.sqrt(sq).is_integer() == False:
        return -1
    else:
        return (math.sqrt(sq) + 1) ** 2

#------------------- 4 ----------------------------------
