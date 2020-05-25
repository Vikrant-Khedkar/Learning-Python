from random import randint

l = []
d = {}
a = input("Press y/n :\t")
i = 0

while a == "y":
    name = input("Enter name:\t")
    n = randint(0, 100)
    if n in l == True:
        continue
    l.append(n)
    d[n] = name
    if i == 0:
        with open("Token_list.txt", mode='w') as f:
            f.write("Token_list\n")
            f.write("\n Name:\t" + name)
            f.write("\n Token:\t{}".format(n))
            f.write("\n")

    else:
        with open("Token_list.txt", mode='a') as f:
            f.write("\n Name:\t" + name)
            f.write("\n Token:\t{}".format(n))
            f.write("\n")

    i = i + 1

    a = input("Press y/n :\t ")
a = input("Press y/n :\t ")
while  a =="y":

    key = int(input("Enter key"))
    print(d[key])
    a = input("Press y/n :\t ")

print(d)
input(".....Thanks for using.....")	





