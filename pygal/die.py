from random import randint

class Die():
    """一个表示骰子的类"""

    def __init__(self,num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """这模拟骰子滚动的情况，在1-面数之间返回一个随机值"""
        return randint(1,self.num_sides)