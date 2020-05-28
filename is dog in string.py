s = "ok"
i = 0


def isdog():
    x=input("Enter a String:")
    return (x)


while i < 1000:

    if s != "close":
        s = isdog()
        if "Dog" in s :
           print("Found")
        else:
           print("Not found")
           i=i+1
    else:
        break
input("")



