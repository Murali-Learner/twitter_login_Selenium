from logging import log
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

userName=input('Enter UserName : ')
password=input('Enter Password : ')

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.implicitly_wait(3)
driver.get("https://twitter.com/LOGIN")
driver.maximize_window()

time.sleep(2)
print(driver.title)

username = driver.find_element_by_name('session[username_or_email]')
username.send_keys(userName)
# username.send_keys('saimura90943439')

passworD = driver.find_element_by_name('session[password]')
passworD.send_keys(password)
# passworD.send_keys('@Sai9010')

login = driver.find_element(
    by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
login.click()
print('Login Successfully')
time.sleep(2)

# follower_btn = driver.find_element_by_xpath(
#     '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[4]/aside/a/div/span')
# follower_btn.click()

notifications=driver.find_element(by=By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[3]/div/div/div/span')
notifications.click()

time.sleep(2)
# follwBtns=driver.find_element(by=By.XPATH,value="//span[text()='Follow']")
# print("button clicked")

# driver.close()


