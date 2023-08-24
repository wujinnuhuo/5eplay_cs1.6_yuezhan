from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from webdriver_manager.chrome import ChromeDriverManager


count=0
while (count<9):

    chrome_driver = "E:\develop\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver)
    # driver.get(url="http://vs.5eplay.com/")
    driver.get('http://vs.5eplay.com/')

    loginclick = driver.find_element(By.CLASS_NAME, 'login-btn')
    action = ActionChains(driver)
    action.click(loginclick)
    action.perform()

    username = driver.find_element(By.ID, 'username').send_keys('xiaorui2014@yeah.net')
    password = driver.find_element(By.ID, 'password').send_keys('sss999')
    time.sleep(1)
    login = driver.find_element(By.XPATH, '//button[@onclick="login();"]')
    action1 = ActionChains(driver)
    action1.click(login)
    action1.perform()

    time.sleep(1)

    fabu = driver.find_element(By.ID, 'vspost')
    act1 = ActionChains(driver)
    act1.click(fabu)
    act1.perform()

    time.sleep(1)

    shuoming = driver.find_element(By.LINK_TEXT, '请选择约战说明')
    act2 = ActionChains(driver)
    act2.click(shuoming)
    act2.perform()

    time.sleep(1)

    shuoming1 = driver.find_element(By.LINK_TEXT, '进来练练枪')
    act3 = ActionChains(driver)
    act3.click(shuoming1)
    act3.perform()

    qrfb = driver.find_element(By.LINK_TEXT, '确定发布')
    act4 = ActionChains(driver)
    act4.click(qrfb)
    act4.perform()

    time.sleep(2)

    driver.quit()

    count = count + 1
    if count > 9:
        break



