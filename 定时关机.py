import os
import datetime
import time

def daojishi(shi,fen,miao):
    t2=shi*3600+fen*60+miao
    print('好的，'+str(t2)+'秒后将关机')
    time.sleep(t2)
    os.system('shutdown /s /t 1')

def dingshi(nian,yue,ri,shi,fen,miao):
    t1=datetime.datetime.now()
    t2=datetime.datetime(nian,yue,ri,shi,fen,miao)
    t3 = t2 - t1
    print('好的，' + str(t3.seconds) + '秒后将关机')
    time.sleep(t4.seconds)
    os.system('shutdown /s /t 1')

def benridingshi(shi,fen,miao):
    t1=datetime.datetime.now()
    t2=datetime.datetime(t1.year,t1.month,t1.day,shi,fen,miao)
    t3=t2-t1
    print('好的，' + str(t3.seconds) + '秒后将关机')
    time.sleep(t3.seconds)
    os.system('shutdown /s /t 1')

def a():
    if int(b)==0:
        print('电脑将在h时m分s秒后关机')
        daojishi(int(input('h:')),int(input('m:')),int(input('s:')))

    elif int(b)==1:
        print('电脑将于y年m月d日h时M分s秒关机')
        dingshi(int(input('y:')),int(input('m:')),int(input('d:')),int(input('h:')),int(input('M:')),int(input('s:1')))

    elif int(b)==2:
        print('电脑将于h时m分s秒关机')
        benridingshi(int(input('h:')),int(input('m:')),int(input('s:')))

b=input('倒计时关机请按0，非本日内定时关机请按1，本日内定时关机请按2')
a()


