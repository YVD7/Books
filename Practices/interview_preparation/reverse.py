# Reverse Using while loop in python

# n = int(input('Please give a number: '))
# print("Before reverse your number is: %d" %n)
# reverse = 0
# while n != 0:
#     reverse = reverse * 10 + n % 10
#     n = (n//10)
# print("After reverse : %d" %reverse)

# Reverse Using String Slicing in Python

# num = int(input("Please give a number: "))
# print("Before reverse your number is: %d " %num)
# rev = int(str(num)[::-1])
# print("After reverse the number: ", rev)

# Reverse using Recursion 

# def reverse(num):
#     if num < 10:
#         return num
#     else:
#         return (num % 10) * 10 ** (len(str(num)) - 1) + reverse(num // 10)
    
# num = int(input("Please enter a number: "))
# print("Before reverse your number is : %d" %num)
# rev = reverse(num)
# print("After reverse the number: ", rev)