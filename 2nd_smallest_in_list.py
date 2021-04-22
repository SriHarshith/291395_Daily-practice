list1 = []
list2 = [13,5,6,8,13,65,3]

n = int(input("Enter number of elements on list1 : "))

for i in range(0, n):
    ele = int(input())
    list1.append(ele)

print("\nList1 is {}".format(list1))
print("List2 is {}".format(list2))

list1.sort()
list2.sort()

print("\nSecond Smallest of list1 is :",list1[1])
print("Second Smallest of list2 is :",list2[1])