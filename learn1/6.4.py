################################################6.4嵌套###############################################################
# 6-7 人 ：在为完成练习6-1而编写的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个名为people 的列表中。
# 遍历这个列表，将其中每个人的所有信息都打印出来。
people1 = {"first_name":"周","last_name":"一璇","age":18,"city":"南昌"}
people2 = {"first_name":"叶","last_name":"成龙","age":24,"city":"珠海"}
people3 = {"first_name":"林","last_name":"俊杰","age":36,"city":"台北"}
peoples = [people1,people2,people3]
for people in peoples :
    print(people)

# 6-8 宠物 ：创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；在每个字典中，包含宠物的类型及其主人的名字。
# 将这些字典存储在一个名为pets的列表中，再遍历该列表，并将宠物的所有信息都打印出来。
dog = {"master":"dd","color":"white"}
cat = {"master":"cc","color":"black"}
pets =[dog,cat]
for pet in pets:
    print(pet)

# 6-9 喜欢的地方 ：创建一个名为favorite_places 的字典。在这个字典中，将三个人的名字用作键；对于其中的每个人，都存储他
# 喜欢的1~3个地方。为让这个练习更有趣些，可让一些朋友指出他们喜欢的几个地方。遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。

favorite_places = {"p1":["zhuhai","shanghai","shenzhen"],"p2":["hangzhou"],"p3":["suzhou","gaungzhou"]}
for name,places in favorite_places.items():
    print(name.title())
    for place in places:
        print(place.title())

# 6-11 城市 ：创建一个名为cities 的字典，其中将三个城市名用作键；对于每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该
# 城市的事实。在表示每座城市的字典中，应包含country 、population 和fact 等键。将每座城市的名字以及有关它们的信息都打印出来。
cities = {
    "shanghai":{
        "country":"zhongguo",
        "pop":75000000
    },
    "dongjing":{
        "country":"riben",
        "pop": 100000000
    },
    "niuyue": {
        "country": "meiguo",
        "pop": 20000000
    }
}
for city,mes in cities.items():
    print(city+" "+str(mes))
