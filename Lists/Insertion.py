a = [int(i) for i in input("Enter multiple values separated by space: ").split()]
print("You entered:", a)
value_to_insert = int(input("Enter a value to insert: "))
a.append(value_to_insert)
print("List after insertion:", a)
index_to_insert = int(input("Enter the index to insert the value at: "))
value_to_insert = int(input("Enter a value to insert: "))
if 0 <= index_to_insert <= len(a):
    a.insert(index_to_insert, value_to_insert)
    print("List after insertion at index", index_to_insert, ":", a)