# -*- coding:utf-8 -*-
'''
Created on 2016. 11. 25.

@author: mskim
'''

from django import template

register = template.Library()

@register.filter(name='convert_spliter')
def convert_spliter(value, spliter):
    #return '\n'.join(value.split(spliter))
    return '\n'.join(list(set(value.split(spliter))))   # add to remove duplicate 

@register.filter(name='get_value')
def get_value(dic, key):
    return dic.get(key)

@register.filter(name='isin')
def isin(val, l):
    if l==None: return False
    return True if val in l else False
    