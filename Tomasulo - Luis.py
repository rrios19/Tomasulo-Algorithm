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
#---Creacion del RAT-------
RAT=[]
cont=1
for i in range(12):
    Nombre = 'R' + str(cont)
    Valid=1
    Tag=None
    Value=cont
    R=Reg(Nombre,Valid,Tag,Value)
    RAT.append(R)
    cont+=1
#-----Creacion de RS de sumas---
AdderRS=[]
cont=1
for i in range(SizeRS):
    Nombre = 'A' + str(cont)
    Valid1=None
    Tag1=None
    Value1=None
    Valid2=None
    Tag2=None
    Value2=None
    contCiclos=0
    Bloque=BloqueRS(Nombre,Valid1, Tag1, Value1, Valid2, Tag2, Value2, contCiclos)
    AdderRS.append(Bloque)
    cont+=1
    

    
'''def dec(Decodificar, RAT, AdderRS):
    if Decodificar:
        f Decodificar[1] == ADD:
            for i in AdderRS:'''
    
#---------------para probar algoritmo---------------------------





EjecutandoSuma=[]#almacena instrucciones que estan esperando a cumplir ciclos
CodigoEnsamblador= [['ADD','R12','R1','R2'],['ADD','R5','R3','R4'],['ADD','R7','R2','R6'],['ADD','R10','R8','R9'],['ADD','R11','R7','R10'],['ADD','R5','R11','R5']]#lista de instrucciones obtenidas del archivo de texto
Decodificar = [] #almacena instruccion a la que se le hace fetch y esta lista para decodificar, ej: ADD, Rd, R1, R2
clock=0
stop=False
#--------------------------------------------------------------------

    
for e in range(18):
    
    print('------------------',e,'-----------------------')
                     
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
                                m.Tag1="~"
                                m.Value2= j.Value1+j.Value2
                                m.Valid2=1
                                m.Tag2="~"
                        k.Valid=1       
                        k.Tag=None
                        k.Value=j.Value1+j.Value2
                        #Se vacia estacion de reserva
                        j.Valid1=None
                        j.Tag1=None
                        j.Value1=None
                        j.Valid2=None
                        j.Tag2=None
                        j.Value2=None
                        j.contCiclos=0
                j.contCiclos+=1
                    
            else:
                j.contCiclos+=1
                
                
            

            
        
                        
                        
                        

                        
                        
                
    
  
                
        
    
    
            
    #--------------------Se decodifica instruccion de suma---------------------------   
    if Decodificar:
        if Decodificar[0][0] == 'ADD':
            cont=0
            disp=0#si hay estacion de reserva dispnible
            pos=0#posicion de estacion de reserva disponible
            while disp == 0 and cont<SizeRS:#ciclo revisa si hay espacio en estacion de reserva de sumas 
                if (AdderRS[cont].Valid1 == None and AdderRS[cont].Valid2 == None): 
                    pos = cont #posicion del bloque disponible en estacion de reserva de sumas
                    disp=1
                cont+=1
                    
            if disp:#proceso que empieza si hay espacio en estacion de reserva
                for i in range(len(RAT)):
                    if RAT[i].Nombre == Decodificar[0][2]:#busca registro de operando 1
                        if RAT[i].Valid==1:#Revisa si registro esta listo o esta esperando un valor
                            AdderRS[pos].Valid1= RAT[i].Valid 
                            AdderRS[pos].Tag1='~'
                            AdderRS[pos].Value1 = RAT[i].Value #si registro esta listo se escribe valor de registro en operando 1 de estacion de reserva
                           
                        else: 
                            AdderRS[pos].Valid1= 0
                            AdderRS[pos].Tag1=RAT[i].Tag  #si registro no esta disponible se copia su tag en operando 1 de estacion de reserva
                            
                            
                    
                    if RAT[i].Nombre == Decodificar[0][3]:#busca registro de operando 2
                        if RAT[i].Valid==1:#Revisa si registro esta listo o esta esperando un valor
                            AdderRS[pos].Valid2= RAT[i].Valid
                            AdderRS[pos].Tag2='~'
                            AdderRS[pos].Value2 = RAT[i].Value #si registro esta listo se escribe valor de registro en operando 2 de estacion de reserva
                        else:
                            AdderRS[pos].Valid2= 0
                            AdderRS[pos].Tag2=RAT[i].Tag#si registro no esta disponble se copia su tag en operando 2 de estacion de reserva
                            
                            
                    if RAT[i].Nombre == Decodificar[0][1]:#Se busca registro destino 
                        RAT[i].Valid=0 #
                        RAT[i].Tag = AdderRS[pos].Nombre #se cambia su tag por el nombre de la estacion de reserva de la que esta esperando dato 
                Decodificar.pop(0)
            else:
                print("Estacion de reserva de sumas llena")
            
    
                            
    #Busqueda de instrucciones listas para ejectutar(parte de la decodificacion)
    '''for i in range(len(AdderRS)):
        if (AdderRS[i].Valid1 == 1 and AdderRS[i].Valid2 == 1):#Revisa si en RS hay instruccion lista para ejecutar
            copia = BloqueRS(AdderRS[i].Nombre, AdderRS[i].Valid1, AdderRS[i].Tag1, AdderRS[i].Value1, AdderRS[i].Valid2, AdderRS[i].Tag2, AdderRS[i].Value2, AdderRS[i].contCiclos)
            EjecutandoSuma.append(copia) #se agrega la copia de instruccion a una lista con las instrucciones que esperan ciclos
            AdderRS[i].Valid1=None#El bloque de la estacion de reserva se "limpia"
            AdderRS[i].Tag1=None
            AdderRS[i].Value1=None
            AdderRS[i].Valid2=None
            AdderRS[i].Tag2=None
            AdderRS[i].Value2=None'''
        
    #----------------fetch---------------------------------------------------------------
    if CodigoEnsamblador: 
        fetch = CodigoEnsamblador.pop(0)
        Decodificar.append(fetch)



    print("operacion: ")
    if Decodificar:
        for i in Decodificar:
            print(i)
    print("Registros: ")
    for i in range(12):
        print(RAT[i].Nombre, RAT[i].Valid, RAT[i].Tag, RAT[i].Value)
    print("RS suma: ")
    for i in range(SizeRS):
        print(AdderRS[i].Nombre, AdderRS[i].Valid1, AdderRS[i].Tag1, AdderRS[i].Value1, AdderRS[i].Valid2, AdderRS[i].Tag2, AdderRS[i].Value2, AdderRS[i].contCiclos)

                    
                    
                
                
                
            
        
        
    
            
            
        
    
            
            
            
            






