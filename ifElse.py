n = int(input())

for x in range(1, n):
    if x % 2 == 0:
        continue
    elif x % 3 == 0 and x % 5 == 0:
        print("Hello World")
    elif x % 3 == 0:
        print("Hello")
    elif x % 5 == 0:
        print("World")
    else:
        print(x)
