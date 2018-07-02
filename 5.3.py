######################################################################## if 语句###################################################################################################
# 5-3 外星人颜色#1 ：假设在游戏中刚射杀了一个外星人，请创建一个名为alien_color 的变量，并将其设置为'green' 、'yellow' 或'red' 。
# 编写一条if 语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出玩家获得了5个点。
# 编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中未通过（未通过测试时没有输出）。

alien_color="green"
if alien_color == "green":
    print("获得了5个点")

alien_color="red"
if alien_color == "green":
    print("获得了5个点")

# 5-4 外星人颜色#2 ：像练习5-3那样设置外星人的颜色，并编写一个if-else 结构。
# 如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5个点。
# 如果外星人不是绿色的，就打印一条消息，指出玩家获得了10个点。
# 编写这个程序的两个版本，在一个版本中执行if 代码块，而在另一个版本中执行else 代码块。
alien_color="green"
if alien_color == "green":
    print("射杀该外星人获得了5个点")
else:
    print("获得了10个点")

alien_color="red"
if alien_color == "green":
    print("射杀该外星人获得了5个点")
else:
    print("获得了10个点")

# 5-5 外星人颜色#3 ：将练习5-4中的if-else 结构改为if-elif-else 结构。
# 如果外星人是绿色的，就打印一条消息，指出玩家获得了5个点。
# 如果外星人是黄色的，就打印一条消息，指出玩家获得了10个点。
# 如果外星人是红色的，就打印一条消息，指出玩家获得了15个点。
# 编写这个程序的三个版本，它们分别在外星人为绿色、黄色和红色时打印一条消息。
alien_color="green"
if alien_color == "green":
    print("射杀该外星人获得了5个点")
elif alien_color == "yellow":
    print("获得了10个点")
else:
    print("获得了15个点")

alien_color="yellow"
if alien_color == "green":
    print("射杀该外星人获得了5个点")
elif alien_color == "yellow":
    print("获得了10个点")
else:
    print("获得了15个点")

alien_color="red"
if alien_color == "green":
    print("射杀该外星人获得了5个点")
elif alien_color == "yellow":
    print("获得了10个点")
else:
    print("获得了15个点")

# 5-6 人生的不同阶段 ：设置变量age 的值，再编写一个if-elif-else 结构，根据age 的值判断处于人生的哪个阶段。
# 如果一个人的年龄小于2岁，就打印一条消息，指出他是婴儿。
# 如果一个人的年龄为2（含）～4岁，就打印一条消息，指出他正蹒跚学步。
# 如果一个人的年龄为4（含）～13岁，就打印一条消息，指出他是儿童。
# 如果一个人的年龄为13（含）～20岁，就打印一条消息，指出他是青少年。
# 如果一个人的年龄为20（含）～65岁，就打印一条消息，指出他是成年人。
# 如果一个人的年龄超过65（含）岁，就打印一条消息，指出他是老年人。

age=24
if age < 2 :
    print("婴儿")
elif age >= 2 and age < 4 :
    print("正蹒跚学步")
elif age >= 4 and age < 13:
    print("儿童")
elif age >= 13 and age < 20:
    print("青少年")
elif age >= 20 and age < 65:
    print("成年人")
else:
    print("老年人")

# 5-7 喜欢的水果 ：创建一个列表，其中包含你喜欢的水果，再编写一系列独立的if 语句，检查列表中是否包含特定的水果。
# 将该列表命名为favorite_fruits ，并在其中包含三种水果。
# 编写5条if 语句，每条都检查某种水果是否包含在列表中，如果包含在列表中，就打印一条消息，如“You really like bananas!”。
fruits=["苹果","水蜜桃","西瓜"]
if "苹果" in fruits:
    print("I really like 苹果!")
if "水蜜桃" in fruits:
    print("I really like 水蜜桃!")
if "西瓜" in fruits:
    print("I really like 西瓜!")
if "香蕉" in fruits:
    print("I really like 香蕉!")
if "橘子" in fruits:
    print("I really like 橘子!")