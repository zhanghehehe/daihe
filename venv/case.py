# -*- coding: UTF-8 -*-
import math
x = input ("请输入分润方案：") # x=1时表示帮帮等额本息还款方式；x=2时表示帮帮先高后低的还款方式
x = int(x)
if x == 1:  #帮帮等额本息
    a = input ("请输入借款金额：")
    b = input ("请输入借款利率：")
    c = input ("请输入借款周期：")
    a = int(a)
    b = float(b)
    c = int(c)
    d = a/c + a*b
    i = 1
    i = int(i)
    for i in range(c):
        i = i + 1
        if i <= c:
            e = a + a*b - a/c*(i-1)+a*0.03
            print ("第",i,"个月付款金额：",d,"；第",i,"个月提前结清金额：",e)
        else:
            break
elif x == 2:  #帮帮先高后低
    a1 = input ("请输入借款金额：")
    b1 = input ("请输入借款利率：")
    c1 = input ("请输入只付利期周期：")
    f1 = input ("请输入利率及本金周期：")
    a1 = int(a1)
    b1 = float(b1)
    c1 = int(c1)
    f1 = int(f1)
    d1 = a1*b1
    e1 = a1 + a1*b1+a1*0.03
    d2 = a1*b1 + a1/f1
    i = c1
    i = int(1)
    for i in range(c1):
        i = i + 1
        if i <= c1:
            print ("第",i,"个月付款金额：",d1,"；第",i,"个月提前结清金额：",e1)
        else:
            break
    for i in range(f1):
        i = i + 1
        if i <= f1:
            e2 = a1 + a1*b1 - a1/f1*(i-1)+a1*0.03
            print ("第",i + c1,"个月付款金额：",d2,"；第",i + c1,"个月提前结清金额：",e2)
        else:
            break
else:
    print ("没有该种还款方式,请从新选择")

