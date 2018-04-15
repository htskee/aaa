#!/use/bin/evn python
# _*_ coding:utf-8 _*_
number = int(input("请输入一个整数 "))
zuida = int(input("最大乘到几"))

print("Here's your table ")
# for i in range(1, zuida + 1):
#     s = number * i
#     print(str(number), '*', str(i), "=", str(s))
while zuida > 0:
    s = number * zuida
    zuida += -1
    print(str(number), '*', str(zuida + 1), "=", str(s))