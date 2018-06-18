#! user/bin/env python3
# -*- coding:utf-8 -*-

import random
import time


# with open("bigdata.txt", "w") as f:
#     i=0
#     while i <= 10000000:
#         num = random.randint(0, 100000000)
#         f.write(str(num)+"\n")
#         i = i + 1

with open("bigdata.txt", "r") as f:
    start_time = time.time()
    content = f.readlines()
    print(content)
    print(len(content))
    for i in range(len(content)):
        content[i] = int(content[i].strip())
    print(content)
    print(len(content))
    content.sort()
    print(content)
    end_time = time.time()
    print("用时：", end_time - start_time)