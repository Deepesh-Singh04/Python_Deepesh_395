a = [[int(x) for x in input("Enter multiple values separated by space: ").split()] + [str(x) for x in input("Enter more values separated by space: ").split()], [int(x) for x in input("Enter additional values separated by space: ").split()]]
print("You entered:", a)
print("List elements:")
for sublist in a:
    for i in sublist:
        print(i)