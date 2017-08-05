'''
Created on 2017年7月29日

@author: gql
'''
from time import sleep



def bd_search(driver):
    driver.get("http://www.baidu.com")
    sleep(2)
    print(driver.title)
    search_in=driver.find_element_by_id('kw')
    search_in.clear()
    search_in.send_keys('python')
    print('搜索关键词： python')
    driver.find_element_by_id('su').click()
    sleep(2)
    print(driver.title)
    return driver.title

if __name__=="__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    url='https://www.baidu.com/'
    bd_search(driver)