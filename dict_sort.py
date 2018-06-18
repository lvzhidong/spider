#! user/bin/env python3
# -*- coding:utf-8 -*-

my_dict = {1: "a", 2: "b", -1: "c"}

print(sorted(my_dict.items(), key=lambda x: x[0], reverse=True))

class Screen(object):
    __slots__ = ("__width", "__height")

    @property    # 读
    def width(self):
        return self.__width

    @width.setter  # 写
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def resolution(self):
        return self.__width * self.__height


s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

