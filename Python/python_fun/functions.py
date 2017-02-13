# # 1) Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.
# def odd_even(num):
#     for num in range(1,2001):
#         if num % 2 == 0:
#             print "Number is " + str(num) + ". This is an even number."
#         elif num % 2 != 0:
#             print "Number is " + str(num) + ". This is an odd number."
# # 2) Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
# def multiply(list,b):
#     result = []
#     for element in list:
#         element = element * b
#         result.append(element)
#     return result
# print(multiply([1,2,3,4],5))
#
# # or
def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b

# challenge) Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain as many ones as the number in the original list. Here's an example:
def layered_multiples(arr):
    array_new = []
    for i in range(len(arr)):
        array_new.append([1]*arr[i])
    return array_new
print layered_multiples(multiply([2,4,6,8],2))
