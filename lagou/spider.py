#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 设置编码格式为utf-8，为了可以打印出中文字符
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 导入resquest模块(需要安装)
import requests

# 导入BeautifulSoup模块(需要安装)，用于解析网页的内容
from bs4 import BeautifulSoup

def main():
    #必须传的headers
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Host':'www.lagou.com',
        'Referer':'https://www.lagou.com/',

    }