# 写一个函数，它接受一个字符串，做的事情和strip()字符串方法一样。如果只
# 传入了要去除的字符串，没有其他参数，那么就从该字符串首尾去除空白字符。否
# 则，函数第二个参数指定的字符将从该字符串中去除。
import re
def stripre(str1,str2 = r'\s'):
    s = re.compile(r'^%s*|%s*$'%(str2,str2))
    str1 = s.sub("",str1)
    return str1

print(stripre('aadasdfsaaa','a'))
print(stripre('  dafsdfa sadfasd  '))





