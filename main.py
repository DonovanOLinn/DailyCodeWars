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