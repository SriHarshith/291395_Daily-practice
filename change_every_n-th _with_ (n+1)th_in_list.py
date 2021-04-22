#list_inp = [2,4,56,78,3,9] #list with even no. of elements

list_inp = [2,4,56,78,3,9,12]  # list with odd no. of elements


odd = None

if (len(list_inp) % 2 ==0):
    list1 = list_inp
else:
    list1 = list_inp[:-1]
    odd = True

#swap i and i+1 th elements
for i in range(0, len(list1), 2):
    list1[i], list1[i + 1] = list1[i + 1], list1[i]

if(not odd):
    print(list1)
else:
    list1.append(list_inp[-1])
    print(list1)
