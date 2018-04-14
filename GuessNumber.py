#!/use/bin/evn python
# _*_ coding:utf-8 _*_
import random, easygui

secret = random.randint(1, 100)
guess = 0
tries = 0

easygui.msgbox("""我们来玩个猜数游戏吧,从1-50,你有6次机会""")

while guess != secret and tries < 6:
    guess = easygui.integerbox("请输入你猜的数字")
    if not guess: break
    if guess < secret:
        easygui.msgbox(str(guess) + '太小了,你敢往大里猜吗??' + str(tries+1) + '次')
    elif guess > secret:
        easygui.msgbox(str(guess) + '大一点点' + '第'+ str(tries+1) + '次')
    tries += 1
    
if guess == secret:
    easygui.msgbox("操 你太聪明了!猜对了")
else:
    easygui.msgbox("你的6次机会用完了!!!答案是 " + str(secret))