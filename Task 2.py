list1 = [i for i in range(1,11)]

list2 = list1[0:5]
list3 = list2.copy()
list2.reverse()

print("Original list:", list1)
print("Extracted first 5 elements:", list2)
print("Reversed extracted elements:", list3)
