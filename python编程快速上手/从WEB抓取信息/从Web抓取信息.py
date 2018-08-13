import requests,logging
logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s- %(message)s')
res = requests.get("http://www.baidu.com")
logging.debug(res.status_code)
logging.debug(len(res.text))
logging.debug(res.text[:100])
