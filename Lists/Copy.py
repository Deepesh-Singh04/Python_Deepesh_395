a = [int(x) for x in input("Enter some numbers: ").split()]
b = a [:]
c = a.copy()
d = list(a)
print("Original List:", a)
print("Copied List using slicing:", b)
print("Copied List using copy():", c)
print("Copied List using list():", d)