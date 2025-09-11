Arr1 = input("Enter elements of first array separated by space: ").split()
Arr2 = input("Enter elements of second array separated by space: ").split()
while Arr1:
    i = Arr1.pop(0)
    j_index = 0
    while j_index < len(Arr2):
        j = Arr2[j_index]
        print(i, j)
        j_index += 1