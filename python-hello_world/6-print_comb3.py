#Write a program that prints numbers from 0 to 99
for i in range(10):
    for j in range(10):
        if(i==j):
            print("")
        else:
            print("{}{}" .format(i,j) , end=", ")
