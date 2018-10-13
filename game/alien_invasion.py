import sys,pygame,logging
logging.basicConfig(level=logging.DEBUG,format="%(asctime)s-%(levelname)s-%(message)s")

def run_game():
    '''
    初始化游戏并创建一个屏幕对象
    :return:
    '''
    pygame.init()
