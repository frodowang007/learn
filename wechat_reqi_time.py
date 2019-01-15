#!/usr/bin/env python
#-*- coding:utf-8 -*-

from datetime import datetime,timedelta

def get_days():
    user_input = input("请输入您的微信注册天数：")
    user_input_max = (datetime.now() - datetime.strptime('2011-1-21','%Y-%m-%d')).days
    if user_input.isdigit() and 0 <= int(user_input) <= user_input_max:
        return int(user_input)
    elif int(user_input) > user_input_max:
        print("您输入的天数超过了微信的上线天数啦！")
    else:
        print("您输入的内容为非正整数，请重新输入啦！")

def wechat_reqi_time():
    a = get_days()
    reqi_time = datetime.now() - timedelta(days=a)
    print(reqi_time)

wechat_reqi_time()