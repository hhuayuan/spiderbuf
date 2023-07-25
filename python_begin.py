# coding=utf-8

import requests

print('中文')

a = 2
b = '张三'
c = 'ddddddd'
print(a,b,c)

d = 2
print(a - d)

if a == 1:
    print('等于1')
elif a == 2:
    print('等于2')
else:
    print('不等于')

# for i in range(0, 10):
#     print(i)

while  a < 10:
    a += 1
    print(a)

print("中文")

lst = ['张三', '李四', '王五']

dict = {'张三':'a2', '李四':'b3'}

print(dict['张三'])

for item in dict.keys():
    print(dict[item])

# f = open('abc.txt', 'w', encoding='utf-8')
# f.write('这是写入文件的内容')
# f.close()
f = open('abc.txt', 'r', encoding='utf-8')
s = f.read()
f.close()
print(s)

