# 写一个函数，它使用正则表达式，确保传入的口令字符串是强口令。强口令的
# 定义是：长度不少于8 个字符，同时包含大写和小写字符，至少有一位数字。你可
# 能需要用多个正则表达式来测试该字符串，以保证它的强度

import re
def checkPassword(str1):
    q=re.compile(r'''
        (?=^.{8,}$)
        (?=.*\d+)
        (?=.*[A-Z])
        (?=.*[a-z])
    ''',re.VERBOSE)
    macth = q.match(str1)
    return macth is not None
# print(checkPassword('A'))  # False
# print(checkPassword('a'))  # False
# print(checkPassword('1'))  # False
# print(checkPassword('Aa'))  # False
# print(checkPassword('A1'))  # False
# print(checkPassword('a1'))  # False
# print(checkPassword('Aa1'))  # False
# print(checkPassword('Aa12345'))  # False
print(checkPassword('AaBbCcDd'))  # False
# print(checkPassword('ABCD1234'))  # False
# print(checkPassword('abcd1234'))  # False
# print(checkPassword('Aa123456'))  # True


