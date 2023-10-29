from selenium import webdriver
from selenium.webdriver.common.by import By
from math import sqrt

sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html',
         'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html',
         'http://parsinger.ru/blank/1/6.html', ]
with webdriver.Chrome() as browser:
    s = 0
    for i, url in enumerate(sites):
        browser.execute_script(f'window.open("{url}", "_blank_{i}");')
    lst_windows = browser.window_handles
    for k in range(len(lst_windows) - 1, 0, -1):
        browser.switch_to.window(browser.window_handles[k])
        browser.find_element(By.CLASS_NAME, 'checkbox_class').click()
        s += sqrt(int(browser.find_element(By.ID, 'result').text))
        browser.close()
    print(round(s, 9))
