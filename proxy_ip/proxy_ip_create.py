#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 设置编码格式为utf-8，为了可以打印出中文字符
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#导入操作json的模块
import json

#导入time模块，用于线程休眠
import time

# 导入resquest模块(需要安装)
import requests

# 导入BeautifulSoup模块(需要安装)，用于解析网页的内容
from bs4 import BeautifulSoup

#从知乎粘贴而来
class SpiderProxy(object):
    """黄哥Python培训 黄哥所写 Python版本为2.7以上"""
    headers = {
        "Host": "www.xicidaili.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "http://www.xicidaili.com/wt/1",
    }

    def __init__(self, session_url):
        self.req = requests.session()
        self.req.get(session_url)

    def get_pagesource(self, url):
        html = self.req.get(url, headers=self.headers)
        return html.content

    def get_all_proxy(self, url, n):
        data = []
        for i in range(1, n):
            html = self.get_pagesource(url + str(i))
            soup = BeautifulSoup(html, "html.parser")

            table = soup.find('table', id="ip_list")
            for row in table.findAll("tr"):
                cells = row.findAll("td")
                tmp = []
                for item in cells:

                    tmp.append(item.find(text=True))
                data.append(tmp[1:3])
        return data

session_url = 'http://www.xicidaili.com/wt/1'
url = 'http://www.xicidaili.com/wt/'
p = SpiderProxy(session_url)
proxy_ip = p.get_all_proxy(url, 2)
for item in proxy_ip:
    if item:
        print '\'http\':\'http://'+item[0]+":"+item[1]+'\','
        print '\'https\':\'https://'+item[0]+":"+item[1]+'\','
