import os
from pyppeteer import launch
import time
import asyncio
import datetime

screencutImagePathTemplate = '../assets/preview/{}.png'


# 截图
async def screencut(url, no):
    if os.path.exists(screencutImagePathTemplate.format(no)):
        return
    browser = await launch(headless=True, dumpio=True, autoClose=False,  args=['--no-sandbox', '--window-size=1920,1080', '--disable-infobars'])
    # 打开新的标签页
    page = await browser.newPage()
    await page.goto(url)
    await page.setViewport({'width': 1920, 'height': 1080})
    height = await page.evaluate('() => document.body.clientHeight')
    time.sleep(1)
    await page.setViewport({'width': 1920, 'height': height})
    await page.screenshot({'path': screencutImagePathTemplate.format(no)})
    await browser.close()


def timestamp_to_timestr(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)


exampleList = open(f"../examples.txt", 'r', encoding='utf-8')
templateFile = open(f"./template.md", 'r', encoding='utf-8')
developmentFile = open(f"./development.md", 'r', encoding='utf-8')
readmeFile = open(f"../readme.md", 'w', encoding='utf-8')
baseUrl = 'http://localhost:6600/'

try:
    lines = exampleList.readlines()
    template = templateFile.readlines()
    development = developmentFile.readlines()
    readmeFile.writelines(template)
    for line in lines:
        if not line.startswith('index'):
            # try:
            asyncio.set_event_loop_policy(
                asyncio.WindowsSelectorEventLoopPolicy())
            asyncio.run(screencut(baseUrl+line, line.split('.')[0]))

            readmeFile.writelines('##### [**{}**](https://linyisonger.github.io/H5.Examples/?name=./{}) \n'.format(
                line.split('.')[1], line.replace('\n', '').replace(' ', '%20')))
            readmeFile.writelines(
                '![](./assets/preview/{}.png)\n'.format(line.split('.')[0]))
        # except:
        #     print('生成异常文件:{}'.format(line))
    readmeFile.writelines('\n')
    readmeFile.writelines('\n')
    readmeFile.writelines(development)
finally:
    developmentFile.close()
    templateFile.close()
    exampleList.close()
    readmeFile.close()
