from __future__ import (absolute_import,division,print_function,unicode_literals)
#是一种绝对导入包，使用了魔法函数

from urllib.request import urlopen
import json
import pygal
import math
from itertools import groupby

dates = []
months = []
weeks = []
weekdays = []
close = []

"""
#这个网址被墙了，我打不开
json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btcc_close_2017.json'
response = urlopen(json_url)

#读取数据
req = response.read()
#将数据写入文件
with open('btc_close_2017urllib.json','wb') as f:
    f.write(req)

    #加载json格式
file_urllib = json.loads(req)
"""

#将数据加载到一个列表里
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)
    #打印每一天的信息
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append( btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

def draw_line(x_data,y_data,title,y_legend):
    """绘制图像"""
    xy_map = []
    for x,y in groupby(sorted(zip(x_data,y_data)),key = lambda _: _[0]):
        y_list = [v for _,v in y]
        xy_map.append([x,sum(y_list)/len(y_list)])
    x_unique,y_mean = [*zip(*xy_map)]
    #pypal实现折线图
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend,y_mean)
    line_chart.render_to_file(title+'.svg')
    return line_chart

idx_week = dates.index('2017-12-01')
wd = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekdays_int,close[1:idx_week],'收盘价星期均值(￥）','星期均值')
line_chart_weekday.x_labels = ['周一','周二','周三','周四','周五','周六','周日']
line_chart_weekday.render_to_file('收盘价星期均值.svg')

with open('收盘价DashBoard.html','w',encoding = 'UTF-8') as html_file:
    html_file.write('<html><head><title>收盘价DashBoard<meta charset = "utf-8"></title></head><body>/n')
    for svg in [
        '收盘价对数变换折现图(￥).svg','收盘价日月均值（￥）.svg','收盘价星期均值(￥）.svg','收盘价星期均值.svg','收盘价折现图(￥).svg'
        ]:
        html_file.write('<object type ="image/svg+xml"data = "{0}"height = 500></object>\n'.format(svg))
        html_file.write('</body></html>')






