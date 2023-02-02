#字典 dictionary
#dict
#key -val
hero_info = {"name":"鲁班七号","grade":14,"skill":"无敌鲨鱼炮"}
print(hero_info)
print(type(hero_info))
#访问 通过key 访问 value
print(hero_info["name"])
print(hero_info["skill"])
#print(hero_info["money"]) #keyError :'money'
print(hero_info.get("skill"))
print(hero_info.get("money"))
print(hero_info.get("money",200))

#修改
hero_info["name"] = "小卤蛋"
print(hero_info)
#增加
hero_info["money"] = 2000
print(hero_info)
#删除
del hero_info["skill"]
print(hero_info)