f = open("prueba.txt",'r')
ins=[]
ins2=[]
for w in f:
    w=w.replace(" ", "")
    w=w.replace("\n", "")
    w=w[:3]+ ','+w[3:]
    ins.append(w)
if (ins[len(ins)-1]==','):
        ins=ins[:(len(ins)-1)]
for i in ins:
    ins2.append(i.split(","))
print(ins2)
f.close()
"""
class Reg:
    #Atributos 
    Nombre = ""
    Valid = ""
    Tag = ""
    Value = ""

    def __init__(self,Nombre,Valid, Tag, Value):
        self.Nombre = Nombre
        self.Valid = Valid
        self.Tag = Tag
        self.Value = Value
#---Creacion del RAT-------
RAT=[]
cont=1
for i in range(12):
    Nombre = 'R' + str(cont)
    Valid=1
    Tag=' '
    Value=cont
    R=Reg(Nombre,Valid,Tag,Value)
    RAT.append(R)
    cont+=1
#--Impresión del RAT--
R2=[]
for i in RAT:
    rr=[i.Valid, i.Tag, i.Value]
    R2.append(rr)
def print_RAT(R):
    t=0
    for i in range(len(R)):
        if len(str(R[i][2]))>5 and len(str(R[i][2]))>t:
            t=len(str(R[i][2]))-5
    print("       Register Alias Table")
    print("----------------------------------"+"-"*t)
    print("| Register | Valid | Tag | Value"+" "*t+" |")
    for i in range(len(R)):
        print("----------------------------------"+"-"*t)
        print("| R"+str(i+1)+" "*(8-len(str(i+1)))+"| "+str(R[i][0])+"     |  "+str(R[i][1])+"  | "+str(R[i][2])+" "*(t+5-len(str(R[i][2])))+" |")
    print("----------------------------------"+"-"*t)   
    return " "
print_RAT(R2)"""
