
"""
使用selenium实现自动登录
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class LoginSite():
    """
    Set of supported locator strategies.
    CLASS_NAME = 'class name'
    CSS_SELECTOR = 'css selector'
    ID = 'id'
    LINK_TEXT = 'link text'
    NAME = 'name'
    PARTIAL_LINK_TEXT = 'partial link text'
    TAG_NAME = 'tag name'
    XPATH = 'xpath'
    """
    
    def __init__(self, website, user_name, password, browser='chrome'):
        self.website = website
        self.user_name = user_name
        self.password = password
        
        self.driver = None
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        if browser == 'firefox':
            self.driver = webdriver.FireFox()
        
    def login(self, name_locator, password_locator, submit_button_locator, ck_auto_login_locator, title):
        """
        关于封装的好坏与判断边界，这种写法如果重用当然会省事，但是否是缺点的判断边界看locator是否能够仅通过find_element这一步就可以找到元素。
        """
        self.driver.get(self.website)
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(name_locator))
        
        i_user_name = self.driver.find_element(name_locator[0], name_locator[1])
        i_user_name.send_keys(self.user_name)
        
        i_password = self.driver.find_element(password_locator[0], password_locator[1])
        i_password.send_keys(self.password)
        
        ck_auto_login = self.driver.find_element(ck_auto_login_locator[0], ck_auto_login_locator[1])
        ck_auto_login.click()
        
        submit = self.driver.find_element(submit_button_locator[0], submit_button_locator[1])
        submit.click()
        WebDriverWait(self.driver, 20).until(expected_conditions.title_contains(title))
        
        cookies = self.driver.get_cookies()
        # print(cookies)
        
        
        