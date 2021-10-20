import pygal

from die import Die

#创建一个D6
die_1 = Die()
die_2 = Die(10)

#掷几次骰子，并将结果存储在一个列表中
results= []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#分析结果
#ffrequency频率 重复率
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value  in range(2,max_result+1):
    #range函数的参数是start,end,step
    frequency = results.count(value)
    frequencies.append(frequency)

#对这种数据进行可视化
hist = pygal.Bar()

hist.title = "Result of rolling aD6 Dice and a D10 Dice 50000 times."
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title  = "Result"
hist.y_title  = "Frequencies of Result"


hist.add('D6 + D10',frequencies)
hist.render_to_file('die_visual.svg')   #生成一个svg格式的图片