hero_info = {"name":"鲁班七号","grade":14,"skill":"无敌鲨鱼炮"}
#元素个数
print(len(hero_info))
#获取所有键
print(list(hero_info.keys()))
#获取所有值
print(list(hero_info.values()))
#获取所有键值
print(list(hero_info.items()))

#
for k , v in hero_info.items():
    print(k,'--->',v)
#词频统计
text = "the club in the best to find a lover so the bar is where I go"
text_ls = text.split()
print(text_ls)
counts = {}
#{"the":3,"club":1}

for word in text_ls:
    #counts[word] = counts[word]+1
    counts[word] = counts.get(word,0)+1
print(counts)