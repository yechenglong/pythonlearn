# 10-3 访客 ：编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写入到文件guest.txt中。
# filename = 'guest.txt'
# with open(filename,'w') as file_boject:
#     m = input("输入姓名: ")
#     file_boject.write(m + "\n")

# 10-4 访客名单 ：编写一个while 循环，提示用户输入其名字。用户输入其名字后，在屏幕上打印一句问候语，并将一条访问记录添加
# 到文件guest_book.txt中。确保这个文件中的每条记录都独占一行。
filename = 'guest.txt'
active = True
with open(filename,'a') as file_boject:
    while active:
        m = input("输入姓名: ")
        if m=="quit":
            active=False
        else:
            print("Hello "+m)
            file_boject.write(m + "\n")
            active = True




