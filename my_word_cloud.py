#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2019/1/9

import pickle
from os import path
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

class MyWordCloud():
    def __init__(self,txt_name,bg_img,):
        """
        初始化文本文件，已经背景图片
        :param txt_name: txt文件所在的路径
        :param bg_img: 背景图片所在的路径
        """
        self.txt_name = txt_name
        self.bg_img = bg_img

    def get_text(self):
        """
        读取文本内容，用jieba进行分词
        :return: 重新组合成的新文本，用于制作词图云的内容
        """
        text = ''
        with open(self.txt_name, 'r', encoding='utf8') as fin:
            for line in fin.readlines():
                line = line.strip('\n')
                text += ' '.join(jieba.cut(line))
        return text

    def load_bgimg(self):
        """
        读取背景图片，以及尺寸，作为的词图云的大小
        :return: 背景图片，高，宽
        """
        backgroud_Image = plt.imread(self.bg_img)
        backgroud_Image_shape = backgroud_Image.shape
        backgroud_Image_height = backgroud_Image_shape[0]
        backgroud_Image_width = backgroud_Image_shape[1]
        print('加载图片成功！')
        return backgroud_Image,backgroud_Image_height,backgroud_Image_width

    def build_word_cloud(self):
        """
        开始制作词图云
        :return: None
        """
        bg_img,height,width = self.load_bgimg()
        '''设置词云样式'''
        wc = WordCloud(
            background_color='black',# 设置背景颜色
            width=width,
            height=height,
            #mask=backgroud_Image,# 设置背景图片
            font_path='C:\Windows\Fonts\simkai.ttf',  # 若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
            max_words=800, # 设置最大现实的字数
            stopwords=STOPWORDS,# 设置停用词
            max_font_size=80,# 设置字体最大值
            #random_state=30# 设置有多少种随机生成状态，即有多少种配色方案

        )
        wc.generate_from_text(self.get_text())
        print('开始加载文本')
        #改变字体颜色
        img_colors = ImageColorGenerator(bg_img)

        #字体颜色为背景图片的颜色
        wc.recolor(color_func=img_colors)
        # 显示词云图
        plt.imshow(wc)
        # 是否显示x轴、y轴下标
        plt.axis('off')
        plt.show()
        # 获得模块所在的路径的
        d = path.dirname(__file__)
        # os.path.join()：  将多个路径组合后返回
        wc.to_file(path.join(d, "h11.jpg"))
        print('生成词云成功!')

if __name__ == '__main__':
    txt_name = 'liuyan2.txt'
    bg_img = '1547050121341.jpg'
    MyWordCloud(txt_name,bg_img).build_word_cloud()