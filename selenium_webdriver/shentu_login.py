
"""
深图自动登录
"""

from login_site import LoginSite

if __name__ == '__main__':
    login_url = 'https://www.szlib.org.cn/MyLibrary/Reader-Access.jsp'
    user_name = 'xxxx'
    password = 'xxxx'
    ls = LoginSite(login_url, user_name, password, browser='chrome')
    name_locator = ('xpath', '//*[@id="username"]')
    password_locator = ('xpath', '//*[@id="password"]')
    submit_button_locator = ('class name', 'input-button')
    auto_login_locator = ('class name', 'input-checkbox')
    title = '我的图书馆'
    ls.login(name_locator, password_locator, submit_button_locator, auto_login_locator, title)