import requests
from selenium import webdriver

url = 'https://www.aqistudy.cn/historydata/daydata.php?city=%E6%9D%AD%E5%B7%9E&month=2018-03'

# res = requests.get(url)
# print(res.text)
driver = webdriver.Chrome()
driver.get(url)
print(driver.page_source)

