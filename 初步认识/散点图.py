import matplotlib.pyplot as plt

x_values = list(range(1,1000))
y_values = [x**2 for x in x_values]
#平方值还可以这么算！！！又学到了

#使用颜色映射，使颜色从较小值到较大值渐变以突出分布
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=40)
#c是字体颜色的标识，edgecolors是轮廓

#设置图表标题，并给坐标轴加上标题
#fontsize指定文字大小
plt.title("Squres Numbers",fontsize=24)
#xlable，ylable能为x，y轴设置标题
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])

#plt.savefig是使保存文件
plt.savefig('squares_plot.png',bbox_inches = 'tight')
#plt.show和plt.savefig不可以同时打开