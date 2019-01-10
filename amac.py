import requests

url = 'http://gs.amac.org.cn/amac-infodisc/api/pof/fund?rand=0.46332793423028007&page=5185&size=20'

post_headers = {
'Content-Type': 'application/json;charset=UTF-8',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

r = requests.post(url, headers = post_headers)

print(r)