# -*- coding: utf-8 -*-
#使用函数求解一元二次方程
import math

def  quadratic(a, b, c):
    deta =  b*b-4*a*c
    if deta < 0:
        print("参数错误")
        return
    else:
        x1 = (-b+ math.sqrt(deta))/(2*a)
        x2 =  (-b- math.sqrt(deta))/(2*a)
        print("x1 = %d x2 = %d", x1, x2)
    return
if __name__ == '__main__':
    quadratic(1, 3, 1);
