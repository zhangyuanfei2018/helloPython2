#!/usr/bin/python
# -*- coding: UTF-8 -*-

#from tkinter import *
'''top = tkinter.Tk()
# 进入消息循环
top.mainloop()'''


'''top = Tk()
a = ['a','b','c','d']
b = ['java','c','c++']
listb = Listbox(top)
listb2 = Listbox(top)
for item in a:
    listb.insert(0,item)
for item2 in listb2:
    listb2.insert(0,item2)
listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()
top.mainloop()
'''

from tkinter import *           # 导入 Tkinter 库
root = Tk()                     # 创建窗口对象的背景色
                                # 创建两个列表
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(root)          #  创建两个列表组件
listb2 = Listbox(root)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)

for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)

listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()
root.mainloop()                 # 进入消息循环