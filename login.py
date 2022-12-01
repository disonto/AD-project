# 로그인 정보를 확인하는 파일
from selenium import webdriver
from selenium.webdriver.common.by import By

def check(id, pw):
    try:
        driver = webdriver.Chrome(executable_path='chromedriver')
        url = 'https://ecampus.kookmin.ac.kr/login/index.php'
        driver.get(url)
        driver.find_element(By.ID, "input-username").send_keys(id)
        driver.find_element(By.ID, "input-password").send_keys(pw)
        driver.find_element(By.XPATH,"//*[@id=\"region-main\"]/div/div/div[1]/div[1]/div[2]/div/form/div[1]/div[2]/button").click()
        if driver.current_url == 'https://ecampus.kookmin.ac.kr/':
            driver.close()
            return True
    except:
        driver.close()
        return False

# https://www.youtube.com/watch?v=x4aXKA0kDL0
# https://iq.opengenus.org/python-script-to-open-webpage-login/
# https://greeksharifa.github.io/references/2020/10/30/python-selenium-usage/
# view-source:https://ecampus.kookmin.ac.kr/login/index.php
# view-source:https://sso.kookmin.ac.kr/sso/error.jsp
