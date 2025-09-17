a = [[int(i) for i in input("Enter multiple values separated by space: ").split()],[str(i) for i in input("Enter more values separated by space: ").split()]]
print("You entered:", a)
print("List elements at first index:", a[0])
print("List elements at second index:", a[1])
print("First element of the first sublist in reverse order:", a[0][-1::-1])
print("Second element of the second sublist in reverse order:", a[1][-1::-1])