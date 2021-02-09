from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


code_list = []
code = ""
driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
driver.get("https://care.srmist.edu.in/srmstudentskill/student/solve/1820120")
n = input("Enter confirm ")
print(n)
content = driver.page_source
soup = BeautifulSoup(content, features="html5lib")
for a in soup.findAll('pre', attrs={'role':'presentation'}):
    title_sub = a.findAll('span', attrs={'role':'presentation'})
    for i in title_sub:
        code_list.append(i.get_text().strip())
print(code_list)
print(len(code_list))
for l in code_list:
    code = code + l
    code = code + "(br)"
code = code + "(end)"
print(code)
code_main = []
code = list(code.split('(end)'))
print(code)
code.pop(1)
code_main.append(code)
print(code_main)