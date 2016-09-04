# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 22:48:22 2016

@author: WHUER
"""
from get_pic import get_pic
from joint import joint
import urllib, urllib2
import re
import datetime
from StringIO import StringIO
import gzip
import time
import random
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

starttime = datetime.datetime.now()

###############################################################################
#                               subfunction                                   #
###############################################################################
#获取验证码
def get_xml(page_url):
    print u"正在请求并分析目标页面……"
    #正则提取
    try:
        e = re.findall('720yun.com/t/(.*?)\?pano_id', page_url)[0]
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        gettime = str(int(time.time())) + str(a) + str(b) + str(c)
        xml = 'http://xml-static.720static.com/@/' + e + '/' + e + '.xml?' + gettime
    except:
        xml = u'提取失败！'
    print 'xml_address: ' + xml
    return xml

#save pic
def get_pic_add(xml, id):
    print u"正在获取图片通用请求地址……"
    try:
        page = urllib2.urlopen(xml, timeout=8)
        status = str(page.getcode())
        pageData = page.read()  # .decode('gbk').encode('utf8')
        page.close()
        pageData_tmp = "".join(pageData.split())
        pic_add_front = re.findall('<scenename="scene_' + id + '(.*?)</scene>', pageData_tmp)[0]
        pic_add_front_tmp = re.findall('<leveltiledimagewidth=(.*?)/></level>', pic_add_front)[0]
        pic_add_front = re.findall('cubeurl="(.*?)' + id, pic_add_front_tmp)[0]
        pic_add_type = re.findall(id + '(.*?).jpg', pic_add_front_tmp)[0]
        pic_add_type = re.findall('0', pic_add_type)
        if pic_add_type == []:
            pic_add_type = ''
        else:
            pic_add_type = '0'
    except:
        status = '404'
        pic_add = ''
    print 'Request info: ' + status
    return pic_add_front, pic_add_type


###############################################################################
#                              mainfunction                                   #
###############################################################################
def test():
    new_path = os.path.join('./pic')
    if not os.path.isdir(new_path):
        os.makedirs('./pic')
    #page_url = raw_input(u'请输入网址：')
    page_url = 'http://720yun.com/t/15a29xbfm4g?pano_id=1101727'#922616
    #提取id
    id = re.findall('id=(.*?)a', page_url+'a')[0]
    #获取xml地址
    xml = get_xml(page_url)
    #获取图片请求通用地址
    response_pic_add = get_pic_add(xml, id)
    pic_add_front =response_pic_add[0]
    pic_add_type = response_pic_add[1]
    pic_add = pic_add_front + id + '/imgs/'
    print 'pic_address: ' + pic_add
    #请求图片片段
    get_pic(pic_add, pic_add_type, page_url)
    #拼接图像
    joint(pic_add_type, id)
    print u'文件全部处理完毕！'

    # 总时间
    endtime = datetime.datetime.now()
    interval = (endtime - starttime).seconds
    print 'Total time is ' + str(int(interval / 60)) + ' min (' + str(interval) + ' s )'

if __name__ == '__main__':
    test()