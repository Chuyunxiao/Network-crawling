from random import randint # 从random库取出randint
#[0,1,2,...,9]
list=[]
for i in range(10):
    list.append(i)
print(list)
print(randint(40,100))

list_2=[]
for i in range(30):
    num = randint(40,100)
    list_2.append(num)
print(list_2)

#遍历 取出
list_3=[]
for num in list_2:
    if num > 60:
        list_3.append(num)
print(list_3)

#筛选偶数
list_4=[]
for num in list_2:
    if num%2 == 0:
        list_4.append(num)
print(list_4)