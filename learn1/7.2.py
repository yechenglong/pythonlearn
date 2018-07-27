##########################################while 循环简介###############################################################

# 7-4 比萨配料 ：编写一个循环，提示用户输入一系列的比萨配料，并在用户输入'quit' 时结束循环。每当用户输入一种配料后，
# 都打印一条消息，说我们会在比萨中添加这种配料。
# message1 = "输入比萨配料:  "
# message1 += "\n输入'quit' 时结束"
# peiliao = input(message1)
# print("我们会在比萨中添加"+peiliao)

# 7-5 电影票 ：有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；3~12岁的观众为10美元；超过12岁的观众为15美元。
# 请编写一个循环，在其中询问用户的年龄，并指出其票价。
# age = 0
# while age > 100:
#     age = input("输入年龄：  ")
#     print(age)
#     age = int(age)
#     if age < 3:
#         print("免费")
#
#     elif age >= 3 and age <= 12 :
#         print("10美元")
#
#     elif age > 12:
#         print("15美元")

# 7-6 三个出口 ：以另一种方式完成练习7-4或练习7-5，在程序中采取如下所有做法。
# 在while 循环中使用条件测试来结束循环。
# age = 0
# while age > 100:
#     age = input("输入年龄：  ")
#     print(age)
#     age = int(age)
#     if age < 3:
#         print("免费")
#
#     elif age >= 3 and age <= 12 :
#         print("10美元")
#
#     elif age > 12:
#         print("15美元")
# 使用变量active 来控制循环结束的时机。
# 使用break 语句在用户输入'quit' 时退出循环。
# active = True
# while active:
#     age = input("输入年龄：  ")
#     print(age)
#     if age == "quit" :
#         active = False
#     elif int(age) < 3:
#         print("免费")
#         active = True
#     elif int(age) >= 3 and int(age) <= 12 :
#         print("10美元")
#         active = True
#     else:
#         print("15美元")
#         active = True
# 7-7 无限循环 ：编写一个没完没了的循环，并运行它（要结束该循环，可按Ctrl +C，也可关闭显示输出的窗口）。
# i = 1
# while True:
#     print(i)
#     i=i+1

