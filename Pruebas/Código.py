# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 01:11:31 2021

@author: IPB
"""
def cod(R): 
    f = open(R,'r')
    ins=[]
    ins2=[]
    c=0
    for w in f:
        w=w.replace(" ", "")
        w=w.replace("\n", "")
        w=w[:3]+ ','+w[3:]
        ins.append(w)
        c=c+1
    if (ins[len(ins)-1]==','):
            ins=ins[:(len(ins)-1)]
    for v in ins:
        ins2.append(v.split(","))
    f.close()
    return ins2,c