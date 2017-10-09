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

#爬取详情页信息
def position_detail(position_id):

    #必须传的headers
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Host':'www.lagou.com',
        'Referer':'xxx',
        'Upgrade-Insecure-Requests':'1',
        'Cookie':'xxx'
    }
    url = 'https://www.lagou.com/jobs/%s.html' % position_id
    print url

    #通过get获取详情页信息
    result = requests.get(url, headers=headers)
    time.sleep(5)

    #解析职位要求text
    soup = BeautifulSoup(result.content, 'html.parser')
    position_conent = soup.find(class_="job_bt")

    #返回职位要求内容
    return position_conent.text

#爬虫主方法
def spider():

    #必须传的headers
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Host':'www.lagou.com',
        'Referer':'xxx',
        'X-Anit-Forge-Code':'0',
        'X-Anit-Forge-Token':None,
        'X-Requested-With':'XMLHttpRequest',
        'Cookie':'xxx'
    }

    #初始化总的职位信息list
    positions = []


    #循环30页，每一页爬取职位列表信息
    for page_int in range(1,31):
        #请求参数
        params = {
            #是否是第一页
            'first':'true',
            #请求第几页
            'pn':page_int,
            #搜索条件
            'kd':'python'
        }

        #构造请求并返回结果
        result = requests.post('https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false&isSchoolJob=0',
                                headers=headers,data=params)
        print result.content
        #解析返回的结果为json格式
        result_json = result.json()

        #获取每一页的职位信息
        page_positions = result_json['content']['positionResult']['result']

        #循环当前页每一个职位信息，再去爬职位详情页面
        for position in page_positions:
            #把我们要爬取信息放入字典
            position_dict = {
                'position_name':position['positionName'],#职位名称
                'work_year':position['workYear'],#工作年限
                'salary':position['salary'],#薪水
                'city':position['city'],#城市
                'company_name':position['companyFullName'],#公司全称
            }
            #获取到职位id
            position_id = position['positionId']

            #根据职位id爬取详情页信息并添加到字典
            position_dict['position_detail'] = position_detail(position_id)

            print position_dict
            #把每个职位信息放入总的list
            positions.append(position_dict)

        #线程休眠5秒，为了克服反爬
        time.sleep(5)

    #把爬取到的信息写入json文件
    line = json.dumps(positions,ensure_ascii=False)
    with open('lagou.json','w') as fp:
        fp.write(line.encode('utf-8'))




if __name__ == '__main__':
    spider()
