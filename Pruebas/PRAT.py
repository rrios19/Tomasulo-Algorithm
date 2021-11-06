# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 01:22:41 2021

@author: IPB
"""
def print_RAT(RAT):
    R=[]
    for u in RAT:
        rr=[u.Valid, u.Tag, u.Value]
        R.append(rr)
    t=0
    for i in range(len(R)):
        if len(str(R[i][2]))>5 and len(str(R[i][2]))>t:
            t=len(str(R[i][2]))-5
    print("       Register Alias Table")
    print("-----------------------------------"+"-"*t)
    print("| Register | Valid | Tag  | Value"+" "*t+" |")
    for i in range(len(R)):
        print("-----------------------------------"+"--"*t)
        print("| R"+str(i+1)+" "*(8-len(str(i+1)))+"| "+str(R[i][0])+"     |  "+str(R[i][1])+"  | "+str(R[i][2])+" "*(t+5-len(str(R[i][2])))+" |")
    print("-----------------------------------"+"-"*t)   
    return " "

"""R2=[[1, '..', 1], [1, '..', 2], [1, '..', 3], [1, '..', 4], [1, '..', 5], [1, '..', 6], [1, '..', 7], [1, '..', 8], [1, '..', 9], [1, '..', 10], [1, '..', 11], [1, '..', 12]]
print_RAT(R2)"""

def print_res(AdderRS,SizeRS):
    R=[]

    for u in range(SizeRS):
        rr=[AdderRS[u].Nombre, AdderRS[u].Valid1, AdderRS[u].Tag1, AdderRS[u].Value1, AdderRS[u].Valid2, AdderRS[u].Tag2, AdderRS[u].Value2, AdderRS[u].contCiclos]
        R.append(rr)
    t=0
    for i in range(len(R)):
        if len(str(R[i][2]))>5 and len(str(R[i][2]))>t:
            t=len(str(R[i][3]))-5
    print("                 ")
    print("                 RS suma ")
    print("-----------------------------------------")
    print("    |     Source 1    |     Source 2    |")
    print("-----------------------------------------")
    print("| N | V | Tag | Value"+" "*t+" | V | Tag | Value"+" "*t+" |")
    for i in range(len(R)):
        if str(R[i][2])!=" ~~ ":
            u=len(str(R[i][2]))
        else:
            u=0
        if str(R[i][5])!=" ~~ ":
            c=len(str(R[i][5]))
        else:
            c=0
        print("-----------------------------------------")
        print("| "+str(R[i][0])+"| "+str(R[i][1])+" | "+str(R[i][2])+" "*u+"|   "+str(R[i][3])+" "*(t+4-len(str(R[i][3])))+"| "+str(R[i][4])+" | "+str(R[i][5])+" "*c+"|   "+str(R[i][6])+" "*(t+3-len(str(R[i][6])))+" |"+str(R[i][7]))
    print("-----------------------------------------")
   
    return " "
