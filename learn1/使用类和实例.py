##################################################9.2　使用类和实例###################################################

# 9-4 就餐人数 ：在为完成练习9-1而编写的程序中，添加一个名为number_served 的属性，并将其默认值设置为0。根据这个类创建
# 一个名为restaurant 的实例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
# 添加一个名为set_number_served() 的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
# 添加一个名为increment_number_served() 的方法，它让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值：
# 你认为这家餐馆每天可能接待的就餐人数。
class Restaurant():
    "'创建一个名为Restaurant 的类'"
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)


    def set_number_served(self,num):
        self.number_served = num


    def increment_number_served(self,num):
        self.number_served +=num

    def open_restaurant(self) :
        print("open the door")
a = Restaurant("xxx","xiaochao")
print(a.number_served)
a.set_number_served(100)
print(a.number_served)
a.increment_number_served(10)
print(a.number_served)

# 9-5 尝试登录次数 ：在为完成练习9-3而编写的User 类中，添加一个名为login_attempts 的属性。编写一个名为increment_login_attempts() 的方法，
# 它将属性login_attempts 的值加1。再编写一个名为reset_login_attempts() 的方法，它将属性login_attempts 的值重置为0。
# 根据User 类创建一个实例，再调用方法increment_login_attempts() 多次。打印属性login_attempts 的值，确认它被正确地递增；然后，调用方
# 法reset_login_attempts() ，并再次打印属性login_attempts 的值，确认它被重置为0。
class User():
    def __init__(self,first_name,last_name,describe):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts = 0
        self.describe=describe

    def describe_user(self):
        print(self.first_name+self.last_name+" "+self.describe)

    def greet_user(self):
        print("Hello "+self.first_name+self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

ll = User("ye","chenglong","handsome")
print(ll.login_attempts)
ll.increment_login_attempts()
ll.increment_login_attempts()
ll.increment_login_attempts()
print(ll.login_attempts)
ll.reset_login_attempts()
print(ll.login_attempts)







