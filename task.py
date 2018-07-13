import requests
import time

url = 'https://api.github.com/search/repositories?q=stars%3A'
base = 10000
step = int(base/10)
k = 0
for i in range(base,base*10,step):
    r = requests.get(url+str(i)+".."+str(i+step))
    repostories = r.json()
    num = repostories["total_count"]
    print(str(i)+":"+str(num))
    k+=1
    if(k==9):
        k=0
        time.sleep(60)
