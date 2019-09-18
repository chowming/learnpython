# -*- coding: utf-8 -*-


# while True:
#     inputnum = int(input("输入数字："))
#     if inputnum > 90:
#         print(inputnum, ">90")
#     elif inputnum > 80:
#         print(inputnum, ">80")
#     else:
#         print(inputnum, "<=80")
#
#
#     if inputnum == -1:
#         break


names=["xiaoguai", "huangnian", "paoshen"]

for name in names:
    print(name)

sum=0
for i in range(100):
    sum+=i
print(sum)

# for i in range(10):
#     print(i)
#
i = 0
sum = 0
while i < 100:
    sum+=i
    i+=1

print(sum)

for i in range(1, 100, 2):
    if i > 80:
        break
    print(i)

for i in range(0, 1000, 50):
    if i % 100 == 0:
        continue
    print(i)


names=["chowming", "what", "your"]
ages=[123, 1231, 3123]

for i in range(len(names)):
    print(names[i], ages[i])

dic = {"chowming": 123, "waht": 1231, "your":123132}

print(dic)
for i in dic.keys():
    print(dic[i])

for i in dic.:
    print i