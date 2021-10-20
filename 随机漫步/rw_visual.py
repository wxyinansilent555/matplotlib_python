import matplotlib.pyplot as plt
from random_walk import  RandomWalk

#只要程序一直运行，就不断的模拟随机漫步
while True:

    #创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()

    #隐藏坐标轴
    current_axes = plt.axes()
    current_axes.get_xaxis().set_visible(False)#不知道为什么隐藏坐标轴和突出起点和终点的代码没有用，有待观察
    current_axes.get_yaxis().set_visible(False)#找到问题所在，必须将plt.axes赋予给一个变量使其初始化

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c = point_numbers,cmap = plt.cm.Blues,edgecolor = 'none',s = 1)
    plt.show()

    #突出起点和终点
    plt.scatter(0,0,c= 'green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c = 'red',edgecolors='none',s=100)



    #设置绘图窗口的尺寸，以适应屏幕的大小
    plt.figure(figsize=(10,6))

    keep_running = input("make another walk?(y/n")
    if keep_running == 'n':
        break
