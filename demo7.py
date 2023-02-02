#集合 set 输出无序,不重复的
hero_info = {"name":"鲁班七号","grade":14,"skill":"无敌鲨鱼炮"}
a = {"haha",222,333}
print(a)
print(type(a)) #<class 'set'>
#print(a[0]) typeerror:'set' object does not support indexing

#不重复
a.add(666)
a.add(666)
a.add(666)
print(a)
