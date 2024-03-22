import os
import json
import requests

def export_file(srvUrl, file):
    try:
        header = {"Content-Type": "application/json;charset=UTF-8"}
        resp = requests.post(url=srvUrl, headers=header)
        print(resp)
        if resp.status_code != requests.codes.ok:
            return  # error!

        header = resp.headers
        name = header.get("Content-Disposition")  # 假设头中携带文件信息，可获取用于写文件
        print(name)

        with open(file, "wb") as conf:
            conf.write(resp.content)
    except Exception as ex:
        print(ex)