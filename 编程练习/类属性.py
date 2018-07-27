# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1
# 首先创建类实例，是怎么一个过程？代码如何知道用户创建了一个类实例? 通过百度，我们知道，一个类，如果被实例化，就会默认执
# 行一次init()函数， 那么，我们就可以在init()函数里对count属性进行累加。 那我们到底是Student.count+=1 呢？ 还是
# self.count+=1 ? 分析一下， self.count,是实例本身的的属性，一个实例对应一个count, 那这样是无法 统计总数的。
# 所以必须用类的属性，类的属性是所有实例都能共享访问的。 所以就写Student.count+=1

# 测试:
if Student.count != 0:
    print('测试失败1!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败2!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败3!')
        else:
            print('Students:', Student.count)
            print('测试通过!')