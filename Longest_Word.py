txt = input()

leng = 0

l = txt.split(" ")
for i in l:
    if len(i) > leng:
        leng = len(i)
        ind = i

print(ind)