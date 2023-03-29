import os
from selenium import webdriver
import time
screencutImagePathTemplate = '../assets/preview/{}.png'

#截图
def screencut(url, no):
    if os.path.exists(screencutImagePathTemplate.format(no)): return
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')  # 禁用gpu
    options.add_argument('--ignore-certificate-errors') #忽略一些莫名的问题
    options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 开启开发者模式
    options.add_argument('--disable-blink-features=AutomationControlled')  # 谷歌88版以上防止被检测
    options.add_argument('--headless')  # 无界面
    driver = webdriver.Chrome(options=options)  # 将chromedriver放到Python安装目录Scripts文件夹下
    #临时html文件路径
    # url = f"http://localhost:6600/038.el-popover%E6%A0%B9%E6%8D%AE%E5%AD%97%E7%AC%A6%E8%B6%85%E5%87%BA%E6%98%AF%E5%90%A6%E5%B1%95%E7%A4%BA.html"
    driver.get(url)
    time.sleep(1)
    js_height = "return document.body.clientHeight"
    k = 1
    height = driver.execute_script(js_height)
    while True:
        if k * 500 < height:
            js_move = "window.scrollTo(0,{})".format(k * 500)
            driver.execute_script(js_move)
            time.sleep(0.2)
            height = driver.execute_script(js_height)
            k += 1
        else:
            break
    # 注：必须开启无界面模式，即：--headless
    # 接下来是全屏的关键，用js获取页面的宽高，如果有其他需要用js的部分也可以用这个方法
    width = driver.execute_script("return document.body.scrollWidth")
    height = driver.execute_script("return document.body.scrollHeight")
    # 将浏览器的宽高设置成刚刚获取的宽高
    driver.set_window_size(width, height)
    time.sleep(1)
    # 截图并关掉浏览器
    driver.save_screenshot(screencutImagePathTemplate.format(no))
    time.sleep(0.5)
    driver.close()

exampleList = open(f"../examples.txt",'r',encoding='utf-8')
templateFile = open(f"./template.md",'r',encoding='utf-8')
developmentFile = open(f"./development.md",'r',encoding='utf-8')
readmeFile = open(f"../readme.md",'w',encoding='utf-8') 
baseUrl = 'http://localhost:6600/'

try:
  lines = exampleList.readlines()
  template = templateFile.readlines()
  development = developmentFile.readlines()
  readmeFile.writelines(template)
  for line in lines:
    if not line.startswith('index'):
        try:
            screencut(baseUrl+line, line.split('.')[0])
            readmeFile.writelines('##### [**{}**](https://linyisonger.github.io/H5.Examples/?name=./{}) \n'.format(line.split('.')[1],line.replace('\n','').replace(' ','%20')))
            readmeFile.writelines('![](./assets/preview/{}.png)\n'.format(line.split('.')[0]))
        except:
            print('生成异常文件:{}'.format(line))
  readmeFile.writelines('\n')
  readmeFile.writelines('\n')
  readmeFile.writelines(development)
finally:
    developmentFile.close()
    templateFile.close()
    exampleList.close()
    readmeFile.close()
    

