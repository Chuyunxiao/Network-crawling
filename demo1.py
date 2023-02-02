# 列表 list
hero_list = ["牛","牛蛙",6,6.66,[7,77]]
print(hero_list)
# 访问 (index从0开始)
print(hero_list[1])
print(hero_list[4])
#修改
hero_list[0] = "牛牛"
print(hero_list[0])
#增加
hero_list.append("芜湖") #末尾追加
print(hero_list)
#删除(整个数组)
# del hero_list
# print (hero_list)
del hero_list[1]
del hero_list[1]
print(hero_list)
