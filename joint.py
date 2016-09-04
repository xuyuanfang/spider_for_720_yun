# -*- coding: utf-8 -*-
"""
Created on Thu Aug 04 11:46:16 2016

@author: WHUER
"""
from __future__ import division #精确除法运算
import Image
import datetime
import sys

reload(sys)
sys.setdefaultencoding('utf8')

starttime = datetime.datetime.now()

def joint(pic_add_type, id):
    imgi = Image.open('./pic/' + 'l3_b_' + pic_add_type + '1_' + pic_add_type + '5.jpg')
    imgi = imgi.convert("RGBA")
    pixdata = imgi.load()
    #小图宽高
    w = imgi.size[0]
    h = imgi.size[1]
    # 新图宽高new
    nw = h*4 + w
    nh = nw
    # Image.new( mode, (width, height), color ) (255, 255, 255)
    newimg = Image.new('RGBA', (nw, nh), (255, 255, 255, 255))
    pixdata_new = newimg.load()
    irange = ['b', 'd', 'f', 'l', 'r', 'u']
    print u'六面图片拼接开始！'
    cal = 0
    for i in irange:
        for j in xrange(1,6):
            for k in xrange(1,6):
                imgi = Image.open('./pic/'+'l3_'+i+'_'+pic_add_type+str(j)+'_'+pic_add_type+str(k)+'.jpg')
                imgi = imgi.convert("RGBA")
                pixdata = imgi.load()
                try:
                    for y in xrange(imgi.size[1]):
                        for x in xrange(imgi.size[0]):
                            # print pixdata[x, y]
                            pixdata_new[x + h*(k-1), y + h*(j-1)] = pixdata[x, y]
                except:
                    print 'resize fail!'
        # 保存子图像
        newimg.save('./pic/'+id+'_'+i+'_cross.jpg', "JPEG")
        cal += 1
        caltime = datetime.datetime.now()
        sec = (caltime - starttime).seconds
        print u'第'+str(cal)+u'张图片拼接完成！ (Used '+str(sec)+'s)'

    nnw = nw*4
    nnh = nh*3
    # Image.new( mode, (width, height), color ) (255, 255, 255)
    newimg = Image.new('RGBA', (nnw, nnh), (255, 255, 255, 255))
    pixdata_new = newimg.load()
    irange = ['l', 'f', 'r', 'b']
    print u'十字图像拼接开始！'
    cal = 0
    for i in irange:
        cal += 1
        imgi = Image.open('./pic/'+id+'_'+i+'_cross.jpg')
        imgi = imgi.convert("RGBA")
        pixdata = imgi.load()
        try:
            for y in xrange(imgi.size[1]):
                for x in xrange(imgi.size[0]):
                    # print pixdata[x, y]
                    pixdata_new[x + nw*(cal-1), y + nw] = pixdata[x, y]
            caltime = datetime.datetime.now()
            sec = (caltime - starttime).seconds
            print u'图片' + i + u'已经就位！ (Used ' + str(sec) + 's)'
        except:
            print 'resize fail!'
    cal =0
    irange = ['u', 'd']
    for i in irange:
        cal += 1
        imgi = Image.open('./pic/' + id + '_' + i + '_cross.jpg')
        imgi = imgi.convert("RGBA")
        pixdata = imgi.load()
        try:
            for y in xrange(imgi.size[1]):
                for x in xrange(imgi.size[0]):
                    # print pixdata[x, y]
                    pixdata_new[x + nw, y + nw*2*(cal - 1)] = pixdata[x, y]
            caltime = datetime.datetime.now()
            sec = (caltime - starttime).seconds
            print u'图片' + i + u'已经就位！ (Used ' + str(sec) + 's)'
        except:
            print 'resize fail!'
    # 保存十字图像
    newimg.save('./pic/'+id+'_cross.jpg', "JPEG")
    caltime = datetime.datetime.now()
    sec = (caltime - starttime).seconds
    print u'十字图像拼接完成！ (Used '+str(sec)+'s)'

    # 总时间
    endtime = datetime.datetime.now()
    interval = (endtime - starttime).seconds
    print 'Total time of jionting pictures is ' + str(int(interval / 60)) + ' min (' + str(interval) + ' s )'

if __name__ == '__main__':
    joint('0', '922616')
