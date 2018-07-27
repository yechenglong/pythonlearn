from 使用类和实例 import Restaurant
from 使用类和实例 import User
#####################################9,3 继承#########################################################################
# 9-6 冰淇淋小店 ：冰淇淋小店是一种特殊的餐馆。编写一个名为IceCreamStand 的类，让它继承你为完成练习9-1或练习9-4而编写
# 的Restaurant 类。这两个版本的Restaurant 类都可以，挑选你更喜欢的那个即可。添加一个名为flavors 的属性，用于存储一个由
# 各种口味的冰淇淋组成的列表。编写一个显示这些冰淇淋的方法。创建一个IceCreamStand 实例，并调用这个方法。
# class IceCreamStand(Restaurant):
#     def __init__(self,restaurant_name,cuisine_type):
#         super().__init__(restaurant_name,cuisine_type)
#         self.flavors = ["1ice","2ice","3ice"]
#
#     def print_ice(self):
#         print(self.flavors)
#
# a=IceCreamStand("111","1111")
# a.print_ice()

# 9-7 管理员 ：管理员是一种特殊的用户。编写一个名为Admin 的类，让它继承你为完成练习9-3或练习9-5而编写的User 类。添加一个
# 名为privileges 的属性，用于存储一个由字符串（如"can add post" 、"can delete post" 、"can ban user" 等）组成的列
# 表。编写一个名为show_privileges() 的方法，它显示管理员的权限。创建一个Admin 实例，并调用这个方法。
# class Admin(User):
#     def __init__(self,first_name,last_name,describe):
#         super().__init__(first_name,last_name,describe)
#         self.privileges=["can add post" ,"can delete post" ,"can ban user" ]
#
#     def show_privileges(self):
#         print(self.privileges)
# b = Admin("ye","chenglong","Handsome")
# b.show_privileges()

# 9-8 权限 ：编写一个名为Privileges 的类，它只有一个属性——privileges ，其中存储了练习9-7 所说的字符串列表。将方法show_privileges() 移到这
# 个类中。在Admin 类中，将一个Privileges 实例用作其属性。创建一个Admin 实例，并使用方法show_privileges() 来显示其权限。
# class Privileges():
#     def __init__(self,privileges=[]):
#         self.privileges = ["can add post" ,"can delete post" ,"can ban user" ]
#
#     def show_privileges(self):
#         print(self.privileges)
#
# class Admin(User):
#     def __init__(self, first_name, last_name, describe):
#         super().__init__(first_name,last_name,describe)
#         self.privileges = Privileges()
#
# c = Admin("ye","chenglong","Handsome")
# c.privileges.show_privileges()

# 9-9 电瓶升级 ：在本节最后一个electric_car.py版本中，给Battery 类添加一个名为upgrade_battery() 的方法。这个方法检查电瓶
# 容量，如果它不是85，就将它设置为85。创建一辆电瓶容量为默认值的电动汽车，调用方法get_range() ，然后对电瓶进行升级，并再
# 次调用get_range() 。你会看到这辆汽车的续航里程增加了。







