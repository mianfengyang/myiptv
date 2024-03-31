import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import re

url = "http://tonkiang.us/?s=%E7%BF%A1%E7%BF%A0%E5%8F%B0"
# 创建一个Chrome WebDriver实例
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_driver_path="/home/frank/bin/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(options=chrome_options,service=service)
# 使用WebDriver访问网页
driver.get(url)  # 将网址替换为你要访问的网页地址

#time.sleep(3)
# 获取网页内容
page_content = driver.page_source
page_content = page_content.split("\n")

for line in page_content:
    match = re.search(r".*m3u8", line)
    if match:
        print(line)
#print(page_conten)
# 关闭WebDriver
driver.quit()