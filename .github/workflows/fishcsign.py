import requests
import sys

url = href="https://fishc.com.cn/plugin.php?id=k_misign:sign&operation=qiandao&formhash=1af23681&format=empty"
headers={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "Cookie": sys.argv[1]
}
response = requests.get(url=url,headers=headers)

if "今日已签" in response.text:
    print("已签到")
else:
    print("签到失败")
