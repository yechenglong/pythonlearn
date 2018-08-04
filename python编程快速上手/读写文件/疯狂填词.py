# 创建一个疯狂填词（Mad Libs）程序，它将读入文本文件，并让用户在该文本
# 文件中出现ADJECTIVE、NOUN、ADVERB 或VERB 等单词的地方，加上他们自
# 己的文本。例如，一个文本文件可能看起来像这样：
# The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
# unaffected by these events.
# 程序将找到这些出现的单词，并提示用户取代它们。
# Enter an adjective:
# silly
# Enter a noun:
# chandelier
# Enter a verb:
# screamed
# Enter a noun:
# pickup truck
# 以下的文本文件将被创建：
# The silly panda walked to the chandelier and then screamed. A nearby pickup
# truck was unaffected by these events.
# 结果应该打印到屏幕上，并保存为一个新的文本文件。

#疯狂填词-替换文本文件中的单词
'''
	方法步骤：
		1.导入文本
		2.循环查找并替换
		3.打印结果，保存为另一个新的文件
'''
import re
with open('test','r') as libfile,open('newfile.txt','w') as newfile:
    # TODO : 导入文本
    text = libfile.read()
    # TODO : 查找要更换的单词
    re1 = re.compile('ADJECTIVE|NOUN|VERB|ADVERB')
    needreplacewprd = re1.findall(text)
    print(needreplacewprd)
    # TODO : 循环更换单词
    for word in needreplacewprd:
        replaceword = input("Enter a  " + word + ' :\n')
        re2 = re.compile(word)
        text = re2.sub(replaceword,text)
    print(text)
    # TODO : 写入新的文本
    newfile.write(text)











