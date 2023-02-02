from random import randint
#列表推导式
#[表达式for 临时 in 迭代对象if]
print([i for i in range(10)]) #
print([i+1 for i in range(10)])
print(["学生"+str(i) for i in range(10)])
ls =[randint(40,100) for i in range(10)]
print(ls)

print("大于60")
print([i for i in ls if i >60])
print("筛选偶数")
print([v for v in ls if v%2==0])