######################################6.3遍历字典######################################################################

# 6-4 词汇表2 ：既然你知道了如何遍历字典，现在请整理你为完成练习6-3而编写的代码，将其中的一系列print 语句替换为一个遍历
# 字典中的键和值的循环。确定该循环正确无误后，再在词汇表中添加5个Python术语。当你再次运行这个程序时，
# 这些新术语及其含义将自动包含在输出中。
favorite_nums = {"a":1,"b":2,"c":3,"d":4,"e":5}
for name,favorite_num in favorite_nums.items() :
    print(name+" "+ str(favorite_num))

# 6-5 河流 ：创建一个字典，在其中存储三条大河流及其流经的国家。其中一个键—值对可能是'nile': 'egypt' 。
# 使用循环为每条河流打印一条消息，如“The Nile runs through Egypt.”。
# 使用循环将该字典中每条河流的名字都打印出来。
# 使用循环将该字典包含的每个国家的名字都打印出来。
rivers = {"nile":"egypt","黄河":"中国","尼罗河":"印度"}
for river,guojia in rivers.items() :
    print(river+" "+guojia)

for river in rivers.keys() :
    print(river)

for guojia in rivers.values() :
    print(guojia)

# 6-6 调查 ：在6.3.1节编写的程序favorite_languages.py中执行以下操作。
# 创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。
# 遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢。对于还未参与调查的人，打印一条消息邀请他参与调查。

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
friends = ["jen","phil","adme","lilth"]
for name in favorite_languages.keys():
    if name in friends:
        print("  Hi"+name.title()+" Thank you")
    else:
        print(" Hi"+name.title()+" welcome")
