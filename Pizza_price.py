slices = int(input("Enter number of pizza slices"))
price = 123.00
price_even = 120.00

if slices % 2 ==0:
    total = slices * price_even
else:
    total = slices * price

print("Total Amount is " + str(total))
