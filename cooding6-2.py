#!/use/bin/evn python
# _*_ coding:utf-8 _*_
import easygui
flavor = easygui.enterbox("what is you  favor ice cream flavor",default='vanilla')
easygui.msgbox("you picked " + flavor)