#!/use/bin/evn python
# _*_ coding:utf-8 _*_
import easygui
flavor =easygui.buttonbox("what is your favorite ice cream flavor?",
                          choices=['vanilla', 'Chocolate', 'Strawberry'])
easygui.msgbox("you picked " + flavor)




