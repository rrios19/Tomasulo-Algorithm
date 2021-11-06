# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 23:13:05 2021

@author: IPB
"""
from Código import cod
from PRAT import print_RAT
from PRAT import print_res

SizeRS=4


#------Prueba usando clases---------
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
class BloqueRS:
    #Atributos 
    Nombre = ""
    Valid1 = ""
    Tag1 = ""
    Value1 = ""
    Valid2 = ""
    Tag2 = ""
    Value2 = ""
    contCiclos = 0

    def __init__(self,Nombre,Valid1, Tag1, Value1, Valid2, Tag2, Value2, contCiclos):
        self.Nombre = Nombre
        self.Valid1 = Valid1
        self.Tag1 = Tag1
        self.Value1 = Value1
        self.Valid2 = Valid2
        self.Tag2 = Tag2
        self.Value2 = Value2
        self.Ciclos = contCiclos
class BloqueRSM:
    #Atributos 
    NombreM = ""
    Valid1M = ""
    Tag1M = ""
    Value1M = ""
    Valid2M = ""
    Tag2M = ""
    Value2M = ""
    contCiclosM = 0

    def __init__(self,NombreM,Valid1M, Tag1M, Value1M, Valid2M, Tag2M, Value2M, contCiclosM):
        self.NombreM = NombreM
        self.Valid1M = Valid1M
        self.Tag1M = Tag1M
        self.Value1M = Value1M
        self.Valid2M = Valid2M
        self.Tag2M = Tag2M
        self.Value2M = Value2M
        self.CiclosM = contCiclosM
#---Creacion del RAT-------
RAT=[]
cont=1
for i in range(12):
    Nombre = 'r' + str(cont)
    Valid=1
    Tag='..'
    Value=cont
    r=Reg(Nombre,Valid,Tag,Value)
    RAT.append(r)
    cont+=1
#-----Creacion de RS de sumas---
AdderRS=[]
cont=1
for i in range(SizeRS):
    Nombre = 'A' + str(cont)
    Valid1=' '
    Tag1=" ~~ "
    Value1='  '
    Valid2=' '
    Tag2=" ~~ "
    Value2='  '
    contCiclos=0
    Bloque=BloqueRS(Nombre,Valid1, Tag1, Value1, Valid2, Tag2, Value2, contCiclos)
    AdderRS.append(Bloque)
    cont+=1
#-----Creacion de RS de multiplicación---
AdderRSM=[]
cont=1
for i in range(SizeRS):
    NombreM = 'B' + str(cont)
    Valid1M=' '
    Tag1M=" ~~ "
    Value1M='  '
    Valid2M=' '
    Tag2M=" ~~ "
    Value2M='  '
    contCiclosM=0
    BloqueM=BloqueRSM(NombreM,Valid1M, Tag1M, Value1M, Valid2M, Tag2M, Value2M, contCiclosM)
    AdderRSM.append(BloqueM)
    cont+=1


EjecutandoSuma=[]#almacena instrucciones que estan esperando a cumplir ciclos
CodigoEnsamblador,c=cod("prueba.txt") #lista de instrucciones obtenidas del archivo de texto
Decodificar = [] #almacena instruccion a la que se le hace fetch y esta lista para decodificar, ej: ADD, Rd, R1, R2
clock=0
stop=False
#--------------------------------------------------------------------

    
for e in range(25):
    print('------------------',e,'-----------------------')
    for i in Decodificar:
        print(i)
                     
    #---------------------revisa si hay instrucciones de suma listas para escribir en registro y cambia los tags--------------
    for j in AdderRS:
        if (j.Valid1==1 and j.Valid2==1):
            if j.contCiclos==4:
                for k in RAT:
                    if j.Nombre==k.Tag:
                        for m in AdderRS:
                            if m.Tag1 == k.Tag:
                                m.Value1= j.Value1+j.Value2
                                m.Valid1=1
                                m.Tag1=" ~~ "
                                m.Value2= j.Value1+j.Value2
                                m.Valid2=1
                                m.Tag2=" ~~ "
                        k.Valid=1       
                        k.Tag='..'
                        k.Value=j.Value1+j.Value2
                        #Se vacia estacion de reserva
                        j.Valid1=' '
                        j.Tag1=" ~~ "
                        j.Value1='  '
                        j.Valid2=' '
                        j.Tag2=" ~~ "
                        j.Value2='  '
                        j.contCiclos=0
                j.contCiclos+=1
                    
            else:
                j.contCiclos+=1
    for j in AdderRSM:
        if (j.Valid1M==1 and j.Valid2M==1):
            if j.contCiclosM==6:
                for k in RAT:
                    if j.NombreM==k.Tag:
                        for m in AdderRSM:
                            if m.Tag1M == k.Tag:
                                m.Value1M= j.Value1M*j.Value2M
                                m.Valid1M=1
                                m.Tag1M=" ~~ "
                                m.Value2M= j.Value1M*j.Value2M
                                m.Valid2M=1
                                m.Tag2M=" ~~ "
                        k.Valid=1       
                        k.Tag='..'
                        k.Value=j.Value1M*j.Value2M
                        #Se vacia estacion de reserva
                        j.Valid1M=' '
                        j.Tag1M=" ~~ "
                        j.Value1M='  '
                        j.Valid2M=' '
                        j.Tag2M=" ~~ "
                        j.Value2M='  '
                        j.contCiclosM=0
                j.contCiclosM+=1
                    
            else:
                j.contCiclosM+=1
                
                
            

            
        
                        
            
    #--------------------Se decodifica instruccion de suma---------------------------   
    if Decodificar:
        if ((Decodificar[0][0] == 'add') or (Decodificar[0][0] == 'sub')):
            cont=0
            disp=0#si hay estacion de reserva dispnible
            pos=0#posicion de estacion de reserva disponible
            while disp == 0 and cont<SizeRS:#ciclo revisa si hay espacio en estacion de reserva de sumas 
                if (AdderRS[cont].Valid1 == ' ' and AdderRS[cont].Valid2 == ' '): 
                    pos = cont #posicion del bloque disponible en estacion de reserva de sumas
                    disp=1
                cont+=1
                    
            if disp:#proceso que empieza si hay espacio en estacion de reserva
                for i in range(len(RAT)):
                    if RAT[i].Nombre == Decodificar[0][2]:#busca registro de operando 1
                        if RAT[i].Valid==1:#Revisa si registro esta listo o esta esperando un valor
                            AdderRS[pos].Valid1= RAT[i].Valid 
                            AdderRS[pos].Tag1=' ~~ '
                            AdderRS[pos].Value1 = RAT[i].Value #si registro esta listo se escribe valor de registro en operando 1 de estacion de reserva
                           
                        else: 
                            AdderRS[pos].Valid1= 0
                            AdderRS[pos].Tag1=RAT[i].Tag  #si registro no esta disponible se copia su tag en operando 1 de estacion de reserva
                            
                            
                    
                    if RAT[i].Nombre == Decodificar[0][3]:#busca registro de operando 2
                        if RAT[i].Valid==1:#Revisa si registro esta listo o esta esperando un valor
                            AdderRS[pos].Valid2= RAT[i].Valid
                            AdderRS[pos].Tag2=' ~~ '
                            if Decodificar[0][0] == 'add':
                                AdderRS[pos].Value2 = RAT[i].Value #si registro esta listo se escribe valor de registro en operando 2 de estacion de reserva
                            else:
                                AdderRS[pos].Value2 =-RAT[i].Value
                        else:
                            AdderRS[pos].Valid2= 0
                            AdderRS[pos].Tag2=RAT[i].Tag#si registro no esta disponble se copia su tag en operando 2 de estacion de reserva
                            
                            
                    if RAT[i].Nombre == Decodificar[0][1]:#Se busca registro destino 
                        RAT[i].Valid=0 #
                        RAT[i].Tag = AdderRS[pos].Nombre #se cambia su tag por el nombre de la estacion de reserva de la que esta esperando dato 
                Decodificar.pop(0)
            else:
                print("Estacion de reserva de sumas y restas llena")

        elif Decodificar[0][0] == 'mul':
            cont=0
            disp=0#si hay estacion de reserva dispnible
            pos=0#posicion de estacion de reserva disponible
            while disp == 0 and cont<SizeRS:#ciclo revisa si hay espacio en estacion de reserva de sumas 
                if (AdderRSM[cont].Valid1M == ' ' and AdderRSM[cont].Valid2M == ' '): 
                    pos = cont #posicion del bloque disponible en estacion de reserva de sumas
                    disp=1
                cont+=1
                    
            if disp:#proceso que empieza si hay espacio en estacion de reserva
                for i in range(len(RAT)):
                    if RAT[i].Nombre == Decodificar[0][2]:#busca registro de operando 1
                        if RAT[i].Valid==1:#Revisa si registro esta listo o esta esperando un valor
                            AdderRSM[pos].Valid1M= RAT[i].Valid 
                            AdderRSM[pos].Tag1M=' ~~ '
                            AdderRSM[pos].Value1M = RAT[i].Value #si registro esta listo se escribe valor de registro en operando 1 de estacion de reserva
                           
                        else: 
                            AdderRSM[pos].Valid1M=0
                            AdderRSM[pos].Tag1M=RAT[i].Tag  #si registro no esta disponible se copia su tag en operando 1 de estacion de reserva
                            
                            
                    
                    if RAT[i].Nombre == Decodificar[0][3]:#busca registro de operando 2
                        if RAT[i].Valid==1:#Revisa si registro esta listo o esta esperando un valor
                            AdderRSM[pos].Valid2M= RAT[i].Valid
                            AdderRSM[pos].Tag2M=' ~~ '
                            AdderRSM[pos].Value2M = RAT[i].Value #si registro esta listo se escribe valor de registro en operando 2 de estacion de reserva
                        else:
                            AdderRSM[pos].Valid2M= 0
                            AdderRSM[pos].Tag2M=RAT[i].Tag#si registro no esta disponble se copia su tag en operando 2 de estacion de reserva
                            
                            
                    if RAT[i].Nombre == Decodificar[0][1]:#Se busca registro destino 
                        RAT[i].Valid=0 #
                        RAT[i].Tag = AdderRSM[pos].NombreM #se cambia su tag por el nombre de la estacion de reserva de la que esta esperando dato 
                Decodificar.pop(0)
            else:
                print("Estacion de reserva de multiplicaciones llena")
                
        
    #----------------fetch---------------------------------------------------------------
    if CodigoEnsamblador: 
        fetch = CodigoEnsamblador.pop(0)
        Decodificar.append(fetch)
    if Decodificar:
        for i in Decodificar:
            if i!=[]:
                print("operacion: ")
                print(i)
    print_RAT(RAT)
    print_res(AdderRS,SizeRS,"suma")
    print_res(AdderRSM,SizeRS,"multiplicación")
    
