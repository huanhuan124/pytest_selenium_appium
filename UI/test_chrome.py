from selenium import webdriver
from selenium.webdriver.chrome.options import Options

option = Options()
option.debugger_address = "localhost:9222"
driver = webdriver.Chrome(options=option)
driver.get("https://weibo.com/newlogin?tabtype=weibo&gid=102803&url=https%3A%2F%2Fweibo.com%2F")

