# str = "If monkeys like bananas, then I must be a monkey!"
# # 1) print the positon for all instances of the word "monkey". Then create a new string where the word "monkey is replaced with the word alligator"
# finds the first instance
# finds the last instance
print str.find("monkey")
print str.rfind("monkey")

print str.replace("monkey", "alligator", 2)
#
# # 2) Print the min and max values in a list.
# x = [2,54,-2,7,12,98]
# print max(x)
# print min(x)
#
# # Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list.
# x = ["hello",2,54,-2,7,12,98,"world"]
# print x[0]
# print x[7]

# Start with a list. Sort it, then slice out all of the values that are negative, placing those values in a new list. Then add your new list into the original one at position 0.
y = []
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
x.remove(-2)
x.remove(-3)
print x
y.append(-2)
y.append(-3)
print y
