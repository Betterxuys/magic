import requests

url = 'https://api.github.com/search/repositories?q=stars%3A'
base = 100
step = base/100
for i in range(base,base*10,step):
    r = requests.get(url+str(i)+".."+str(i+step))
    repostories = r.json()
    num = repostories["total_count"]
    print(str(i)+":"+str(num)+"\n")