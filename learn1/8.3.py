###########################################8.3　返回值################################################################

# 8-6 城市名 ：编写一个名为city_country() 的函数，它接受城市的名称及其所属的国家。这个函数应返回一个格式类似于下
# 面这样的字符串："Santiago, Chile" 至少使用三个城市-国家对调用这个函数，并打印它返回的值。
# def city_country(city,country):
#     mes = '"'+city+', '+country+'"'
#     return  mes
# a=city_country("Shanghai","China")
# print(a)
# b=city_country("Zhuhai","China")
# print(b)
# c=city_country("Santiago","Chile")
# print(c)

# 8-7 专辑 ：编写一个名为make_album() 的函数，它创建一个描述音乐专辑的字典。这个函数应接受歌手的名字和专辑名，并返回一个
# 包含这两项信息的字典。使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
# 给函数make_album() 添加一个可选形参，以便能够存储专辑包含的歌曲数。如果调用这个函数时指定了歌曲数，就将这个值添加到
# 表示专辑的字典中。调用这个函数，并至少在一次调用中指定专辑包含的歌曲数。
# def make_album(singer,album_name,songnum='') :
#     if songnum:
#         album = {"singer": singer, "album_name": album_name,"songnum":songnum}
#         return album
#     else:
#         album = {"singer": singer, "album_name": album_name}
#         return album
# a=make_album("JJ","她说","14")
# print(a)
# b=make_album("jay","以父之名")
# print(b)
# c=make_album("vae","青年晚报")
# print(c)

# 8-8 用户的专辑 ：在为完成练习8-7编写的程序中，编写一个while 循环，让用户输入一个专辑的歌手和名称。获取这些信息后，
# 使用它们来调用函数make_album() ，并将创建的字典打印出来。在这个while 循环中，务必要提供退出途径。
def make_album(singer,album_name,songnum='') :
    if songnum:
        album = {"singer": singer, "album_name": album_name,"songnum":songnum}
        return album
    else:
        album = {"singer": singer, "album_name": album_name}
        return album
active = True
while active:
    z = input("是否要继续（离开请输入quit）： ")
    if z == "quit":
        active = False
    else:
        singer = input("输入歌手名字： ")
        album_name = input("输入专辑: ")
        m = make_album(singer,album_name)
        print(m)

