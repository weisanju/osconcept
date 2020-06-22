import  webimport os
import time
from PIL import ImageGrab
import numpy as np
import cv2
urls = (
    '/reboot_html/(.*)', 'reboot_html',
    '/jp_html/(.*)', 'jp_html',
    '/shutdown_html/(.*)', 'shutdown_html',
    '/(js|css|images)/(.*)', 'static'
)
app = web.application(urls, globals())
render = web.template.render('templates/')
#重启电脑
class reboot_html:
    def GET(self, text):
        print('input:' + text)
        adb ='shutdown -r now'
        d = os.popen(adb)
        return render.reboot(content=text.upper())
#截屏
class jp_html:
    def GET(self, text):
        print('input:' + text)
        beg = time.time()
        debug = False
        # img = ImageGrab.grab(bbox=(250, 161, 1141, 610))
        img = ImageGrab.grab()
        end = time.time()
        print('time:',end - beg)
 
        # img.show()
        img.save("images/screen.jpg")
        return render.jp(content=text.upper())  
 
#关闭电脑
class shutdown_html:
    def GET(self, text):
        print('input:' + text)
        adb ='shutdown -s -f'
        d = os.popen(adb)
        return render.shutdown(content=text.upper())    
         
class static:
    def GET(self, media, file):
        try:
            f = open(media+'/'+file, 'rb')
            return f.read()
        except:
            return ''
 
if __name__ == "__main__":
    app.run()