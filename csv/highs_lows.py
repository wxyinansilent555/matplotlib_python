from matplotlib import pyplot as plt
from datetime import datetime
import csv

#从文件中获取最高气温
#在文件中获取日期,最高气温和最低气温
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates=[]
    highs=[]
    lows =[]

    for row in reader:
        try:

            current_date = datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])
            low  = int(row[3])
        except ValueError:
            #如过有数据丢失的情况
            #remove，continue...都是可行的
            print(current_date,'missing data')
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

#显示图像
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor = 'blue',alpha=0.1)

#设置图形的格式
plt.title("Daily high and low temperatures - 2014\nDeath Valley,CA",fontsize = 24)
plt.xlabel("title",fontsize = 20)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)",fontsize = 16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()

"""
for index,column_header in enumerate(header_row):
    #获取每个元素的索引和值
    print(index,column_header)
"""