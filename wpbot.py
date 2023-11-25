from selenium import webdriver
import time
from selenium.webdriver.common.by import By
brow=webdriver.Chrome(executable_path='chromedriver.exe')

brow.get('http://web.whatsapp.com')
input("Enter if allright")
user=input('Victim friend >')
num=int(input('Message count >'))
msg=input('Default msg:[NUMBER], you can add msg after it >')

X=brow.find_element(By.XPATH, '//span[@title="{}"]'.format(user))
X.click()

msg_box=brow.find_element(By.XPATH, '//div[@spellcheck="true"]')
for x in range(1,num+1):
    msg_box.click()
    msg_box.send_keys(str(x)+msg)
    brow.find_element(By.XPATH, '//span[@data-icon="send"]').click()

input('Ended')

