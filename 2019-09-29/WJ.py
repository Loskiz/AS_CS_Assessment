#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 22:55:56 2019

@author: zhangletian
"""

# coding: utf-8  有中文，所以这样，不然乱码
# 本代码旨在对战粮及其后吴京先生主演或有重要话题度的电影进行词频分析
import jieba  # 分词包
import numpy  # numpy计算包
import codecs  # codecs提供的open方法来指定打开的文件的语言编码，它会在读取的时候自动转换为内部unicode
import re
import pandas as pd
import matplotlib.pyplot as plt
from urllib import request
from bs4 import BeautifulSoup as bs
import matplotlib
import xlwt
import operator
from functools import reduce
from wordcloud import WordCloud

MovieList=['26266893','30413052','27114417','26363254','26284595','26125779','23788440','24753810']

def getComments(pageNum,movie):
    eachCommentList = []
    eachDateList = []
    if pageNum > 0:
        start = (pageNum-1) * 20
    else:
        return False
    requrl = 'https://movie.douban.com/subject/{}/comments'.format(movie) + \
        '?' + 'start=' + str(start) + '&limit=20' + '&sort=new_score&status=P'

    print(requrl)

    resp = request.urlopen(requrl)
    html_data = resp.read().decode('utf-8')  # 有中文，所以要转码
    soup = bs(html_data, 'html.parser')  # 用美丽汤先进先进行分析
    # 找到所有<div, class = 'comment'>的部分
    comment_div_lits = soup.find_all('div', class_='comment')
    for item in comment_div_lits:
        if item.find_all('p'):
            # 准确的找到comment所在的那个<span>
            eachCommentList.append(item.find_all('span', class_='short')[0].string)
            tmpDate = item.find_all('span')[-2].string
            eachDateList.append(tmpDate)
    return eachCommentList, eachDateList  # 组合评论

def main():
    commentList = []
    dateList = []
    for j in MovieList:
        for i in range(10):
            num = i + 1
            [commentList_temp, dateList_temp] = getComments(num,j)
            commentList.append(commentList_temp)
            dateList.append(dateList_temp)
    commentList = reduce(operator.add, commentList)
    dateList = reduce(operator.add, dateList)

    dataTmp = {'comments': commentList[:], 'date': dateList[:]}
    df2 = pd.DataFrame(dataTmp)
    pd.DataFrame(df2).to_excel("text-movie.xls",
                               sheet_name="sheet1", index=False, header=True)

    comments = ''
    for k in range(len(commentList)):
        comments = comments + (str(commentList[k])).strip()

    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    filterdata = re.findall(pattern, comments)  # 过滤标点 用正则表达式
    cleaned_comments = ''.join(filterdata)

    segment = jieba.lcut(cleaned_comments)
    # 请实践 -- 调整分词
    #https://github.com/fxsjy/jieba  结巴分词的网站
    #使用 add_word(word, freq=None, tag=None) 和 del_word(word) 可在程序中动态修改词典。
    #使用 suggest_freq(segment, tune=True) 可调节单个词语的词频，使其能（或不能）被分出来。
    jieba.add_word('说真的')
    jieba.del_word('今天天气')
    jieba.suggest_freq(('说', '真的'), False)
    
    words_df = pd.DataFrame({'segment': segment})  # 割词

    stopwords = pd.read_csv("stopwords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'],
                            encoding='utf-8')
    # -- 请实践： 停止词， 在 stopwords.txt 文件中，可以添加和修改停止词。 
    # 例如将 “电影” 这个词加入到 stopwords文件中，
    with open("stopwords.txt") as f1:
        a1=f1.readlines()
    a1.append('\n')
    a1.append('电影\n')
    #a1.append('说\n')
    #a1.append('真的\n')
    with open("stopwords.txt",'w') as f2:
        f2.writelines(a1)
    

    
    words_df = words_df[~words_df.segment.isin(stopwords.stopword)]

    words_stat = words_df.groupby(by=['segment'])[
        'segment'].agg({"计数": numpy.size})
    words_stat = words_stat.reset_index().sort_values(
        by=["计数"], ascending=False)
    print(words_stat.head())  # 数词

    wordcloud = WordCloud(font_path="simhei.ttf",
                          background_color="white", max_font_size=80)
    word_frequence = {x[0]: x[1] for x in words_stat.head(1000).values}  # 画图

    word_frequence_list = []
    for key in word_frequence:
        temp = (key, word_frequence[key])
        word_frequence_list.append(temp)

    wordcloud = wordcloud.fit_words(dict(word_frequence_list))
    plt.figure()
    plt.imshow(wordcloud)
    plt.show() 

main()
