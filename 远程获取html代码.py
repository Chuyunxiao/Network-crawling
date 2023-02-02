import requests
# pip install requests
url = ""
response = requests.get("https://www.baidu.com/")
print(response.status_code)  #ok 200
print(response.encoding)  #ISO-8859-1
response.encoding = 'utf-8'
print(response.encoding)  #utf-8

data = response.text
print(data)

# 存入本地
with open('baidu.html', mode='w', encoding='utf-8') as f:
    f.write(data)
