# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 登录
def login(un,pwd):
    # 点击登录按钮
    WebDriverWait(browser,10).until(
        EC.presence_of_element_located((By.LINK_TEXT,'登录'))
    ).click()
    # 输入用户名和密码
    WebDriverWait(browser,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'#userPanelName'))
    ).send_keys(un)
    WebDriverWait(browser,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'#userPanelPwd'))
    ).send_keys(pwd)
    time.sleep(5)
    # 登录
    WebDriverWait(browser,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'#loginBtn'))
    ).click()
    # 等待网页跳转
    time.sleep(10)

# 进入发帖页面 
def into_publish_page():
    # 进入发帖页面
    WebDriverWait(browser,10).until(
        EC.presence_of_element_located((By.LINK_TEXT,'发表新帖'))
    ).click()
    windows = browser.window_handles
    browser.switch_to.window(windows[-1])
    # 等待网页跳转
    time.sleep(5)
    # 点击证券区
    WebDriverWait(browser,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'#blockID1'))
    ).click()
    # 提交
    browser.find_element_by_css_selector('body > div > form > input[type="submit"]').click()
    time.sleep(5)
    
# 发帖  
def publish(headline,substance):
    # 填写标题
    WebDriverWait(browser,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'#subject'))
    ).send_keys(headline)
    # 点一下内容框
    # 进入iframe标签
    # 填写内容
    WebDriverWait(browser,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'.ks-editor'))
    ).click()
    time.sleep(5)
    browser.switch_to.frame('ks-editor-iframe')
    browser.find_element_by_css_selector('body').send_keys(substance)
    browser.switch_to.default_content()
    # 提交
    browser.find_element_by_css_selector('#submit2').click()
    
# 主函数
def main(un,pwd,tit,cont):
    try:
        login(un,pwd)
        into_publish_page()
        publish(tit,cont)
    except:
        print('未找到元素')
    finally:
        browser.quit()

       
username = '输入账号'
password = '输入密码'  
title = '输入标题'
content = '输入内容'
browser = webdriver.Chrome()
browser.get('https://www.taoguba.com.cn/')
main(username,password,title,content)



