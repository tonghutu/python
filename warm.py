
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
def getImg(html):
    reg = r'src="(.*?\.jpg)" pic_ext=' #此处为正则表达式，用于匹配页面中的图片链接，不同的网页图片链接的格式有所不用，此处需按需调整
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 1
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.gif' % x )
        print "第",x,"张下载完成！"
        x+=1
#将图片所在网页链接放入此处，大部分在WINDOWS下使用，所以不采用变量传入的方式        
html = getHtml("http://tieba.baidu.com/p/3191208081")
#print html
getImg(html)
