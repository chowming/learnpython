# -*- coding: utf-8 -*-
# test unicode utf-8
# name=input("请输入你的名字：")
# print("你输入的名字为：", name)

print(ord("你"))
print(ord("我"))

name="我是中国人"
nameordlist=[]
for ch in name:
    print(ord(ch))
    nameordlist.append(ord(ch))

print(nameordlist)

for ch in nameordlist:
    print(chr(ch))


str="我是中国人"
print(str, '的utf-8编码', str.encode('utf-8'))
print(str, '的utf-16编码', str.encode('utf-16'))
print(str, "的长度：", len(str))

str='hello world'

print(str, '的utf-8编码', str.encode('utf-8'))
print(str, '的utf-16编码', str.encode('utf-16'))

print(str, "的长度：", len(str))


month=9
day=18
year=2019

todaystr="today is %d/%d/%d" % (year, month, day)
print(todaystr)

invalid=0xffffffffffffffff

print("invalid 64 %d" % invalid)

todaystr="today is {0}/{1}/{2}".format(year,month,day)

print(todaystr)


#this is test for list and tuple


workmate=["h", "z", "s", "w"]
print(workmate)

print(len(workmate))

for i in range(len(workmate)):
    print(workmate[i])

print(workmate[-1])

workmate.append("l")
print(workmate[-1])

workmate.pop()

print(workmate)

workmate[-1]="haha"
print(workmate)

workmate=["wh", 123, 1.2131, "我是中国人", print, ["1231", {1,2,3}]]
print(workmate)


classmate=("xjh", "lt", "zj")
print(classmate)

#one element tuple
onet = (1,)
print(onet)
