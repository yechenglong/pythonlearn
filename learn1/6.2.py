#########################################6.2使用字典##################################################################

# 6-1 人 ：使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。该字典应包含键first_name 、last_name 、age
# 和city 。将存储在该字典中的每项信息都打印出来。
people = {"first_name":"周","last_name":"一璇","age":18,"city":"南昌"}
print(people["first_name"]+people["last_name"]+" "+str(people["age"])+" "+people["city"])

# 6-2 喜欢的数字 ：使用一个字典来存储一些人喜欢的数字。请想出5个人的名字，并将这些名字用作字典中的键；想出每个人喜欢的一
# 个数字，并将这些数字作为值存储在字典中。打印每个人的名字和喜欢的数字。为让这个程序更有趣，通过询问朋友确保数据是真实的
favorite_nums = {"a":1,"b":2,"c":3,"d":4,"e":5}
print("a 喜欢 " + str(favorite_nums["a"]))
print("b 喜欢 " + str(favorite_nums["b"]))
print("c 喜欢 " + str(favorite_nums["c"]))
print("d 喜欢 " + str(favorite_nums["d"]))
print("e 喜欢 " + str(favorite_nums["e"]))


