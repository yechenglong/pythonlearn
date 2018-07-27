############################################10.3 异常##############################################################

# 10-6 加法运算 ：提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数字。在这种情况下，当你尝试将输入
# 转换为整数时，将引发TypeError 异常。编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。在用户输入的任何一个
# 值不是数字时都捕获TypeError 异常，并打印一条友好的错误消息。对你编写的程序进行测试：先输入两个数字，再输入一些文本而不是数字。
# 10-7 加法计算器 ：将你为完成练习10-6而编写的代码放在一个while 循环中，让用户犯错（输入的是文本而不是数字）后能够继续输入数字。
# active =True
# while active:
#     num1 = input("shurudiyigeshuzi:  ")
#     num2 = input("shurudiergeshuzi:  ")
#     try:
#         add = int(num1) + int(num2)
#     except ValueError:
#         print("meiyoutigongshuzi,qingchongxinshuru: ")
#         continue
#     else:
#         print(add)

# 10-8 猫和狗 ：创建两个文件cats.txt和dogs.txt，在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。编写一个程序，尝试读取这些文件，
# 并将其内容打印到屏幕上。将这些代码放在一个try-except 代码块中，以便在文件不存在时捕获FileNotFound 错误，并打印一条友好的消息。将其中一个文件
# 移到另一个地方，并确认except 代码块中的代码将正确地执行。
with open("cats.txt","w") as file_cat:
    file_cat.write("cat1 \n"+"cat2 \n"+"cat3 \n")
with open("dogs.txt","w") as file_dog:
    file_dog.write("dog1 \n"+"dog2 \n"+"dog3 \n")
try:
    with open("cats.txt") as file_read:
        cats = file_read.read()
except FileNotFoundError:
    print("mei you zhao dao zhe ge wen dang ")
else:
    print(cats)
