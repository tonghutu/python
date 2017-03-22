# -*- coding:utf-8 -*-
# coding=UTF-8

import os,urllib,urllib2,re

url = u"http://www.zngirls.com/g/21498/8.html"
outpath = "/Users/dufei/Code/Python/warm/"

def getHtml(url):
    webfile = urllib.urlopen(url)
    outhtml = webfile.read()
    print outhtml
    return outhtml

def getImageList(html):
    restr=ur'('
    restr+=ur'http:\/\/[^\s,"]*\.jpg'
    restr+=ur'|http:\/\/[^\s,"]*\.jpeg'
    restr+=ur'|http:\/\/[^\s,"]*\.png'
    restr+=ur'|http:\/\/[^\s,"]*\.gif'
    restr+=ur'|http:\/\/[^\s,"]*\.bmp'
    restr+=ur'|https:\/\/[^\s,"]*\.jpeg'
    restr+=ur'|https:\/\/[^\s,"]*\.jpeg'
    restr+=ur'|https:\/\/[^\s,"]*\.png'
    restr+=ur'|https:\/\/[^\s,"]*\.gif'
    restr+=ur'|https:\/\/[^\s,"]*\.bmp'
    restr+=ur')'
    htmlurl = re.compile(restr)
    imgList = re.findall(htmlurl,html)
    print imgList
    return imgList

def download(imgList, page):
    x = 1
    for imgurl in imgList:
        filepathname=str(outpath+'pic_%09d_%010d'%(page,x)+str(os.path.splitext(urllib2.unquote(imgurl).decode('utf8').split('/')[-1])[1])).lower()
        print '[Debug] Download file :'+ imgurl+' >> '+filepathname
        urllib.urlretrieve(imgurl,filepathname)
        if os.path.getsize(filepathname) < 102400:
            os.remove(filepathname)
        x+=1

def downImageNum(pagenum):
    page = 1
    pageNumber = pagenum
    while(page <= pageNumber):
        html = getHtml(url)#获得url指向的html内容
        imageList = getImageList(html)#获得所有图片的地址，返回列表
        download(imageList,page)#下载所有的图片
        page = page+1

if __name__ == '__main__':
    downImageNum(1)
