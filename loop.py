# for i in range (0, 50, 2 ):
#     print(i)

list1=[12,3,4,21,3,5,23,6,7,5,4,3.5,4.2,4]
for i in(list1):
    if i/2==0:
        print(i," is even")
    else:
        print(i," is odd")


x=0
while x<=50:
    print(x)
    x+=2


list1 = [12, 3, 4, 21, 3, 5, 23, 6, 7, 5, 4, 3.5, 4.2, 4]
i = 0
while i <len(list1):
    if list1[i] % 2 == 0:
        print(list1[i], "is even")
    else:
        print(list1[i], "is odd")
    i += 1



# i = 0
# while i < 5:
#     j = 0
#     while j <= i+1:
#         print("*", end="")
#         j=j+1
#     print("")
#     i=i+1
for x in range (5):
    for y in range (x+1):
        print("*", end = " ")
    print()
for i in range(5,0,-1):
    for j in range(i-1):
        print("*", end = " ")
    print()
