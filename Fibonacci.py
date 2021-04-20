num = int(input())

def fibo(n):
    if n <= 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(0)
for x in range(num-1):
    print(fibo(x))