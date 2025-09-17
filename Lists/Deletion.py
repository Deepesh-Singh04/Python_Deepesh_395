a = [int(i) for i in input("Enter multiple values separated by space: ").split()]
print("You entered:", a)
value_to_remove = int(input("Enter a value to remove: "))
if value_to_remove in a:
    a.remove(value_to_remove)
    print("List after removal:", a)
else:
    print("Value not found in the list.")