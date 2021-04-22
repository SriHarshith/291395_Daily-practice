inp = input("Enter the input ")

if(inp == "0" ):
    print("It is a zero")
    exit()

try:
    if inp.isdigit() or int(inp):
        print("It is an integer")
except:
    try:
        if float(inp):
            print("It is a float")
    except:
        try:
            if complex(inp):
                print("It is a complex number")
        except:
            if inp.isalpha() or str(inp):
                print("It is a string")

