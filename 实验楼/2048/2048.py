import curses


class Action(object):

    UP = 'up'
    LEFT = 'left'
    DOWN = 'down'
    RIGHT = 'right'
    RESTART = 'restart'
    EXIT = 'exit'
    # ord()函数返回对应字符的 ASCII 数值
    letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
    actions = [UP, LEFT, DOWN, RIGHT, RESTART, EXIT]
    # 将UP, LEFT, DOWN, RIGHT, RESTART, EXIT和WASDRQwasdrq进行匹配{87: 'up', 65: 'left', 83: 'down', 68:
    # 'right', 82: 'restart', 81: 'exit', 119: 'up', 97: 'left', 115: 'down', 100: 'right', 114: 'restart', 113: 'exit'}
    # zip()把列表合并，并创建一个元组对的列表,dict()传一个包含一个或多个元祖的列表建立字典
    actions_dict = dict(zip(letter_codes, actions * 2))

    def __init__(self, stdscr):
        self.stdscr = stdscr

    def get(self):
        char = "N"
        while char not in self.actions_dict:
            char = self.stdscr.getch()
        return self.actions_dict[char]

class test(object):
    def __call__(self, stdscr):
        curses.use_default_colors()
        self.stdscr = stdscr
        self.action = Action(stdscr)
if __name__ == '__main__':
    curses.wrapper(test())