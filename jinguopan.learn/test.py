#coding=utf-8
import math
def move(x, y, step, angle=0,angle2=7,angle3=8):
    '''

    :param x:
    :param y:
    :param step:
    :param angle:
    :return:
    '''
    '''
    :param x:
    :param y:
    :param step:
    :param angle:
    :return:返回 nx,ny
    '''
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    print("angle ",(angle))
    print("angle2 ",(angle2))
    print("angle3 ",(angle3))
    return nx, ny