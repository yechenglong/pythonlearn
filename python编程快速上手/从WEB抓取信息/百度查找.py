# 下面是程序要做的事：
# • 从命令行参数中获取查询关键字。
# • 取得查询结果页面。
# • 为每个结果打开一个浏览器选项卡。
# 这意味着代码需要完成以下工作：
# • 从sys.argv 中读取命令行参数。
# • 用requests 模块取得查询结果页面。
# • 找到每个查询结果的链接。
# • 调用webbrowser.open()函数打开Web 浏览器。
# 打开一个新的文件编辑器窗口，并保存为lucky.py。
import requests,webbrowser,logging,bs4
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
keyword = 'cc'
res = requests.get('http://www.baidu.com/baidu?wd='+ ''.join(keyword))
status = res.raise_for_status()
logging.debug(status)
# logging.debug(res.text)
soup = bs4.BeautifulSoup(res.text)

links = soup.findAll('h3')
logging.debug('###############################################################################')
numOpen = min(5,len(links))
for h3 in range(numOpen):
    href = links[h3].find("a").get("href")
    logging.debug(href)
    webbrowser.open(href)

