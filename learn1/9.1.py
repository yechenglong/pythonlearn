#########################################9.1　创建和使用类###################################################

# 9-1 餐馆 ：创建一个名为Restaurant 的类，其方法__init__() 设置两个属性：restaurant_name 和cuisine_type 。创建一个名
# 为describe_restaurant() 的方法和一个名为open_restaurant() 的方法，其中前者打印前述两项信息，而后者打印一条消息，
# 指出餐馆正在营业。根据这个类创建一个名为restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
# class Restaurant():
#     "'创建一个名为Restaurant 的类'"
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name=restaurant_name
#         self.cuisine_type=cuisine_type
#
#     def describe_restaurant(self):
#         print(self.restaurant_name)
#         print(self.cuisine_type)
#
#     def open_restaurant(self) :
#         print("open the door")
#
# r1=Restaurant("xingping","chaocai")
# print(r1.restaurant_name+"  "+r1.cuisine_type)
# r1.describe_restaurant()
# r1.open_restaurant()

# 9-2 三家餐馆 ：根据你为完成练习9-1而编写的类创建三个实例，并对每个实例调用方法describe_restaurant() 。
# r2=Restaurant("xingping2","chaocai2")
# r3=Restaurant("xingping3","chaocai3")
# r4=Restaurant("xingping4","chaocai4")
# r2.describe_restaurant()
# r3.describe_restaurant()
# r4.describe_restaurant()


# 9-3 用户 ：创建一个名为User 的类，其中包含属性first_name 和last_name ，还有用户简介通常会存储的其他几个属性。在类User
# 中定义一个名为describe_user() 的方法，它打印用户信息摘要；再定义一个名为greet_user() 的方法，它向用户发出个性化的问候。
# 创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
class User():
    def __init__(self,first_name,last_name,describe):
        self.first_name=first_name
        self.last_name=last_name

        self.describe=describe

    def describe_user(self):
        print(self.first_name+self.last_name+" "+self.describe)

    def greet_user(self):
        print("Hello "+self.first_name+self.last_name)
u2=User("ye","chenglong","handsome")
u2.describe_user()
u2.greet_user()
