import os
import pprint

x = dir(os)


# pprint.pprint(x)

# print(*x, sep="\t")




dic = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10}

print(f"\n\ndic: {dic} \n\n")
print(dic)



list = [1,2,4,5,6]
print(list) #prints [1,2,4,5,6]

print(*list) #prints 1 2 4 5 6 :: unpacking the list

print(**dic)
