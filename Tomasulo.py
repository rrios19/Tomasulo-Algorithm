from io import open


text=open("Code.txt", "r")
codigo=text.readlines()
text.close()


def separar(codigo):
    code=[]
    code2=[]
    op=[]
    rd=[]
    ra=[]
    rb=[]
    for i in codigo:
        i = i.replace(" ", "")
        code.append(i)

    for i in code:
        op.append(i[0:3])

    for i in code:
        i = i.replace(i[0:3], "")
        code2.append(i)

    codigo.clear()
    for i in code2:
        i = i.replace("\n", "")
        codigo.append(i)

    code.clear()

    for i in codigo:
        i = i.split(",")
        code.append(i)

    a=0
    for i in code:
        rd.append(code[a][0])
        ra.append(code[a][1])
        rb.append(code[a][2])
        a+=1

    return op, rd, ra, rb


print(separar(codigo))


R = [[1, "~",123457656789876567876],
    [1, "~", 2474],
    [1, "~", 35674],
    [1, "~", 4],
    [1, "~", 5],
    [1, "~", 6],
    [1, "~", 765759765436756987],
    [1, "~", 8],
    [1, "~", 9],
    [1, "~", 109876567898767898765],
    [1, "~", 119876545678],
    [1, "~", 1246898765678987657655]]



def print_RAT(Tabla):
    t=0
    v=0
    r=0
    for i in range(len(R)):
        if (len(str(R[i][2]))>5) and (len(str(R[i][2]))>t):
            t=len(str(R[i][2]))-5
    print("       Register Alias Table")
    print("----------------------------------"+"-"*t)
    print("| Register | Valid | Tag | Value"+" "*t+" |")
    for i in range(len(R)):
        print("----------------------------------"+"-"*t)
        print("| R"+str(i+1)+" "*(8-len(str(i+1)))+"| "+str(R[i][0])+"     |  "+str(R[i][1])+"  | "+str(R[i][2])+" "*(t+5-len(str(R[i][2])))+" |")
    print("----------------------------------"+"-"*t)   
    return " "

print_RAT(R)

