# coding=utf-8
from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Safari()

def after_all(context):
    context.driver.close()