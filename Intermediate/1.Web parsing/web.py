from selenium import webdriver
from bs4 import BeautifulSoup
import time
url=input("enter the url from chrome:")
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)
tag=input("enter tag need to be parsed from url:")
soup = BeautifulSoup(driver.page_source, "html.parser")
title=soup.find_all(tag)
a=[]
for t in title:
    a.append(t.text.strip())
if a:
    print(f"after finding all tag {tag} in this url")
    for i in a:
        print(i)
else:
    print("There is no tag {tag} in this url")   

driver.quit()
