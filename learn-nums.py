
def space():
    print("\n\n\n\n\n")


x = 1
y = 1.1009






a = x +y


print(a)


print (10/3)

print (10//3) #gives integer


print(10 % 3) #gives remainder


print(abs(-10))

print(round(10.123456789, 2)) #rounds to 2 decimal places




condition = True

pp = 'peter'

print(type(pp))
print(type(x))
print(type(y))

print(type(condition))


fruit = "apple"

print(fruit[2])

print(fruit[0:-1])  # prints from 0 to -1 index, which is the last character not included
print(fruit[1:])  # prints from 1 to all the way to end





age = 21;

# if age >=20:
#     message = "eligible"
# else:
#     message = "not eligible"
# print(message)


message = "eligible" if age >=20 else "Not eligible"

print(message)

for i in range(24,31): # 24 to 30
    print(i)

print("\n")
for i in range(24,34,3): # 24 to 30, interval of 3
    print(i)


for i in range(24,31):
    print("number is:", i +1, (i +1) * "_")


print("\n\n\n\n\n")

# For Else example
successful = False
for nu in range(3):
    print(f"attempt {nu}")
    if successful:
        print("successful")
        break
    else:
        print("not successful")
else:
    print("all attempts failed")



space()

for x in range(1,4+1):
    for y in range(1,6+1):
        print(f"x: {x}, y {y}")


for c in "hello": #string is iterable
    print(c)


for item in [1,4,5,11,66,5,00,9,980]:
    print(item)


stupid_column_names = ["order_id", "order_date", "order_amount", "customer_id", "customer_name"]


for a in stupid_column_names:
    print(f"{a} => {a.title().replace('_', ' ')}")


def plusnums(num1: int, num2: int) -> int:
    return(num1 + num2)


print(plusnums(1.1,.2))





file = open("requirements2.txt", "w")
file.write('we are one')
file.close()






fruits = ["apple", "banana", "cherry"]

# fruits.add("annanas")
fruits.append("orange")

fruits.remove("banana")  # removes first occurrence of banana
print(fruits)







print("http://localhost:81/index.html?namee=waqar".split('?')[1])