###########################################10.4存储数据#############################################################
# 10-11 喜欢的数字 ：编写一个程序，提示用户输入他喜欢的数字，并使用json.dump() 将这个数字存储到文件中。再编写一个程序，
# 从文件中读取这个值，并打印消息“I know your favorite number! It's _____.”。
import json
filename = "xihuandeshuzi.json"
def write():
    with open(filename,"w") as filewrite:
        num = input("qing shu ru ni xi huan de shu zi: ")
        json.dump(num,filewrite)
def read():
    with open(filename,"r") as fileread:
        num1 = json.load(fileread)
        print("I know your favorite number! It's "+num1+" .")
# write()
# read()

# 10-12 记住喜欢的数字 ：将练习10-11中的两个程序合而为一。如果存储了用户喜欢的数字，就向用户显示它，否则提示用户输入他喜
# 欢的数字并将其存储到文件中。运行这个程序两次，看看它是否像预期的那样工作。
def test():
    try:
        read()
    except FileNotFoundError:
        write()

# 10-13 验证用户 ：最后一个remember_me.py版本假设用户要么已输入其用户名，要么是首次运行该程序。我们应修改这个程序，以应
# 对这样的情形：当前和最后一次运行该程序的用户并非同一个人。为此，在greet_user() 中打印欢迎用户回来的消息前，先询问
# 他用户名是否是对的。如果不对，就调用get_new_username() 让用户输入正确的用户名。
def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username
def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        ss = input("ni hao ,qing wen nin shi bu shi "+username+" (yes/no) ")
        if ss== "yes":
            print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
    print("We'll remember you when you come back, " + username + "!")

greet_user()