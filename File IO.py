a = None
i = 0
while i <= 5:
    if i == 0:
        with open("myfile.txt", mode='w') as f:
            a = input("Enter")
            f.write(a)
            i = i + 1



    else:
        with open("myfile.txt", mode='a') as f:
            a = input("Enter")
            f.write("\n" + a)
            i = i + 1

with open("myfile.txt", mode='r') as f:
    print(f.read())
    input("")
