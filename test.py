import os

# 一个装饰器
def log(func):
    def wrapper(*args, **kwargs):
        print("use function: ", func.__name__)
        return func(*args, **kwargs)
    return wrapper


step = 0


@log
def getAllFiles(path):
    for file in os.listdir(path):  # 遍历当前目录下所有文件
        filePath = os.path.join(path, file)  # 生成当前目录下文件的绝对路径
        if os.path.isfile(filePath):  # 如果这个路径是文件而不是文件夹则找到一个文件
            print("get file: ", filePath)
        else:   # 如果这个路径是文件夹，则递归调用此函数
            getAllFiles(filePath)


# getAllFiles(r"C:\Users\zhidong\PycharmProjects\exercise\github\spider")

# class Test:
#     def test(self, path):
#         self.mypath = path
#         print(type(self.mypath))
#         print(type(path))
#
# mytest = Test()
#
# mytest.test("a")


class A(object):
    class_var = "类变量"  # 类变量

    __slots__ = ("age", "instance_var")

    def __init__(self):
        self.instance_var = "实例变量"  # 实例变量？


s = A()
s.age = 18 #
print(s.age)

class B(A):
    __slots__ = "another_var"

s_b = B()
s_b.another_var = 18
print(s_b.another_var)
# s_b.three = 3
# print(s_b.three)
s_b.age = 18
print(s_b.age)
# s = A()  # 创建类A的一个实例s
# print(1, s.class_var)  # 实例s 没有实例变量class_var 所以会 : 输出类变量class_var
# print(2, s.instance_var)  # 输出“实例变量”
# # del s.class_var  # 实例s 没有实例变量class_var, 而类变量是不能删除的, 所以会：报错
# s.class_var = "实例变量"  # 类变量不能通过类实例直接修改， 所以这时会：创建一个实例变量class_var , 真正的类变量class_var被隐藏起来了
# print(3, s.class_var)  # 输出：实例变量
# print(4, A.class_var)  # 输出: 类变量
# del s.class_var  # 删除s 的实例变量class_var, 类变量class_var就出来了
# print(5, s.class_var)  # 输出：类变量
# A.class_var = "通过类名来改变类变量"
# print(6, s.class_var)  # 输出：通过类名来改变类变量
# print(7, A.class_var)  # 输出：通过类名来改变类变量
# k = A()  # 新建一个实例k
# print(8, k.class_var)  # 因为类变量是所有类实例共享的，所以输出：通过类名来改变类变量
