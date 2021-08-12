# coding:utf-8
class CountList:
    def __init__(self, *args):       #定义一个列表
        self.values = [x for x in args]           #定义列表的值values     #[x for x int args]是获取输入的值 组成一个新的[]
        self.count = {}.fromkeys(range(len(self.values)), 0) #定义列表的键
        #这里使用列表的下标作为字典的键，注意不能用元素作为字典的键
        #因为列表的不同下标可能有值一样的元素，但字典不能有两个相同的键

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]

