import requests

heads = {
    "User-Ageng":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
url = "http://tonkiang.us"
key = "凤凰"
query_url = url + "?" + key
resp = requests.post(query_url,headers=heads)
print(resp.text)