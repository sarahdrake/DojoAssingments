# 1a) Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use an array to do this exercise
for num in range(0,1001):
    if num % 2 != 0:
        print num
# 1b) Create another program that prints all the multiples of 5 from 5 to 1,000,000.
for num in range(5,1000001):
    if num % 5 == 0:
        print num
# 2) Create a program that prints the sum of all the values in the list.
list = [1, 2, 5, 10, 255, 3]
sum = 0
for element in list:
    sum += element
    print sum
# 3) Create a program that prints the average of the values in the list.
a = [1, 2, 5, 10, 255, 3]
print sum(a)/len(a)

# or
a = [1, 2, 5, 10, 255, 3]
sum = 0
for num in a:
    sum+= num
    avg = sum / len(a)
    print avg
