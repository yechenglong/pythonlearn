UP = 'up'
LEFT = 'left'
DOWN = 'down'
RIGHT = 'right'
RESTART = 'restart'
EXIT = 'exit'
# ord()函数返回对应字符的 ASCII 数值
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
actions = [UP, LEFT, DOWN, RIGHT, RESTART, EXIT]
# 将UP, LEFT, DOWN, RIGHT, RESTART, EXIT和WASDRQwasdrq进行匹配
actions_dict = dict(zip(letter_codes, actions * 2))
print(actions_dict)