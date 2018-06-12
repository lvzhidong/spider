#! user/bin/env python3
# -*- coding:utf-8 -*-

import requests
import re
from urllib import request
import time, random
import os



def getImageList(url_want):
    headers = random.choice([
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'},
        {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"},
        {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"}
    ])
    print("使用header: ", headers)

    print("开始处理：", url_want)
    try:
        process_content = requests.get(url=url_want, headers=headers, timeout=5)
    except requests.exceptions.ConnectTimeout:
        print("处理 %s 异常" % url_want)
        return
    process_content.encoding = "utf8"
    url_content = process_content.text
    # print("网页源代码：", url_content)
    match_pattern = re.compile("window\.open\('[a-zA-z]+://[^\s]*\)")
    try:
        title = re.search("<title>.*\[[0-9]*P\]", url_content).group()[7:-5]
        print("网页标题：", title)
    except:
        print(url_want, "can not get a title")
        return

    print("开始下载 :", title)
    imaget_url_list = re.findall(match_pattern, url_content)
    print("图片地址列表: ", imaget_url_list)
    for i in imaget_url_list:
        image_url = re.search('http.*jpg', i).group()
        image_name = re.search('[0-9]*\.jpg', image_url).group()
        print(image_url)
        try:
            req = request.Request(url=image_url, headers=headers)
        except requests.exceptions.ConnectTimeout:
            print("获取图片 %s 失败" %image_url)
            continue
        pic = request.urlopen(req).read()
        file_save_dir = "C:\\Users\\zhidong\\PycharmProjects\\exercise\\pictures\\"+title + "\\"
        if not os.path.exists(file_save_dir):
            os.makedirs(file_save_dir)
        file_path = file_save_dir + str(image_name)
        fp = open(file_path, "wb")
        fp.write(pic)
        fp.close()
        time.sleep(random.random())
    return


url_want_list = [
                 # "http://d2.sku117.info/pw/htm_data/21/1806/1191781.html",
                 # "http://d2.sku117.info/pw/htm_data/21/1806/1191780.html",
                 # "http://d2.sku117.info/pw/htm_data/21/1806/1191779.html",
                 # "http://d2.sku117.info/pw/htm_data/21/1806/1191778.html",
                 # "http://d2.sku117.info/pw/htm_data/21/1806/1191777.html",
                 # "http://d2.sku117.info/pw/htm_data/21/1806/1191776.html",
                 # "http://d2.sku117.info/pw/htm_data/21/1806/1191775.html",
                 # "http://d2.sku117.info/pw/htm_data/21/1806/1191774.html",
                 # "http://d2.sku117.info/pw/htm_data/21/1806/1191773.html",
                 # "http://d2.sku117.info/pw/htm_data/21/1806/1191772.html",
                 # "http://d2.sku117.info/pw/htm_data/21/1806/1191771.html",
                 # "http://d2.sku117.info/pw/htm_data/21/1806/1191770.html",
                 # "http://d2.sku117.info/pw/htm_data/21/1806/1191769.html",
                 # "http://d2.sku117.info/pw/htm_data/21/1806/1191768.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1191767.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1191766.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1191765.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1191764.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1191763.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1191762.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189988.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189987.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189985.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189984.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189983.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189982.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189980.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189979.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189977.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189975.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189972.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189971.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189970.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189969.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189967.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189966.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189965.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189964.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189962.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189961.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189958.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189957.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189956.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189955.html",
                 "http://d2.sku117.info/pw/htm_data/21/1806/1189954.html"]

for url in url_want_list:
    getImageList(url)
