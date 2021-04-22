set1 = {1,2,4,5,6,5}

n = int(input("Enter number of elements on set2 : "))
list2 =[]
for i in range(0, n):
    ele = int(input())
    list2.append(ele)

set2 = set(list2)

print("\nSet1: ",set1)
print("Set2: ",set2)

print("\nMaximum of set1 is: ",max(set1)) #maximum value
print("Maximum of set2 is: ",max(set2))

print("\nMinimum of set1 is: ",min(set1)) #minimum value
print("Minimum of set2 is: ",min(set2))