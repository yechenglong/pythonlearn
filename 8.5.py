#################################################8.5　传递任意数量的实参##############################################

# 8-12 三明治 ：编写一个函数，它接受顾客要在三明治中添加的一系列食材。这个函数只有一个形参（它收集函数调用中提供的所
# 有食材），并打印一条消息，对顾客点的三明治进行概述。调用这个函数三次，每次都提供不同数量的实参。
# def make_sandwich(*toppings) :
#     for topping in toppings :
#         print(topping)
# make_sandwich("Romaine Lettuce","Bacon")
# make_sandwich("Ham","egg","beef")
# make_sandwich("chicken")

# 8-13 用户简介 ：复制前面的程序user_profile.py，在其中调用build_profile() 来创建有关你的简介；调用这个函数时，
# 指定你的名和姓，以及三个描述你的键-值对。
# def build_profile(first,last,**user_info):
#     profile={}
#     profile['first_name']=first
#     profile['last_name']=last
#     for key,value in user_info.items() :
#         profile[key]=value
#     return profile
# a=build_profile("ye","chenglong",describe="handsome",describe2="handsome",describe3="handsome")
# print(a)

# 8-14 汽车 ：编写一个函数，将一辆汽车的信息存储在一个字典中。这个函数总是接受制造商和型号，还接受任意数量的关键字实参。
# 这样调用这个函数：提供必不可少的信息，以及两个名称—值对，如颜色和选装配件。这个函数必须能够像下面这样进行调用：
# car = make_car('subaru', 'outback', color='blue', tow_package=True)打印返回的字典，确认正确地处理了所有的信息。
def make_car(Manufacturer,Model,**infos):
    car={}
    car["Manufacturer"] = Manufacturer
    car["Model"] = Model
    for key,value in infos.items():
        car[key] = value
    return car
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

