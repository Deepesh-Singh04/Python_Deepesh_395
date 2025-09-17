a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Before swapping: ")
print("First number:", a)   
print("Second number:", b)
# Swapping using XOR bitwise operator
a = a^b
b = a^b
a = a^b
print("After swapping: ")
print("First number:", a)
print("Second number:", b)