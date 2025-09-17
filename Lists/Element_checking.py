a = [[int(i) for i in input("Enter multiple values separated by space: ").split()],[str(i) for i in input("Enter more values separated by space: ").split()]]
print("You entered:", a)
if 7 in a[0]:
    print("7 is present in the first sublist.")
else:   
    print("7 is not present in the first sublist.")