# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 22:48:22 2016

@author: WHUER
"""

import urllib, urllib2
import datetime
import sys

reload(sys)
sys.setdefaultencoding('utf8')

starttime = datetime.datetime.now()

###############################################################################
#                               subfunction                                   #
###############################################################################
#获取验证码
def get_picture_data(i, j, k, pic_add, pic_add_type, page_url):
    print u"正在尝试请求 " + 'l3_'+i+'_'+pic_add_type+j+'_'+pic_add_type+k+'.jpg'
    #request
    picture_url = pic_add +i+'/l3/'+pic_add_type+j+'/l3_'+i+'_'+pic_add_type+j+'_'+pic_add_type+k+'.jpg'
    req = urllib2.Request(picture_url) 
    req.add_header('Accept', '*/*')
    req.add_header('Accept-Encoding', 'gzip, deflate, sdch')
    req.add_header('Accept-Language', 'zh-CN,zh;q=0.8')
    req.add_header('Cache - Control', 'max-age=0')
    req.add_header('Connection', 'keep-alive')
    req.add_header('Host', 'xml-static.720static.com')
    req.add_header('Origin', 'http://720yun.com')
    req.add_header('Referer', page_url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36')
    try:
        picture = urllib2.urlopen(picture_url, timeout=8)
        status = str(picture.getcode())
        picData = picture.read()
        picture.close()
    except:
        try:
            print u'请求似乎出现了问题，正在重试中……'
            picture = urllib2.urlopen(picture_url, timeout=8)
            status = str(picture.getcode())
            picData = picture.read()
            picture.close()
        except:
            status = '404'
            picData = ''

    print 'Request info: ' + status
    return picData, status

#save pic
def save_picture(i, j, k, picData, pic_add_type):
    path = './pic/' + 'l3_'+i+'_'+pic_add_type+j+'_'+pic_add_type+k+'.jpg'
    print u"正在下载图片，请稍后……"
    localPic = open(path, "wb")
    localPic.write(picData)
    localPic.close()

###############################################################################
#                              mainfunction                                   #
###############################################################################
def get_pic(pic_add, pic_add_type, page_url):
    irange = ['b', 'd', 'f', 'l', 'r', 'u']
    for i in irange:
        for j in xrange(1,6):
            for k in xrange(1,6):
                j = str(j)
                k = str(k)
                get_return = get_picture_data(i, j, k, pic_add, pic_add_type, page_url)
                picData = get_return[0]
                status = get_return[1]
                if status == '200':
                    save_picture(i, j, k, picData, pic_add_type)
                else:
                    print u'本次请求的图片不存在！'

    print u'所有图片请求完毕！'

    # 总时间
    endtime = datetime.datetime.now()
    interval = (endtime - starttime).seconds
    print 'Total time of getting pictures is ' + str(int(interval / 60)) + ' min (' + str(interval) + ' s )'

if __name__ == '__main__':
    get_pic('http://pano8.qncdn.720static.com/resource/prod/214ifdc13n9/d5023xsvaun/922616/imgs/', '0')