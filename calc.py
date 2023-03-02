# # Enter the first number:

# print ("Enter the first number: ", end = "")
# x_input = input()
# x = int(x_input)

# print("The first number is: ", x)

# y = int(input('Enter the second number: '))

# print("The second number is: ", y)

# operation = input("What is the operation? ")

# if operation == "+":
#     result = x +y
#     print("The result is: ", result)
# elif operation == "-":
#     result = x - y
#     print("The result is: ", result)
# else:
#     print("This calculator can only add or substract.")


    #Manipulating lists

numbers = input("Enter three numbers: ")
split_numbers = numbers.split(",")
print (split_numbers)

n1= int(split_numbers[0].strip())
print(n1)