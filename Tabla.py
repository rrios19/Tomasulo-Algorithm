#from io import open

#codigo=open("Code.txt", "r")
#text=codigo.readlines()
#codigo.close()

R = [[1, "~",123457656789876567876],
    [1, "~", 2474],
    [1, "~", 35674],
    [1, "~", 4],
    [1, "~", 5],
    [1, "~", 6],
    [1, "~", 7657597654367569],
    [1, "~", 8],
    [1, "~", 9],
    [1, "~", 109876567898767898765],
    [1, "~", 119876545678],
    [1, "~", 1246898765678987657655]]



def print_RS(Tabla):
    v=0
    tag="~"
    
    v_size=0
    t_cell=0
    c=int(input("Ingrese el tamaño: "))
    t_size=len(str(c))
    if t_size>3:
        t_cell=t_size-3
    sub=1
    for i in R:
        if len(str(i[2]))>int(v_size):
            v_size = len(str(i[2]))
    print(" "*(t_size+3)+"    Source 1"+" "*(6+t_cell)+"|   Source 2  ")
    print(" "*(t_size+3)+"-"*(36+len(str(c))))
    print(" "*(t_size+3)+"| V | Tag "+" "*t_cell+"| Value | V | Tag | Value |")
    print(" "*(t_size+3)+"-"*(36+len(str(c))))
    while sub<=c:
        print(" a"+str(sub)+" "*(t_size-len(str(sub))+1)+"| "+str(v)+" | "+str(tag)+" "*(3+t_cell)+"| "+str(R[sub-1][2]))
        print(" "*(t_size+3)+"-"*(36))
        sub+=1
        
print_RS(R)
