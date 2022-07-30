#***************************************************************cimple_4085.py
#***************************************************************Lazaros Kosmidis  AM 4085
#***************************************************************Usernames ergastiriou
#***************************************************************cse74085 Lazaros Kosmidis 
#*****************Final Part of Project************************
#Kanw to project 2h fora #
#COMPILE PYTHON PROGRAM#
#python3 cimple_4085.py#
#OR#
#python cimple_4085.py#
#RUN#
#cimple test.ci#

global k
global line
Desmeumenes_lexeis = ["program", "declare", "if", "else", "while", "switchcase", "loop", "forcase", "incase",
         "case", "default", "not", "and", "or", "function", "procedure", "call", "return",
         "input", "print"]
sletters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
cletters = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
digits = ["1","2","3","4","5","6","7","8","9","0"]
operator = ["+","-","*","/"]
soperator = ["<",">","=",]
anathesis= [":","="]
diaxoristes = [";",","]
omadopoihsh = ["[","]","(",")","{","}"]
termatismou = ["."]
sxolio = ["#"]
 
compiler_name, file_name = input().split()
if(compiler_name != "cimple"):
    print("Error,should be 'cimple_4085 test.ci' .")
    exit(1)
f = open(file_name,'r')
line=0
k=f.read(1)
#Properties: tokentype , tokenstring , lineNo
class Token:
    def __init__(self,tokenType,tokenString, lineNo):
        self.tokenType = tokenType  
        self.tokenString = tokenString
        self.lineNo = lineNo

def lex():
    global k,a,b,c,t,z,d
    global line
    global ha
    i=0
    z =  ''
    global j
    while(i<1500):
        
        while(k==" " or k=="\n" or k=="\t"):
            
            if(k=="\n"):
                line = line + 1
                ha = 1
            
            k=f.read(1)
            break
        while(k!= " " and k!= "\n" and k!= "\t"):   
            
            if (k in sletters):
                z = z + k
                k = f.read(1)
                
                while((k in sletters) or (k in cletters) or (k in digits)):
                    
                    z = z + k
                    k = f.read(1)
                
                for c in range (0,len(Desmeumenes_lexeis)):
                    if(z == Desmeumenes_lexeis[c]):
                        t = Token("keyword",z,line)
                        
                        return t
                    else:
                        continue
                
                if(len(z) > 30):
                    print("Error variable name must me less than 30 chars,line: ",line)
                    exit(1)
                elif((k not in sletters) and (k not in cletters) and (k not in digits)):
                    t = Token("identifier",z,line)
                    return t        
            if (k in cletters):
                z = z + k
                k = f.read(1)
                
                while((k in sletters) or (k in cletters) or (k in digits)):
                    z = z + k
                    k = f.read(1)
                    
                if(len(z) > 30):
                    print("Error variable name must me less than 30 chars,line: " ,line)
                    sys.exit()
                elif((k not in sletters) and (k not in cletters) and (k not in digits)):
                    t = Token("identifier",z,line)
                    return t        
            if (k in digits):
                z = z +k
                k = f.read(1)
                while(k in digits):
                    z = z + k
                    k = f.read(1)
                
                if(int(z)>((2**32)-1)):
                    
                    print("Error numbers are between -(2^32)-1 and (2^32)-1")
                    exit(1)
                t = Token("digits",z,line)
                return t  
            if k in operator :
                if (k == "+" or k == "-"):
                    t = Token ("addOperator",k,line)
                    k = f.read(1)
                    return t
                if (k == "*" or k == "/"):
                    t = Token("mulOperator",k,line)
                    k = f.read(1)
                    return t
        
            if k in soperator:
                if(k == "<"):
                    z = z + k
                    k = f.read(1)
                    if(k == "="):
                        z = z + k
                        t = Token("relOperator",z,line)
                        k = f.read(1)
                        return t
                    if(k == ">"):
                        z = z + k
                        t = Token("relOperator",z,line)
                        k = f.read(1)
                        return t
                    else:
                        t = Token("relOperator",z,line)
                        k = f.read(1)
                        return t
                if(k == ">"):
                    z = z + k
                    k = f.read(1)
                    if(k == "="):
                        z = z + k
                        t = Token("relOperator",z,line)
                        k = f.read(1)
                        return t
                    if(k == "<"):
                        z = z + k
                        t = Token("relOperator",z,line)
                        k = f.read(1)
                        return t
                    else:
                        t = Token("relOperator",z,line)
                        k = f.read(1)
                        return t
                if(k == "="):
                    
                    t = Token("relOperator",k,line)
                    k = f.read(1)
                    return t
                
            if k in anathesis:
                if (k == ":"):
                    z = z + k
                    k = f.read(1)
                    if(k == "="):
                        z= z + k
                        t = Token("assignment",z,line)
                        k = f.read(1)
                        return t
    
            if k in diaxoristes:
                if (k == "," or k == ";"):
                    t = Token("delimiter",k,line)
                    k=f.read(1)
                    return t
                
            if k in omadopoihsh:
                if (k == ")" or k == "(" or k == "{" or k =="}" or k =="[" or k == "]"):
                    t = Token("groupSymbol",k,line)
                    k = f.read(1)
                    return t
            if k =='.':
                t = Token("termatismou",k,line)
                return t
            if k == '#':
                k = f.read(1) 
                gab = 0
                while(k != "#"):
                    gab+=1
                    if k == "\n":
                        line+=1
                    if(gab >3000) :
                        print("Error unclosed comments line:",line)
                        exit(1)
                    k =f.read(1)
                k =f.read(1)
                return lex()
                      
            i=i+1
            
            
# ****************************************************************************
# **************************Endiamesos Kodikas********************************
# ****************************************************************************
global numberOfQuads
numberOfQuads=0
global Assing
Assing = 0
global ListOfQuads 
ListOfQuads = list()
global temp
temp = 0
temp = 0
global ListOfQuads1
ListOfQuads1 = []
global length
global b
global gh
global rtx
global bo
global w1
global gp
global opr
global opr1
global opr2
global opr3
global opr4
global opr5
opr5=''
global gor 
global CList
global vlist
global vlist1
vlist1= list()
global ha
global WhoIsToKeepInformationForOut
global listnewtemp
global shtem
shtem = 12
global KeepInformationForOut
KeepInformationForOut = list()
listnewtemp = list()
ha = 0
CList = list()
global Clistlength
def nextquad():
    global numberOfQuads
    numberOfQuads=numberOfQuads+1
    
    return numberOfQuads
    
def genquad(op,x,y,z):
    global ListOfQuads1 
    global newQuad
    global length
    newQuad = ''
    newQuad=newQuad + str(nextquad())
    newQuad=newQuad + ": "   
    newQuad = newQuad + op
    newQuad = newQuad + x
    newQuad = newQuad + y
    newQuad = newQuad + z
    ListOfQuads1.append(newQuad)
    length = len(ListOfQuads1)
    
def newtemp():
    global ListOfVars
    global temp
    temp +=1
    ListOfVars = "T_"
    ListOfVars = ListOfVars + str(temp)
    listnewtemp.append(ListOfVars)
    return ListOfVars

def emptylist():
    emptylist=list()
    return emptylist

def makelist(x):
    listx=[x]
    return listx

def merge(list1,list2):
    mergeList=list1+list2
    return mergeList

def backpatch(List,z):
        #z is label
        global metavliti
        metavliti = 0
        a=''
        b=''
        c=''
        d=''
        a=List[0]+List[1]
        
        
        
        for x in range(2,len(List)):
            b+=List[x]
            if(List[x] == ","):
                metavliti =x
                break;
        for y in range(metavliti+1,len(List)):
            c+=List[y]
            if(List[y] == ","):
                metavliti = y
                break;        
        for h in range(metavliti+1,len(List)):
            d+=List[h]
            if(List[h] == ","):
                metavliti = h
                break;
        List=[]
        List = a + b + c + d +z
        
        return List          
            
# ***************************************************************************   
# ******************Implementation Tou Suntaktikou Analiti*******************
# ***************************************************************************
global name 
global g5
global Block
global FunctionList
global a
global no
global sin
global Fun2
global sin1
global G1
G1=0
global Helpa
global Helpb
global Helpin
global Helpin1
global gor1
global jpeg
global Inif
Inif=0
global geg
geg = 0
global WriteOnC
global WriteOnArrayOfSymbols
WriteOnArrayOfSymbols = 1 
global batr
batr = 0
FunctionList = list()
g5=5
Block = 0 
global NextQuadListHelp
NextQuadListHelp = list()
global tolist
tolist = list()
global Ltolist
Ltolist = len(tolist)
global CallList
CallList = list()
global jp
global G
G=0
global AssingCount
AssingCount=0
global Inwhile
Inwhile = 0
global vlist2
vlist2 = list()
global FunWriteOnArr
FunWriteOnArr = 0
global ProWriteOnArr
ProWriteOnArr = 0
global returnStat
returnStat = 0
global ArrayOfSyms
ArrayOfSyms = list()
global ArrayOfSymsHelp
ArrayOfSymsHelp = list()
global FinalCodeList
FinalCodeList = list()
global FinalCodeCounter
FinalCodeCounter = 0
global counter
counter = 0
global stopit
stopit=0
global NotFunction
NotFunction = 0
w=''
w1=''
global idFunc
idFunc = ''
global InFuncion
InFuncion = 0
global StartOfFunc
StartOfFunc = 0
Fun2 = 0
global NOTInFunc
global NoMoreMain
NoMoreMain = 0
NOTInFunc = 0
global HASFUNC
HASFUNC=0
def suntaktikos():
    global token
    token=lex()
    global length
    
# ***************************************************************************   
    def program():
        global token
        global name
        global g5
        global Block
        global CList
        global WriteOnC
        global Clistlength
        global vlist1
        global tolist
        global ArrayOfSymsHelp
        global ha
        global counter
        global sect
        global Array
        global sh1
        global NextQuadListHelp
        global WriteOnArrayOfSymbols
        global FinalCodeCounter
        global FinalCodeList
        NextQuadListHelp = list()
        Array = list()
        sect = 0
        counter = 0
        WriteOnC = 1
        if token.tokenString =='program':   
            token=lex()
            name = token.tokenString
            FinalCodeList.append("L"+str(FinalCodeCounter)+": "+"\t"+"b Lmain")
            FinalCodeCounter+=1
            ID()
            if(token.tokenString != '{'):
                print("ERROR missing '{' line:",line)
                exit(1)

            token=lex()
            block()
            block()
            if token.tokenString =='.':
               
                Block = 1
                sect = 1
                sh = 12
                sh1 = 12
                
                if(WriteOnArrayOfSymbols == 1):
                    for rh in range (0,len(tolist)):
                            for rh1 in range (0,len(vlist1)):               
                                if(tolist[rh]==vlist1[rh1]):
                                    print("Error: functions and variables cant have the same name!")
                                    exit(1) 
                block() 
                if(WriteOnC==1):
                    CList.append("}")
                    Clistlength = len(CList)
                print("Lexical and Syntax Analyse Complete Successfull!")
            
        else:
            print("Error: the word program was expected, line",line)
            exit(1) 
# ***************************************************************************   
    def block():
        global name
        global g5
        global Block
        global token
        global WriteOnC
        global CList
        global vlist1
        global vlist2
        global Clistlength
        global sect
        global listnewtemp
        global ListOfQuads1
        global FinalCodeList
        global FinalCodeCounter
        global stopit
        global NoMoreMain
        global HASFUNC
        if(Block==1):
           genquad("halt ,","_ ,","_ ,","_")
           genquad("end_block, ",",main_"+name,", _ ,","_")      
           FinalCodeList.append("L"+str(FinalCodeCounter)+":")
           FinalCodeCounter+=1
           FinalCodeList.append("L"+str(FinalCodeCounter)+":")
           
        declarations()
        if(token.tokenString=='function'):
            HASFUNC=1
        if(token.tokenString != 'function' and NoMoreMain==0 and HASFUNC==0):
            
            genquad("begin_block, ",",main_"+name,", _ ,"," _")
            NoMoreMain=1
        
        subprograms()
        if(WriteOnC == 1):    
            if(sect==0):   
                
                start = "int main(){"
                CList.append(start)
                for gr in range (0,len(vlist1)):
                        CList.append("\t"+"int "+ str(vlist1[gr])+";")
                 
                for gr in range (0,len(listnewtemp)): 
                    CList.append("\t"+"int "+ str(listnewtemp[gr])+";")
                
                if(ha == 1):
                    CList.append("\t" + "L_"+str(counter)+":")
                Clistlength = len(CList)
                sect=1
               
        statement()
        statements()

# ***************************************************************************   

    def declarations():
        global token
        global CList
        global Clistlength
        global ha
        global vlist1
        global ArrayOfSyms
        global ArrayOfSymsHelp
        global sh
        sh = 12
        if token.tokenString == 'declare':
            
            while(token.tokenString == 'declare'):
                token=lex()
                ArrayOfSymsHelp.append(token.tokenString)
                ArrayOfSymsHelp.append("variable")
                ArrayOfSymsHelp.append(sh)
                ArrayOfSyms.append(ArrayOfSymsHelp)
                ArrayOfSymsHelp=list()
                sh+=4
                varlist()
                
                if token.tokenString==';':
                    token=lex()
                    
                else:
                    print("ERROR : ';' was expected line, : ",line)
                    exit(1)
       
            
# ***************************************************************************   
    def varlist():
        global token
        global vlist
        global vlist1
        global ArrayOfSyms
        global ArrayOfSymsHelp
        global sh 
        sh = 16
        vlist1.append(token.tokenString)
        ID()
        while( token.tokenString==','):
            
            token=lex()
            ArrayOfSymsHelp.append(token.tokenString)
            ArrayOfSymsHelp.append("variable")
            ArrayOfSymsHelp.append(sh)
            ArrayOfSyms.append(ArrayOfSymsHelp)
            ArrayOfSymsHelp=list()
            sh+=4
            vlist1.append(token.tokenString)
            
            ID()
        
        if((token.tokenString[0] in sletters) or (token.tokenString[0] in cletters)):
            print("Error : , need between variables,line :",line)

# ***************************************************************************           
    def subprograms():
        global token
        global g5
        global WriteOnC
        global FunWriteOnArr
        global ProWriteOnArr
        global NOTInFunc
       
        while token.tokenString=='function' or token.tokenString=='procedure':
            WriteOnC = 0
            
            subprogram()
            block()
            
                    
          
# ***************************************************************************   
    def subprogram():
        global token
        global g5
        global ablist
        global a
        global b
        global FunctionList
        global tolist
        global sin
        global sin1
        global vlist1
        global FunWriteOnArr
        global ProWriteOnArr
        global returnStat
        global FinalCodeCounter
        global FinalCodeList
        returnStat = 0
        global NotFunction
        global stopit
        global idFunc
        global InFuncion
        ablist = list()
        g5=5
        
        if token.tokenString=='function':
            InFuncion += 1
            FunWriteOnArr = 1
            g5=6
            token=lex()
            idFunc = token.tokenString
            
            
            tolist.append(idFunc)
            genquad("begin_block ,",idFunc," ,_ ,","_ ")
            FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "sw ra,-0(sp)")
            FinalCodeCounter+=1
            
            ID()
            ablist.append(idFunc)
            
            if token.tokenString=='(':
                token=lex()
                
                formalparlist()
                ablist.append(a)
                ablist.append(b)
                ablist.append(sin)
                ablist.append(sin1)
                FunctionList.append(ablist)
                if token.tokenString==')':
                    token=lex()
                    g5=6
                    
                    declarations()
                    block()
     
                else:
                    print("ERROR : ')' was expected, line:",line)
                    exit(1)
                if(NotFunction == 1):
                    if(g5 == 6 and sect!= 1 and stopit==0):
                        
                        
                        stopit = 1
                        g5=8
                        NotFunction=2
            else:
                print("ERROR : '(' was expected, line:",line)
                exit(1)
        elif token.tokenString=='procedure':
            ProWriteOnArr = 1
            
            token=lex()
            tolist.append(token.tokenString)
            ablist.append(token.tokenString)
            
            ID()
            
            if token.tokenString=='(':
                token=lex()
                formalparlist()
                ablist.append(a)
                ablist.append(b)
                ablist.append(sin)
                ablist.append(sin1)
                FunctionList.append(ablist)
                if token.tokenString==')':
                    token=lex()
                    block()
                else:
                    print("ERROR : ')' was expected, line:",line)
                    exit(1)
            else:
                print("ERROR : '(' was expected, line:",line)
                exit(1)
        
        FunWriteOnArr = 0
        ProWriteOnArr = 0
        returnStat = 0
        
# ***************************************************************************   
    def formalparlist():
        global b
        global token
        global no
        no = 5
        formalparitem()
        while token.tokenString==',':
            token=lex()
            no = 6
            formalparitem()
            

# ***************************************************************************           
    def formalparitem():
        global token
        global a
        global b
        global no
        global sin
        global sin1
        global ablist
        global FunctionList
        if token.tokenString=='in' or token.tokenString=='inout':
            
            if(no==5):
                if(token.tokenString=='in'):
                    sin = 'in'
            
                if(token.tokenString=='inout'):
                    sin = 'inout'
            if(no == 6):
                if(token.tokenString=='in'):
                    sin1 = 'in'
                if(token.tokenString=='inout'):
                    sin1 = 'inout'
            
            token=lex()
            if(no==5):
                a = token.tokenString
            if (token.tokenString == ")"):
                print("ERROR: variable was expected , line ",line)
                exit(1)
            if(no == 6):
                b = token.tokenString

            else :
                b = " "
                sin1=" "
                
            ID()
            
        
# ***************************************************************************   
    def statements():
        global token
        global Block
        global returnStat
        global FunWriteOnArr
        global WriteOnArrayOfSymbols
        global NotFunction
        global idFunc
        global InFuncion
        global StartOfFunc
        global Fun2
        global name
        global FinalCodeList
        global FinalCodeCounter
        global NoMoreMain
        
        if(token.tokenString!="."): 
                
                if(token.tokenString not in Desmeumenes_lexeis):
                    if(token.tokenString=='{'):
                       
                        StartOfFunc += 1
                    if(StartOfFunc == 2):
                        Fun2 = 1
                    token=lex()
                    
                statement()
                
                while token.tokenString==';':
                
                    token=lex()
                    
                    if(token.tokenString == '}'):   
                        
                        break
                    if(token.tokenString == '.'):
                        break
                    if(token.tokenString == ';'):
                        break
                    statement() 
               
                
                if  token.tokenString=='}':
                    
                    
                    
                    if(InFuncion == 1 and Fun2 ==0):
                        genquad("end_block ,",FunctionList[len(FunctionList)-1][0]," ,_ ,","_ ")
                        FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "lw ra,-0(sp)")
                        FinalCodeList.append("\t"+"\t"+"jr ra")
                        FinalCodeCounter+=1
                    if(InFuncion == 2 and StartOfFunc == 2):
                        genquad("end_block ,",FunctionList[len(FunctionList)-1][0]," ,_ ,","_ ")
                        FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "lw ra,-0(sp)")
                        FinalCodeList.append("\t"+"\t"+"jr ra")
                        FinalCodeCounter+=1
                    if(InFuncion == 1 and Fun2 == 1):
                        
                        genquad("end_block ,",FunctionList[len(FunctionList)-2][0]," ,_ ,","_ ")
                        FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "lw ra,-0(sp)")
                        FinalCodeList.append("\t"+"\t"+"jr ra")
                        FinalCodeCounter+=1
                        Fun2 = 0
                    
                    InFuncion-=1
                    StartOfFunc -=1
                    token=lex()
                    
                    if(NoMoreMain==0 and InFuncion<=0 and StartOfFunc <=0 and Fun2 ==0 and token.tokenString!='function' ):
                        
                        genquad("begin_block, ",",main_"+name,", _ ,"," _")
                        FinalCodeList.append("Lmain:")
                        FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "addi sp, sp , framelength")
                        FinalCodeList.append("\t"+"\t"+"move gp, sp")
                        FinalCodeCounter+=1
                        Fun2 = 5
                if  token.tokenString=='{':
                        token=lex()
                        
                if(token.tokenString==';'):
                    token=lex()
                if(token.tokenString != "function"):
                    NotFunction = 1
               
                if(returnStat == 0 and FunWriteOnArr == 1):
                    
                    WriteOnArrayOfSymbols = 0
                if(returnStat == 1 and FunWriteOnArr == 0 and ProWriteOnArr ==0):
                   
                    WriteOnArrayOfSymbols = 0               
                if(returnStat == 1 and ProWriteOnArr ==1):                  
                   
                    WriteOnArrayOfSymbols = 0
            
# ***************************************************************************   
    def statement():
        assingStat()
        ifStat()
        whileStat()
        switchcaseStat()
        forcaseStat()
        incaseStat()
        callStat()
        returnStat()
        inputStat()
        printStat()

# ***************************************************************************   
    def assingStat():
        global token
        global FunctionList
        global c
        global h
        global tolist
        global w1
        global Eplace
        global gor
        global gor1
        global Helpa
        global Helpb
        global CList
        global Clistlength
        global counter
        global WriteOnC
        global FinalCodeList
        global FinalCodeCounter
        global ArrayOfSyms
        global KeepInformationForOut
        global WhoIsToKeepInformationForOut
        gor1=0
        WhoIsToKeepInformationForOut = token.tokenString
        global Assing
        global AssingCount
        if (token.tokenString not in Desmeumenes_lexeis):   
            id = token.tokenString
            
            ID()
            if token.tokenString==':=':
                Assing = 1
                token=lex()
                for c in range (0,len(FunctionList)-1):
                        if(token.tokenString == FunctionList[c][0]):
                            if(FunctionList[c][2] == " "):
                                if(FunctionList[c][3] == "in"):
                                    genquad("par ,",FunctionList[c][1]," ,CV,"," _")
                                    for bc in range (0,len(ArrayOfSyms)):
                                        if(Helpa==ArrayOfSyms[bc][0]):
                                            FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "addi fp,sp, offset")
                                            FinalCodeList.append("\t"+"\t"+"lw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                                            FinalCodeList.append("\t"+"\t"+"sw t1,-"+str(ArrayOfSyms[bc][2])+"(fp)")
                                            FinalCodeCounter+=1
                                elif(FunctionList[c][3] == "inout"):
                                    genquad("par ,",FunctionList[c][1],", REF,"," _")
                                    
                                
                                
                            else:
                                if(FunctionList[c][3] == "in"):
                                    genquad("par ,",FunctionList[c][1]," ,CV,"," _")
                                    for bc in range (0,len(ArrayOfSyms)):
                                        if(Helpa==ArrayOfSyms[bc][0]):
                                            FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "addi fp,sp, offset")
                                            FinalCodeList.append("\t"+"\t"+"lw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                                            FinalCodeList.append("\t"+"\t"+"sw t1,-"+str(ArrayOfSyms[bc][2])+"(fp)")
                                            FinalCodeCounter+=1
                                if(FunctionList[c][3] == "inout"):
                                    genquad("par, ",FunctionList[c][1]," ,REF,"," _")
                                if(FunctionList[c][4] == "in"):
                                    genquad("par ,",FunctionList[c][2]," ,CV,"," _")
                                    for bc in range (0,len(ArrayOfSyms)):
                                        if(Helpb==ArrayOfSyms[bc][0]):
                                            FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "addi fp,sp, offset")
                                            FinalCodeList.append("\t"+"\t"+"lw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                                            FinalCodeList.append("\t"+"\t"+"sw t1,-"+str(ArrayOfSyms[bc][2])+"(fp)")
                                            FinalCodeCounter+=1
                                if(FunctionList[c][4] == "inout"):
                                    genquad("par ,",FunctionList[c][2]," ,REF,"," _")
                            
                            w = newtemp()
                            genquad("par, ",w," ,RET,"," _ ")
                            FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "addi t0,sp,-offset")
                            FinalCodeList.append("\t"+"\t"+"sw t0,-8(fp)")
                            FinalCodeCounter+=1
                            genquad("call ,",token.tokenString,", _,"," _ ")
                            gor1 = 2
                
                if(token.tokenString not in tolist):
                    Eplace = token.tokenString
                                  

                if(token.tokenString==';' ):
                    print ("ERROR : expected value after assignment , line:",line)
                    exit(1)               
                expression()
                
                if(gor == 0 and gor1 == 0): 
                
                    genquad(":= ,",Eplace,", _ ,",id)
                    
                    for bc in range (0,len(ArrayOfSyms)):
                        if(id==ArrayOfSyms[bc][0]):
                            FinalCodeList.append("L"+str(FinalCodeCounter)+": "+"\t"+"li t1,"+Eplace)
                            FinalCodeList.append("\t"+"\t"+"sw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                            FinalCodeCounter+=1
                    if(WriteOnC==1):
                        CList.append("\t"+"L_"+str(counter)+": "+id + "=" + Eplace +";"+ "   // ( :=  " + Eplace +  " _ " + id + ")" )
                        counter+=1
                        Clistlength = len(CList)
                
            
                if(gor1 == 1):
                    
                    genquad(":= ,",id+" ",", _ ,",w1)
                    
                    for bc in range (0,len(ArrayOfSyms)):
                        if(w1==ArrayOfSyms[bc][0]):
                            FinalCodeList.append("L"+str(FinalCodeCounter)+": "+"\t"+"lw t1,-offset(sp)")
                            FinalCodeList.append("\t"+"\t"+"lw t0,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                            FinalCodeList.append("\t"+"\t"+"sw t1,(t0)")
                            FinalCodeCounter+=1
                    if(WriteOnC==1):
                        CList.append("\t"+"L_"+str(counter)+": "+id + "=" + w1 +";"+ "   // ( := " + id + " _ " + w1 + ");" )
                        counter+=1
                        Clistlength = len(CList)
                if(gor1 == 2):
                    genquad(":= ,",id+" ",", _ ,",w)
                    
                    for bc in range (0,len(ArrayOfSyms)):
                        if(w==ArrayOfSyms[bc][0]):
                            FinalCodeList.append("L"+str(FinalCodeCounter)+": "+"\t"+"lw t1,-"+ArrayOfSyms[bc][2]+"(sp)")
                            FinalCodeList.append("\t"+"\t"+"lw t0,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                            FinalCodeList.append("\t"+"\t"+"sw t1,(sp)")
                            FinalCodeCounter+=1
                
                if(token.tokenString != ';'):
                    print ("ERROR : ';' was expected, line:",line)
                    exit(1)
                    
        Assing=0 
        AssingCount = 0
# ***************************************************************************   
    def ifStat():
        global token
        global fg
        global rtx
        global WriteOnC
        global counter
        global Clistlength
        global CList
        global opr
        global opr1
        global opr2
        global opr3
        global opr4
        global opr5
        global rtx
        global jpeg
        global gor1
        global IfG1
        global bo
        global gor
        global FinalCodeCounter
        global FinalCodeList
        global Inif
        fg = 0
        if token.tokenString=='if':
            token=lex()
            Inif = 1
            
            if token.tokenString=='(':
                token=lex()
                mem = token.tokenString
                if(token.tokenString not in tolist):
                    rtx = token.tokenString
                IfG1 = numberOfQuads                
                while(token.tokenString!=')'):  
                    condition()
                if(WriteOnC==1):
                        if(gor1 == 0):
                            if(jpeg == "="):
                            
                                CList.append("\t"+"L_"+str(counter)+" if ("+mem+jpeg+jpeg+opr+")"+" goto " + "   // ( if " + mem + jpeg + opr + ");" )
                                counter+=1
                                
                                CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                                Clistlength = len(CList)
                                counter+=1
                            if(jpeg == ">"):
                            
                                CList.append("\t"+"L_"+str(counter)+" if ("+mem+jpeg+opr1+")"+" goto " + "   // ( if " + mem + jpeg + opr1 + ");")
                                counter+=1
                                CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                                Clistlength = len(CList)
                                counter+=1
                            if(jpeg == "<"):
                            
                                CList.append("\t"+"L_"+str(counter)+" if ("+mem+jpeg+opr2+")"+" goto "+ "   // ( if " + mem + jpeg + opr2 + ");")
                                counter+=1
                                CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   //  (JUMP,  ,  , )")
                                Clistlength = len(CList)
                                counter+=1
                            if(jpeg == "<="):
                            
                                CList.append("\t"+"L_"+str(counter)+" if ("+mem+jpeg+opr5+");"+" goto " + "   // ( if " + mem + jpeg + opr5 + ")")
                                counter+=1
                                CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                                Clistlength = len(CList)
                                counter+=1
                            if(jpeg == ">="):
                            
                                CList.append("\t"+"L_"+str(counter)+" if ("+mem+jpeg+opr3+");"+" goto " + "   // ( if " + mem + jpeg + opr3 + ")") 
                                counter+=1
                                CList.append("\t"+"L_"+str(counter)+"got to;" + "   // (JUMP,  ,  , )")
                                Clistlength = len(CList)
                                counter+=1
                            if(jpeg == "<>"):
                            
                                CList.append("\t"+"L_"+str(counter)+" if ("+mem+jpeg+opr4+");"+" goto " + "   // ( if " + mem + jpeg + opr4 + ")")
                                counter+=1
                                CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                                Clistlength = len(CList)
                                counter+=1
                        elif(gor1 == 1):
                            if(jpeg == "="):
                                CList.append("\t"+"L_"+str(counter)+" if ("+w1+jpeg+opr+");"+" goto " + "   // ( if " + mem + jpeg + opr + ")")
                                counter+=1
                                CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                                Clistlength = len(CList)
                                counter+=1
                            if(jpeg == ">"):
                                CList.append("\t"+"L_"+str(counter)+" if ("+w1+jpeg+opr1+");"+" goto " + "   // ( if " + mem + jpeg + opr1 + ")")
                                counter+=1
                                CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                                Clistlength = len(CList)
                                counter+=1
                            if(jpeg == "<"):
                                CList.append("\t"+"L_"+str(counter)+" if ("+w1+jpeg+opr2+");"+" goto " + "   // ( if " + mem + jpeg + opr2 + ")")
                                counter+=1
                                CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                                Clistlength = len(CList)
                                counter+=1
                            if(jpeg == "<="):
                                CList.append("\t"+"L_"+str(counter)+" if ("+w1+jpeg+opr5+");"+" goto " + "   // ( if " + mem + jpeg + opr5 + ")")
                                counter+=1
                                CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                                Clistlength = len(CList)
                                counter+=1
                            if(jpeg == ">="):
                                CList.append("\t"+"L_"+str(counter)+" if ("+w1+jpeg+opr3+");"+" goto " + "   // ( if " + mem + jpeg + opr3 + ")")
                                counter+=1
                                CList.append("\t"+"L_"+str(counter)+"got to;" + "   // (JUMP,  ,  , )")
                                Clistlength = len(CList)
                                counter+=1
                            if(jpeg == "<>"):
                                CList.append("\t"+"L_"+str(counter)+" if ("+w1+jpeg+opr4+");"+" goto " + "   // ( if " + mem + jpeg + opr4 + ")")
                                counter+=1
                                CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                                Clistlength = len(CList)
                                counter+=1
                
                if token.tokenString==')':
                    token=lex()
                    
                    genquad("jump ,"," _,"," _,"," _")
                    IfG=numberOfQuads
                    FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "b _")
                    FinalCodeCounter+=1
                    statements()
                    
                    
                    genquad("jump ,","_ ,"," _ ,",str(IfG-1))
                    NewIfG=numberOfQuads
                    
                    for s in range (0,len(ListOfQuads1)):
                        if(int(IfG) == int(ListOfQuads1[s][0])):
                            mylist = backpatch(ListOfQuads1[s],str(NewIfG+1))
                            ListOfQuads1[s]=mylist
                    
                    
                    elsepart()
                    
                else:
                    print("ERROR : ')' was expected, line:",line)
                    exit(1)
            else:
                print("ERROR : '(' was expected, line:",line)
                exit(1)
            Inif=0
# ***************************************************************************   
    def elsepart():
        global token 
        
        if token.tokenString=='else':
            
            token=lex()
            statements()

# ***************************************************************************   
    def whileStat():
        global jp
        global token
        global c
        global h
        global tolist
        global w
        global w1
        global Eplace
        global fd
        global rtx
        global jpeg
        global gp
        global opr
        global opr1
        global opr2
        global opr3
        global opr4
        global opr5
        global Helpa
        global Helpb
        global numberOfQuads
        global ListOfQuads1
        global gor
        global gor1
        global WriteOnC
        global CList
        global Clistlength
        global counter
        global FinalCodeCounter
        global FinalCodeList
        global ArrayOfSyms
        global ArrayOfSymsHelp
        global Inwhile
        global G1
        
        
        gp = 0 
        
        if token.tokenString=='while':
            token=lex()
            Inwhile =1
            
            if token.tokenString=='(':
                token=lex()
                fd = token.tokenString   
                if(fd in tolist):
                    rtx = token.tokenString
                    gp = 1
                else:
                    rtx = token.tokenString
                    gp = 0
                #Btrue=token.tokenString
                G1 = numberOfQuads
                condition()
                for c in range (0,len(FunctionList)):
                        
                        if(fd == FunctionList[c][0]):
                            if(FunctionList[c][2] == " "):
                                
                                if(gor1 == 1):   
                                    if(FunctionList[c][3] == "in"):
                                        genquad("par ,",w1," ,CV,"," _")
                                        for bc in range (0,len(ArrayOfSyms)):
                                            if(w1==ArrayOfSyms[bc][0]):
                                                FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "addi fp,sp, offset")
                                                FinalCodeList.append("\t"+"\t"+"lw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                                                FinalCodeList.append("\t"+"\t"+"sw t1,-"+str(ArrayOfSyms[bc][2])+"(fp)")
                                                FinalCodeCounter+=1
                                    elif(FunctionList[c][3] == "inout"):
                                        genquad("par ,",w1," ,REF,"," _")  
                                elif(gor1 == 0):
                                    
                                    if(FunctionList[c][3] == "in"):
                                        genquad("par ,",Helpa," ,CV,"," _")
                                        for bc in range (0,len(ArrayOfSyms)):
                                            if(Helpa==ArrayOfSyms[bc][0]):
                                                FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "addi fp,sp, offset")
                                                FinalCodeList.append("\t"+"\t"+"lw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                                                FinalCodeList.append("\t"+"\t"+"sw t1,-"+str(ArrayOfSyms[bc][2])+"(fp)")
                                                FinalCodeCounter+=1
                                    elif(FunctionList[c][3] == "inout"):
                                        genquad("par ,",Helpa," ,REF,"," _")
                            else:
                                if(gor1 == 1):
                                    if(FunctionList[c][3] == "in"):
                                        genquad("par ,",w1," ,CV,"," _")
                                        for bc in range (0,len(ArrayOfSyms)):
                                            if(w1==ArrayOfSyms[bc][0]):
                                                FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "addi fp,sp, offset")
                                                FinalCodeList.append("\t"+"\t"+"lw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                                                FinalCodeList.append("\t"+"\t"+"sw t1,-"+str(ArrayOfSyms[bc][2])+"(fp)")
                                                FinalCodeCounter+=1
                                    if(FunctionList[c][3] == "inout"):
                                        genquad("par ,",w1," ,REF,"," _")
                                    if(FunctionList[c][4] == "in"):
                                        genquad("par ,",w1," ,CV,"," _")
                                        for bc in range (0,len(ArrayOfSyms)):
                                            if(w1==ArrayOfSyms[bc][0]):
                                                FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "addi fp,sp, offset")
                                                FinalCodeList.append("\t"+"\t"+"lw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                                                FinalCodeList.append("\t"+"\t"+"sw t1,-"+str(ArrayOfSyms[bc][2])+"(fp)")
                                                FinalCodeCounter+=1
                                    if(FunctionList[c][4] == "inout"):
                                        genquad("par ,",w1," ,REF,"," _")
                                elif(gor1 == 0):
                                    if(FunctionList[c][3] == "in"):
                                        genquad("par ,",Helpb," ,CV,"," _")
                                        for bc in range (0,len(ArrayOfSyms)):
                                            if(Helpb==ArrayOfSyms[bc][0]):
                                                FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "addi fp,sp, offset")
                                                FinalCodeList.append("\t"+"\t"+"lw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                                                FinalCodeList.append("\t"+"\t"+"sw t1,-"+str(ArrayOfSyms[bc][2])+"(fp)")
                                                FinalCodeCounter+=1
                                    if(FunctionList[c][3] == "inout"):
                                        genquad("par ,",Helpb," ,REF,"," _")
                                    if(FunctionList[c][4] == "in"):
                                        genquad("par ,",Helpb," ,CV,"," _")
                                        for bc in range (0,len(ArrayOfSyms)):
                                            if(Helpb==ArrayOfSyms[bc][0]):
                                                FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "addi fp,sp, offset")
                                                FinalCodeList.append("\t"+"\t"+"lw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                                                FinalCodeList.append("\t"+"\t"+"sw t1,-"+str(ArrayOfSyms[bc][2])+"(fp)")
                                                FinalCodeCounter+=1
                                    if(FunctionList[c][4] == "inout"):
                                        genquad("par ,",Helpb," ,REF,"," _")
                            w = newtemp()
                            genquad("par ,",w," ,RET,"," _ ")
                            FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "addi t0,sp,-offset")
                            FinalCodeList.append("\t"+"\t"+"sw t0,-8(fp)")
                            FinalCodeCounter+=1
                            genquad("call ,",fd,", _,"," _ ")
                            
                            if(jpeg == "="):
                                
                                genquad(jpeg+" ,",w+" ,",opr,", _ ")
                                
                            if(jpeg == ">"):
                                genquad(jpeg+" ,",w+" ,",opr1," ,_ ")
                                
                            if(jpeg == "<"):
                                genquad(jpeg+" ,",w+" ,",opr2,", _ ")
                                
                            if(jpeg == ">="):
                                genquad(jpeg+" ,",w+" ,",opr3," ,_ ")
                                
                            if(jpeg == "<>"):
                                genquad(jpeg+" ,",w+" ,",opr4," ,_ ")
                                
                            if(jpeg == "<="):
                                genquad(opr5+" ,",w+" ,",opr5," ,_ ")
                
                if(WriteOnC==1):
                    if(gor1==0):
                        if(jpeg == "="):
                            CList.append("\t"+"L_"+str(counter)+" if ("+fd+jpeg+opr+");"+" goto " + "   // ( if " + jpeg + w + opr + ")")
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // ( if " + jpeg + w + opr + ")")
                            Clistlength = len(CList)
                            counter+=1
                
                        if(jpeg == ">"):        
                           # CList.append("\t"+"L_"+str(counter)+" if ("+fd+jpeg+opr1+");"+" goto " + "  // ( if " + jpeg + w + opr1 + ")" )
                            counter+=1
                            #CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // ( if " + jpeg + w + opr1 + ")")
                            Clistlength = len(CList)
                            counter+=1
                
                        if(jpeg == "<"):
                            CList.append("\t"+"L_"+str(counter)+" if ("+fd+jpeg+opr2+");"+" goto " + "  // ( if " + jpeg + w + opr2 + ")")
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // ( if " + jpeg + w + opr2 + ")")
                            Clistlength = len(CList)
                            counter+=1
                
                        if(jpeg == ">="):
                            CList.append("\t"+"L_"+str(counter)+" if ("+fd+jpeg+opr3+");"+" goto " + "   // ( if " + jpeg + w + opr3 + ")")
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // ( if " + jpeg + w + opr3 + ")")
                            Clistlength = len(CList)
                            counter+=1
                
                        if(jpeg == "<="):
                          #  CList.append("\t"+"L_"+str(counter)+" if ("+fd+jpeg+opr5+");"+" goto " + "   // ( if " + jpeg + w + opr4 + ")")
                            counter+=1
                          # CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                
                        if(jpeg == "<>"):
                            CList.append("\t"+"L_"+str(counter)+" if ("+fd+jpeg+opr4+");"+" goto "+ "   // ( if " + jpeg + w1 + opr5 + ")")
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                    elif(gor1==1):
                        if(jpeg == "="):
                            
                            CList.append("\t"+"L_"+str(counter)+" if ("+w1+jpeg+opr+");"+" goto " + "   // ( if " + jpeg + w + opr + ")")
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                
                        if(jpeg == ">"):        
                            CList.append("\t"+"L_"+str(counter)+" if ("+w1+jpeg+opr1+");"+" goto " + "   // ( if " + jpeg + w + opr1 + ")")
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                
                        if(jpeg == "<"):
                            CList.append("\t"+"L_"+str(counter)+" if ("+w1+jpeg+opr2+");"+" goto " + "   // ( if " + jpeg + w + opr2 + ")")
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , ))")
                            Clistlength = len(CList)
                            counter+=1
                
                        if(jpeg == ">="):
                            CList.append("\t"+"L_"+str(counter)+" if ("+w1+jpeg+opr3+");"+" goto " + "   // ( if " + jpeg + w + opr3 + ")")
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                
                        if(jpeg == "<="):
                            CList.append("\t"+"L_"+str(counter)+" if ("+w1+jpeg+opr5+");"+" goto "  +  "   // ( if " + jpeg + w1 + opr5 + ")")
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                
                        if(jpeg == "<>"):
                            CList.append("\t"+"L_"+str(counter)+" if ("+w1+jpeg+opr4+");"+" goto " + "   // ( if " + jpeg + w1 + opr5 + ")")
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                
                if token.tokenString==')':
                    token=lex()
                    
                    genquad("jump ,"," _,"," _,","_")
                    G=numberOfQuads
                    
                    
                    FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "b _")
                    FinalCodeCounter+=1
                    statements()
                  
                    
                    genquad("jump ,","_ ,"," _ ,",str(G-1))
                    NewG=numberOfQuads
                    
                    for s in range (0,len(ListOfQuads1)):
                        if(int(G) == int(ListOfQuads1[s][0])):
                            mylist = backpatch(ListOfQuads1[s],str(NewG+1))
                            ListOfQuads1[s]=mylist
                            
                            
                    
                else:
                    print("ERROR : ')' was expected, line:",line)
                    exit(1)
            else:
                print("ERROR : '(' was expected, line:",line)
                exit(1)
            Inwhile=0
# ***************************************************************************   
    def switchcaseStat():
        global token
        global rtx
        global batr
        global FinalCodeCounter
        global FinalCodeList
        global FunctionList
        if token.tokenString=='switchcase':
            token=lex()
            #exitlist=emptylist()
            while token.tokenString=='case':
                
                token=lex()
                
                if token.tokenString=='(':
                    token=lex()
                    
                    rtx = token.tokenString
                    #condtrue=token.tokenString
                    condition()
                    if token.tokenString==')':
                        
                        token=lex()
                        
                        if(token.tokenString=='{'):
                            token=lex()
                        
                        #backpatch(condtrue,nextquad())
                        
                        statements()
                        
                        #condfalse=token.tokenString
                        #e=makelist(nextquad())
                        genquad("jump,","_ ,","_ ,","_ ")
                        FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "b _")
                        FinalCodeCounter+=1
                        if token.tokenString=='}':
                            token=lex()
                            
                       
                        #merge(exitlist,e)
                        #backpatch(condfalse,nextquad())
                    else:
                        print("ERROR : ')' was expected, line:",line)
                        exit(1)
                else:
                    print("ERROR : '(' was expected, line:",line)
                    exit(1)
            
            
            if token.tokenString=='default':
                token=lex()
                #backpatch(exitlist,nextquad())
                batr = 1
                
                
                #statement()

# ***************************************************************************   
    def forcaseStat():
        global token
        global rtx
        global FinalCodeCounter
        global FinalCodeList
        if token.tokenString=='forcase':
            token=lex()
            #p1Quad=nextquad()
            while token.tokenString=='case':
                token=lex()
                if token.tokenString=='(':
                    token=lex()
                    rtx = token.tokenString
                    #condtrue=token.tokenString
                    condition()
                    
                    if token.tokenString==')':
                        token=lex()          
                        statements()
                      
                        genquad("jump,"," _,"," _,","_ ")
                        FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "b _")
                        FinalCodeCounter+=1
                        #backpatch(condfalse,nextquad()) 
                        
                    else:
                        print("ERROR : ')' was expected, line:",line)
                        exit(1)
                else:
                    print("ERROR : '(' was expected, line:",line)
                    exit(1)
               
            
            if token.tokenString=='default':
                token=lex()
                if(token.tokenString == ";"):
                    print("ERROR : ';' not in need, line:",line)
                    exit(1)
                

# ***************************************************************************   
    def incaseStat():
        global token
        if token.tokenString=='incase':
            token=lex()
            w=newtemp()
            
            genquad(":=","","_",w)
            while token.tokenString=='case':
                token=lex()
                if token.tokenString=='(':
                    token=lex()
                                      
                    condition()
                    if token.tokenString==')':
                        token=lex()
                        #backpatch(condtrue,nextquad())
                        #genquad(":=,",0,",_,",w)
                        statement()
                        #condfalse=token.tokenString
                        #backpatch(condfalse,nextquad())
                        #genquad("=,",w,0,p1Quad)    
                    else:
                        print("ERROR : ')' was expected, line:",line)
                        exit(1)
                else:
                    print("ERROR : '(' was expected, line:",line)
                    exit(1)
           
# ***************************************************************************   
    def returnStat():
        global token
        global Helpa
        global w 
        global goe
        global rtx
        global gp
        global gor
        global batr
        global returnStat
        global FunWriteOnArr
        global ProWriteOnArr
        global FinalCodeCounter
        global FinalCodeList
        global ArrayOfSyms
        global ArrayOfSymsHelp
        global KeepInformationForOut
        global GreenLight
        GreenLight = 0
        goe = 0
        
        if token.tokenString=='return':
            returnStat = 1
            token=lex()
            
            if token.tokenString=='(':
                token=lex()
                
                fd = token.tokenString
                if(fd in tolist):
                    rtx = token.tokenString
                    gp = 1
                else:
                    rtx = token.tokenString
                    gp = 0
                
                Eplace = token.tokenString
                expression()
                for c in range (0,len(FunctionList)):
                        if(fd == FunctionList[c][0]):
                            if(FunctionList[c][2] == " "):
                                if(FunctionList[c][3] == "in"):
                                    genquad("par ,",Helpa," ,CV,"," _")
                                    for bc in range (0,len(ArrayOfSyms)):
                                        if(Helpa==ArrayOfSyms[bc][0]):
                                            FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "addi fp,sp, offset")
                                            FinalCodeList.append("\t"+"\t"+"lw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                                            FinalCodeList.append("\t"+"\t"+"sw t1,-"+str(ArrayOfSyms[bc][2])+"(fp)")
                                            FinalCodeCounter+=1
                                elif(FunctionList[c][3] == "inout"):
                                    genquad("par ,",Helpa," ,REF,"," _")  
                            else:
                                if(FunctionList[c][3] == "in"):
                                    genquad("par ,",Helpa," ,CV,"," _")
                                    for bc in range (0,len(ArrayOfSyms)):
                                        if(Helpa==ArrayOfSyms[bc][0]):
                                            FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "addi fp,sp, offset")
                                            FinalCodeList.append("\t"+"\t"+"lw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                                            FinalCodeList.append("\t"+"\t"+"sw t1,-"+str(ArrayOfSyms[bc][2])+"(fp)")
                                            FinalCodeCounter+=1
                                if(FunctionList[c][3] == "inout"):
                                    genquad("par ,",Helpa," ,REF,"," _")
                                if(FunctionList[c][4] == "in"):
                                    genquad("par ,",Helpa," ,CV,"," _")
                                    for bc in range (0,len(ArrayOfSyms)):
                                        if(Helpa==ArrayOfSyms[bc][0]):
                                            FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "addi fp,sp, offset")
                                            FinalCodeList.append("\t"+"\t"+"lw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                                            FinalCodeList.append("\t"+"\t"+"sw t1,-"+str(ArrayOfSyms[bc][2])+"(fp)")
                                            FinalCodeCounter+=1
                                if(FunctionList[c][4] == "inout"):
                                    genquad("par ,",Helpa," ,REF,"," _")
                            goe = 1
                            w = newtemp()
                            genquad("par ,",w," ,RET,"," _ ")
                            FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "addi t0,sp,-offset")
                            FinalCodeList.append("\t"+"\t"+"sw t0,-8(fp)")
                            FinalCodeCounter+=1
                            genquad("call ,","_ ,"," _ ,",fd)
                if token.tokenString==')':
                    token=lex()
                    
                    if(batr==1 and token.tokenString==";"):
                        
                        token = lex()
                      
                    if(goe == 1):
                        genquad("retv ,","_ ,"," _ ,",w)
                        
                        for bc in range (0,len(ArrayOfSyms)):
                            if(w==ArrayOfSyms[bc][0]):
                                FinalCodeList.append("L"+str(FinalCodeCounter)+": "+"\t"+"lw t0,-"+ArrayOfSyms[bc][2]+"(sp)")
                                FinalCodeList.append("\t"+"\t"+"lw t1,(t0)")
                                FinalCodeList.append("\t"+"\t"+"lw t0,-8(sp)")
                                FinalCodeList.append("\t"+"\t"+"sw t1,(t0)")
                                FinalCodeCounter+=1
                        genquad("out ,","_ ,"," _ ,",Eplace)
                        for bc in range (0,len(ArrayOfSyms)):
                            if(w1==ArrayOfSyms[bc][0]):
                                FinalCodeList.append("L"+str(FinalCodeCounter)+": "+"\t"+"lw t0,-"+str(ArrayOfSyms[bc][2])+"offset(sp)")
                                FinalCodeList.append("\t"+"\t"+"li v0,1")
                                FinalCodeList.append("\t"+"\t"+"move a0, t1")
                                FinalCodeList.append("\t"+"\t"+"ecall")
                                FinalCodeCounter+=1
                    if(goe != 1 and gor == 1):
                        genquad("retv ,",w1," ,_ "," ,_ ")
                        
                        for bc in range (0,len(ArrayOfSyms)):
                            if(w1==ArrayOfSyms[bc][0]):
                                FinalCodeList.append("L"+str(FinalCodeCounter)+": "+"\t"+"lw t0,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                                FinalCodeList.append("\t"+"\t"+"lw t1,(t0)")
                                FinalCodeList.append("\t"+"\t"+"lw t0,-8(sp)")
                                FinalCodeList.append("\t"+"\t"+"sw t1,(t0)")
                                FinalCodeCounter+=1
                        genquad("out ,","_ ,"," _ ,",Eplace)
                        for bc in range (0,len(ArrayOfSyms)):
                            if(Eplace==ArrayOfSyms[bc][0]):
                                FinalCodeList.append("L"+str(FinalCodeCounter)+": "+"\t"+"lw t0,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                                FinalCodeList.append("\t"+"\t"+"li v0,1")
                                FinalCodeList.append("\t"+"\t"+"move a0, t1")
                                FinalCodeList.append("\t"+"\t"+"ecall")
                                FinalCodeCounter+=1
                    elif(goe == 0):
                        
                        for c in range(0,len(KeepInformationForOut)-1):
                            
                            if(Eplace == KeepInformationForOut[c]):
                                genquad("retv ,",KeepInformationForOut[c+1]," ,_ "," ,_ ")
                                GreenLight=1
                        if(GreenLight==0):
                            genquad("retv ,",Eplace," ,_ "," ,_ ")
                        for bc in range (0,len(ArrayOfSyms)):
                            if(Eplace==ArrayOfSyms[bc][0]):
                                FinalCodeList.append("L"+str(FinalCodeCounter)+": "+"\t"+"lw t0,-"+str(ArrayOfSyms[bc][2])+"offset(sp)")
                                FinalCodeList.append("\t"+"\t"+"lw t1,(t0)")
                                FinalCodeList.append("\t"+"\t"+"lw t0,-8(sp)")
                                FinalCodeList.append("\t"+"\t"+"sw t1,(t0)")
                                FinalCodeCounter+=1
                        for c in range(0,len(KeepInformationForOut)):
                            if(Eplace == KeepInformationForOut[c]):
                                genquad("out ,","_ ,"," _ ,",Eplace)
                        if(GreenLight==0):
                            genquad("out ,","_ ,"," _ ,",Eplace)
                        
                        for bc in range (0,len(ArrayOfSyms)):
                            if(Eplace==ArrayOfSyms[bc][0]):
                                FinalCodeList.append("L"+str(FinalCodeCounter)+": "+"\t"+"lw t0,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                                FinalCodeList.append("\t"+"\t"+"li v0,1")
                                FinalCodeList.append("\t"+"\t"+"move a0, t1")
                                FinalCodeList.append("\t"+"\t"+"ecall")
                                FinalCodeCounter+=1
                    if(token.tokenString != ";"):
                        print("ERROR : ';' was expected, line:",line)
                        exit(1)
                
                else:
                    print("ERROR : ')' was expected, line:",line)
                    exit(1)
                batr = 0
            else:
                print("ERROR : '(' was expected, line:",line)
                exit(1)
        
        
        
        
# ***************************************************************************   
    def callStat():
        global token
        global FunctionList
        global nam
        global CallList
        global Helpa
        global Helpb
        global Helpin
        global Helpin1
        global tr
        global FinalCodeCounter
        global FinalCodeList
        global ArrayOfSyms
        global ArrayOfSymsHelp
        if token.tokenString=='call':
           
            token=lex()
            ap = token.tokenString
            
            ID()
            
            if token.tokenString=='(':
                token=lex()
                
                actualparlist()
               
                CallList.append(Helpa)
                
                CallList.append(Helpb)
                CallList.append(Helpin)
                CallList.append(Helpin1)
                
                
                if(CallList[1]==" "):
                    if(CallList[2]=="in"):
                        genquad("par ,",CallList[0]," ,CV,"," _")
                        for bc in range (0,len(ArrayOfSyms)):
                            if(CallList[0]==ArrayOfSyms[bc][0]):
                                FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "addi fp,sp, offset")
                                FinalCodeList.append("\t"+"\t"+"lw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                                FinalCodeList.append("\t"+"\t"+"sw t1,-"+str(ArrayOfSyms[bc][2])+"(fp)")
                                FinalCodeCounter+=1
                    if(CallList[2]=="inout"):
                        genquad("par ,",CallList[0]," ,REF,"," _")
                else:
                    if(CallList[2]=="in"):
                        genquad("par ,",CallList[0]," ,CV,"," _")
                        for bc in range (0,len(ArrayOfSyms)):
                            if(CallList[0]==ArrayOfSyms[bc][0]):
                                FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "addi fp,sp, offset")
                                FinalCodeList.append("\t"+"\t"+"lw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                                FinalCodeList.append("\t"+"\t"+"sw t1,-"+str(ArrayOfSyms[bc][2])+"(fp)")
                                FinalCodeCounter+=1
                    if(CallList[2]=="inout"):
                        genquad("par ,",CallList[0]," ,REF,"," _")
                    if(CallList[3]=="in"):
                        genquad("par ,",CallList[1]," ,CV,"," _")
                        for bc in range (0,len(ArrayOfSyms)):
                            if(CallList[1]==ArrayOfSyms[bc][0]):
                                FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "addi fp,sp, offset")
                                FinalCodeList.append("\t"+"\t"+"lw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                                FinalCodeList.append("\t"+"\t"+"sw t1,-"+str(ArrayOfSyms[bc][2])+"(fp)")
                                FinalCodeCounter+=1
                    if(CallList[3]=="inout"):
                        genquad("par ,",CallList[1]," ,REF,"," _")
                genquad("call ,",ap," ,_"," ,_")
                FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "sw sp,-offset(fp)")
                FinalCodeList.append("\t"+"\t"+"addi sp, sp ," + "offset")
                FinalCodeList.append("\t"+"\t"+"jail L")
                FinalCodeList.append("\t"+"\t"+"addi sp, sp ,"+"-"+"offset")
                FinalCodeCounter+=1
                if token.tokenString==')':
                    token=lex()
                if(token.tokenString==';'):
                    token=lex()
                    
                else:
                    print("ERROR : ')' was expected, line:",line)
                    exit(1)
                
            else:
                print("ERROR : '(' was expected, line:",line)
                exit(1)

# ***************************************************************************   
    def printStat():
        global token
        global gp
        global rtx
        global fd
        global Helpa
        global Helpb
        global w
        global w1
        global goa
        global gor
        global geg
        global WriteOnC
        global CList
        global counter
        goa = 0
        
        global FinalCodeCounter
        global FinalCodeList
        global ArrayOfSyms
        global ArrayOfSymsHelp
        #global tolist
        #global PrintList 
        
        if token.tokenString=='print':
            token=lex()
            if token.tokenString=='(':
                token=lex()
                fd = token.tokenString   
                
                if(fd in tolist):
                    rtx = token.tokenString
                    gp = 1
                else:
                    rtx = token.tokenString
                    gp = 0
                
                if (token.tokenString==')'):
                    print("Error : print() needs value inside (),line: ",line )
                    exit(1)
                Eplace = token.tokenString       
                expression()
                
                for c in range (0,len(FunctionList)):
                        if(fd == FunctionList[c][0]):
                            if(FunctionList[c][2] == " "):
                                if(FunctionList[c][3] == "in"):
                                    genquad("par ,",Helpa," ,CV,"," _")
                                    for bc in range (0,len(ArrayOfSyms)):
                                        if(Helpa==ArrayOfSyms[bc][0]):
                                            FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "addi fp,sp, offset")
                                            FinalCodeList.append("\t"+"\t"+"lw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                                            FinalCodeList.append("\t"+"\t"+"sw t1,-"+str(ArrayOfSyms[bc][2])+"(fp)")
                                            FinalCodeCounter+=1
                                elif(FunctionList[c][3] == "inout"):
                                    genquad("par ,",Helpa," ,REF,"," _")  
                            else:
                                if(FunctionList[c][3] == "in"):
                                    genquad("par ,",Helpa," ,CV,"," _")
                                    for bc in range (0,len(ArrayOfSyms)):
                                        if(Helpa==ArrayOfSyms[bc][0]):
                                            FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "addi fp,sp, offset")
                                            FinalCodeList.append("\t"+"\t"+"lw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                                            FinalCodeList.append("\t"+"\t"+"sw t1,-"+str(ArrayOfSyms[bc][2])+"(fp)")
                                            FinalCodeCounter+=1
                                if(FunctionList[c][3] == "inout"):
                                    genquad("par ,",Helpa," ,REF,"," _")
                                if(FunctionList[c][4] == "in"):
                                    genquad("par ,",Helpb," ,CV,"," _")
                                    for bc in range (0,len(ArrayOfSyms)):
                                        if(Helpa==ArrayOfSyms[bc][0]):
                                            FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "addi fp,sp, offset")
                                            FinalCodeList.append("\t"+"\t"+"lw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                                            FinalCodeList.append("\t"+"\t"+"sw t1,-"+str(ArrayOfSyms[bc][2])+"(fp)")
                                            FinalCodeCounter+=1
                                if(FunctionList[c][4] == "inout"):
                                    genquad("par ,",Helpb," ,REF,"," _")
                            goa = 1
                            w = newtemp()
                            genquad("par ,",w," ,RET,"," _ ")
                            genquad("call ,",fd,", _,"," _ ")
   
                
                
                if token.tokenString==')':
                    if(goa == 1):
                        genquad("out ,",w," ", " ")
                        FinalCodeList.append("L"+str(FinalCodeCounter)+": "+"\t"+"li v0,1")
                        FinalCodeList.append("\t"+"\t"+"lw a0,-offset(s0)")
                        FinalCodeList.append("\t"+"\t"+"ecall")
                        FinalCodeCounter+=1
                    elif(goe != 1 and (gor == 1 or geg == 1)):
                        genquad("out ,",w1," ", " ")
                        FinalCodeList.append("L"+str(FinalCodeCounter)+": "+"\t"+"li v0,1")
                        FinalCodeList.append("\t"+"\t"+"lw a0,-offset(s0)")
                        FinalCodeList.append("\t"+"\t"+"ecall")
                        FinalCodeCounter+=1
                        if(WriteOnC==1):
                            CList.append("\t"+"L_"+str(counter)+": "+"printf(%d,&"+w1+");" + "   // (out " +w1 + "_ _)")
                            counter+=1
                            Clistlength = len(CList)
                    else:
                        
                        genquad("out ,",Eplace," ", " ")
                        
                        FinalCodeList.append("L"+str(FinalCodeCounter)+": "+"\t"+"lw t1,-offset(sp)")
                        FinalCodeList.append("\t"+"\t"+"...")
                        
                        FinalCodeCounter+=1
                        if(WriteOnC==1):
                            CList.append("\t"+"L_"+str(counter)+": "+"printf(%d,&"+Eplace+");" + "   // ( out " +Eplace + "_ _ )")
                            counter+=1
                            Clistlength = len(CList)
                    token=lex()
                    if token.tokenString != ";":
                        print("ERROR : ';' was expected, line:",line)   
                        exit(1)
                else:
                    print("ERROR : ')' was expected, line:",line)
                    exit(1)
            else:
                print("ERROR : '(' was expected, line:",line)
                exit(1)

# ***************************************************************************   
    def inputStat():
        global token
        global vlist2
        global CList
        global counter
        global FinalCodeCounter
        global FinalCodeCounter
        global FinalCodeList
        
        if token.tokenString=='input':
            
            token=lex()
            if token.tokenString=='(':
                token=lex()
                idplace = token.tokenString
                if(WriteOnC==1):
                    
                    CList.append("\t"+"L_"+str(counter)+": "+"scanf(%d,&"+idplace+");" + "   // (  inp " +idplace+ "_ _  ) ")
                    counter+=1
                    Clistlength = len(CList)
                genquad("inp  ,",idplace," ,_ "," ,_ ")
                FinalCodeList.append("L"+str(FinalCodeCounter)+": "+"\t"+"li v0, 5")
                FinalCodeList.append("\t"+"\t"+"ecall")
                
                FinalCodeCounter+=1
                if token.tokenString==')':
                    print("Error : input needs argument between () ,line: ",line)
                ID()
                
                if token.tokenString==')':
                    
                    token=lex()
                    
                    if token.tokenString != ";":
                        print("ERROR : ';' was expected, line:",line)   
                        exit(1)
                else:
                    print("ERROR : ')' was expected, line:",line)
                    exit(1)
            else:
                print("ERROR : '(' was expected, line:",line)
                exit(1)


# ***************************************************************************   
    def actualparlist():
        global token
        global CallList
        global gh
        global Helpa
        global Helpb
        global Helpin
        global Helpin1
        gh=5
        
        actualparitem()
        if(token.tokenString==")"):
            Helpb=" "
            Helpin1=" "
        while token.tokenString==',':
            token=lex()
            gh = 6
            actualparitem()
            break

# ***************************************************************************   
    def actualparitem():
        global token
        global CallList
        global Helpa
        global Helpb
        global Helpin
        global Helpin1
        global gh
        
        if(gh == 5):         
            
            if token.tokenString=='in':
                token=lex()
               
                Helpin = "in"
                Helpa=token.tokenString
                
                expression()
            elif token.tokenString=='inout':
                token=lex()
                Helpin = "inout"
                Helpa=token.tokenString
                ID()        
        if(gh == 6):
            
            if token.tokenString=='in':
                token=lex()
                Helpin1 = "in"
                Helpb=token.tokenString
                expression()
            elif token.tokenString=='inout':
                token=lex()
                Helpin1 = "inout"
                Helpb=token.tokenString
                ID()
        
# ***************************************************************************   
    def condition():
        global token
        global Btrue
        global Bfalse
        global rtx
        boolterm()
        #Btrue=Q1true
        #Bfalse=Q1false
        while token.tokenString=='or':
            token=lex()
            #backpatch(Bfalse,nextquad())
            rtx = token.tokenString
            boolterm()
            #Q2true=Q1true
            #Q2false=Q1false
            #Btrue=merge(Btrue,Q2true)
            #Bfalse=Q2false

# ***************************************************************************       
    def boolterm():
        global token
        global Qtrue
        global Qfalse
        global rtx 
        global w1
        global timh
        global FinalCodeCounter
        global FinalCodeList
        timh = 0
        global IfG
        boolfactor()
        #Qtrue=R1true
        #Qfalse=R1false
        while token.tokenString=='and':
           
            timh = 1
            token=lex()
            FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "b _")
            FinalCodeCounter+=1
            rtx = token.tokenString
            
            #backpatch(Qtrue,nextquad())
            boolfactor()
            
            #R2false=R1false
            #R2true=R1true
            #Qfalse=merge(Qfalse,R2false)
            #Qtrue=R2true
        

# ***************************************************************************   
    def boolfactor():
        global token
        global Btrue
        global Bfalse
        global R1true
        global R1false
        global relop
        
        if token.tokenString=='not':
            token = lex()
            if token.tokenString=='[':
                token=lex()
                
                condition()
                if token.tokenString==']':
                    #R1true=Btrue
                    #R1false=Bfalse
                    token=lex()
                else:
                    
                    print("ERROR : ']' was expected, line:",line)
                    exit(1)
            else:
                print("ERROR : '[' was expected, line:",line)
                exit(1)
                
        elif token.tokenString=='[':
            token=lex()
            while(token.tokenString != ']'):
                condition()
            if token.tokenString==']':
                #R1true=Btrue
                #R1false=Bfalse
                token=lex()
            else:
                print("ERROR : ']' was expected, line:",line)
                exit(1)
        else:   
            expression()
            #E1place=token.tokenString
            
            REL_OP()
            
            expression()
            
            #E2place=E1place
            #R1true=makelist(nextquad())
            #genquad(relop,E1place,E2place,"_")
            #R1false=makelist(nextquad())
            #genquad("jump","_","_","_")
# ***************************************************************************   
    def expression():
        global token
        global bo
        global w1
        global gor1
        global gor
        global geg
        global WriteOnC
        global counter
        global CList
        global Clistlength
        global FinalCodeCounter
        global FinalCodeList
        global shtem
        global ArrayOfSyms
        global ArrayOfSymsHelp
        global KeepInformationForOut
        global WhoIsToKeepInformationForOut
        geg = 0
        global Assing
        global AssingCount
        optionalSign()
        
        T1place=token.tokenString
        
        gor = 0
        bo = 5
        term()
          
        
        
        while token.tokenString=='+' or token.tokenString=='-':
            
            
            if(token.tokenString == "+" or token.tokenString=='-'):
                    
                gor = 1
                gor1 = 1
                geg = 1
                bo = 6
                
            
            ope = token.tokenString
            token=lex()
            
            T2place = token.tokenString
            w1=newtemp()
            ArrayOfSymsHelp.append(w1)
            ArrayOfSymsHelp.append("temporary variable")
            ArrayOfSymsHelp.append(shtem)
            ArrayOfSyms.append(ArrayOfSymsHelp)
            ArrayOfSymsHelp=list()
            KeepInformationForOut.append(WhoIsToKeepInformationForOut)
            KeepInformationForOut.append(w1)
            shtem+=4
        
            if(ope=="+"):
                
                if(Assing == 1 and AssingCount!=0):
                    genquad("+ ,",ArrayOfSyms[len(ArrayOfSyms)-2][0]+" ,",T2place+" ,",w1)
                if(Assing==1 and AssingCount==0):
                    genquad("+ ,",T1place+" ,",T2place+" ,",w1)
                
                
                    
                if((T1place in cletters) or (T1place in sletters)):
                    for bc in range (0,len(ArrayOfSyms)):
                        if(T1place==ArrayOfSyms[bc][0]):
                            FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "lw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                if(T1place in digits):
                        FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "li t1,"+T1place)
                if((T2place in cletters) or (T2place in sletters)):
                    for bc in range (0,len(ArrayOfSyms)):
                        if(T2place==ArrayOfSyms[bc][0]):
                            FinalCodeList.append("\t"+"\t"+"lw t2,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                if(T2place in digits):
                    FinalCodeList.append("\t"+"\t"+"lw t2,"+T2place)               
                FinalCodeList.append("\t"+"\t"+"add t1,t1,t2")
                for bc in range (0,len(ArrayOfSyms)):   
                    if(w1==ArrayOfSyms[bc][0]):
                        FinalCodeList.append("\t"+"\t"+"sw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                FinalCodeCounter+=1
                
                if(WriteOnC==1):
                    CList.append("\t"+"L_"+str(counter)+" "+w1+" = "+T1place+ope+T2place +";"+ " //  ( + " + T1place + "_" + T2place +"_" +  w1 + ")")
                    Clistlength = len(CList)
                    counter+=1    
            if(ope=="-"):
                genquad("- ,",T1place+" ,",T2place+" ,",w1)
                if((T1place in cletters) or (T1place in sletters)):
                    for bc in range (0,len(ArrayOfSyms)):
                        if(T1place==ArrayOfSyms[bc][0]):
                            FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "lw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                if(T1place in digits):
                        FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "li t1,"+T1place)
                if((T2place in cletters) or (T2place in sletters)):
                    for bc in range (0,len(ArrayOfSyms)):
                        if(T2place==ArrayOfSyms[bc][0]):
                            FinalCodeList.append("\t"+"\t"+"lw t2,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                if(T2place in digits):
                    FinalCodeList.append("\t"+"\t"+"lw t2,"+T2place)               
                FinalCodeList.append("\t"+"\t"+"sub t1,t1,t2")
                for bc in range (0,len(ArrayOfSyms)):   
                    if(w1==ArrayOfSyms[bc][0]):
                        FinalCodeList.append("\t"+"\t"+"sw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                FinalCodeCounter+=1
                if(WriteOnC==1):
                    CList.append("\t"+"L_"+str(counter)+" "+w1+" = "+T1place+ope+T2place +";"+ " //  ( - " + T1place + "_" + T2place + "_" + w1 + ")")
                    Clistlength = len(CList)
                    counter+=1 
            T1place=w1
            if(token.tokenString==';'):
                print("Error: after sign we need a variable ,line:" ,line)
                exit(1)
            AssingCount +=1
            ADD_OP()
            
            term()
            
        #Eplace=token.tokenString
        #Eplace=T1place
# ***************************************************************************   
    def ADD_OP():
        global token
        global bo 
        global geg
        
        if token.tokenString =="+":
            
            token=lex()
            
        elif token.tokenString=='-':
            
            token=lex()
    def term():
        global token
        global bo
        global w1
        global gor
        global gor1
        global counter
        global WriteOnC
        global CList
        global Clistlength
        global FinalCodeCounter
        global FinalCodeList
        global ArrayOfSyms
        global shtem
        global ArrayOfSymsHelp
        global AssingCount
        F1place=token.tokenString
        factor()
        gor = 0
        
        
        while token.tokenString=='*' or token.tokenString=='/':
            
            
            if(token.tokenString == "*" or token.tokenString=='/'):
                
                gor = 1
                gor1 = 1
                bo = 6
            
            ope = token.tokenString
            token=lex()
            
            F2place = token.tokenString
            w1=newtemp()
            ArrayOfSymsHelp.append(w1)
            ArrayOfSymsHelp.append("temporary variable")
            ArrayOfSymsHelp.append(shtem)
            ArrayOfSyms.append(ArrayOfSymsHelp)
            ArrayOfSymsHelp=list()
            shtem+=4
            if(ope == "*"):
                if(Assing == 1 and AssingCount!=0):
                    genquad("* ,",ArrayOfSyms[len(ArrayOfSyms)-2][0]+" ,",F2place+" ,",w1)
                if(Assing == 1 and AssingCount==0):
                    genquad("* ,",F1place+" ,",F2place+" ,",w1)
                if((F1place in cletters) or (F1place in sletters)):
                    for bc in range (0,len(ArrayOfSyms)):
                        if(F1place==ArrayOfSyms[bc][0]):
                            FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "lw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                if(F1place in digits):
                        FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "li t1,"+F1place)
                if((F2place in cletters) or (F2place in sletters)):
                    for bc in range (0,len(ArrayOfSyms)):
                        if(F2place==ArrayOfSyms[bc][0]):
                            FinalCodeList.append("\t"+"\t"+"lw t2,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                if(F2place in digits):
                    FinalCodeList.append("\t"+"\t"+"lw t2,"+F2place)               
                FinalCodeList.append("\t"+"\t"+"mul t1,t1,t2")
                for bc in range (0,len(ArrayOfSyms)):   
                    if(w1==ArrayOfSyms[bc][0]):
                        FinalCodeList.append("\t"+"\t"+"sw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                FinalCodeCounter+=1
                if(WriteOnC==1):
                    CList.append("\t"+"L_"+str(counter)+" "+w1+" = "+F1place+ope+F2place +";"+ " //  ( * " + F1place + "_"  + F2place + "_" +  w1 + ")")
                    Clistlength = len(CList)
                    counter+=1
            if(ope=="/"):
                genquad("/ ,",F1place+" ,",F2place+" ,",w1)
                if((F1place in cletters) or (F1place in sletters)):
                    for bc in range (0,len(ArrayOfSyms)):
                        if(F1place==ArrayOfSyms[bc][0]):
                            FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "lw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                if(F1place in digits):
                        FinalCodeList.append("L" + str(FinalCodeCounter) + ": " + "\t" + "li t1,"+F1place)
                if((F2place in cletters) or (F2place in sletters)):
                    for bc in range (0,len(ArrayOfSyms)):
                        if(F2place==ArrayOfSyms[bc][0]):
                            FinalCodeList.append("\t"+"\t"+"lw t2,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                if(F2place in digits):
                    FinalCodeList.append("\t"+"\t"+"lw t2,"+F2place)               
                FinalCodeList.append("\t"+"\t"+"div t1,t1,t2")
                for bc in range (0,len(ArrayOfSyms)):   
                    if(w1==ArrayOfSyms[bc][0]):
                        FinalCodeList.append("\t"+"\t"+"sw t1,-"+str(ArrayOfSyms[bc][2])+"(sp)")
                FinalCodeCounter+=1
                if(WriteOnC==1):
                    CList.append("\t"+"L_"+str(counter)+" "+w1+" = "+F1place+ope+F2place +";"+ " //  ( / " + F1place + "_" + F2place + "_" + w1 + ")")
                    Clistlength = len(CList)
                    counter+=1
            F1place=w1
            if(token.tokenString==';'):
                print("Error: after sign we need a variable ,line:" ,line)
                exit(1)
            AssingCount+=1
            MUL_OP()
            factor()
            
        #Tplace=token.tokenString
        #Tplace=F1place
# ***************************************************************************   

    def factor():
        global token
        global jp
        global geg
        INTEGER()
        
        if token.tokenString=='(':
            token=lex()
            
            expression()
            
            if token.tokenString==')':
                token=lex()
            else:
                print("ERROR : ')' was expected, line:",line)
                exit(1)
        else:
            jp = token.tokenString
            
            ID()
           
            idtail()
            
# ***************************************************************************   

    def idtail():
        global token
        global jp
        if token.tokenString=='(':
            
            if(jp not in tolist):
                print("Error: " +jp +" function not defined ,line",line)
                exit(1)
            token=lex()
            actualparlist()
            if token.tokenString==')':
                token=lex()
            else:
                print("ERROR : ')' was expected, line:",line)
                exit(1)
        
# ***************************************************************************   

    def optionalSign():
        global token
        ADD_OP()
# ***************************************************************************   

    def REL_OP():
        global token
        global rtx
        global w1
        global gp
        global bo
        global opr
        global opr1
        global opr2
        global opr3
        global opr4
        global opr5
        global jpeg
        global Inwhile
        global G1
        global IfG1
        global Inif
        jpeg = token.tokenString
        
        if token.tokenString=='=':
            token=lex()
            opr = token.tokenString
            if(bo==5 and gp == 0 and Inif==1):
                genquad("= ,",rtx+" ,",opr+" ,",str(IfG1+3))
            if(bo==5 and gp == 0 and Inwhile==1):
                genquad("= ,",rtx+" ,",opr+" ,",str(G1+3))
            if(bo==5 and gp == 0 and Inwhile == 0 and Inif==0):
                genquad("= ,",rtx+" ,",opr+" ,","_ ")
            if(bo==6 and gp == 0):
                genquad("= ,",w1+" ,",opr+" ,","_ ")
        elif token.tokenString=='<=':
            token=lex()
            opr5 = token.tokenString
            if(bo==5 and Inif==1):
               genquad("<= ,",rtx+" ,",opr5+" ,",str(IfG1+3)) 
            if(bo==5 and Inwhile==1):
               genquad("<= ,",rtx+" ,",opr5+" ,",str(G1+3)) 
            if(bo==5 and Inwhile ==0 and Inif==0):
               genquad("<= ,",rtx+" ,",opr5+" ,","_ ")
            if(bo==6):
                genquad("<= ,",w1+" ,",opr5+" ,","_ ")    
        elif token.tokenString=='>=':
            
            token=lex()
            opr3 = token.tokenString
            if(bo==5 and gp == 0 and Inif==1):
                genquad(">= ,",rtx+" ,",opr3+" ,",str(IfG1+3))
            if(bo==5 and gp == 0 and Inwhile==1):
                genquad(">= ,",rtx+" ,",opr3+" ,",str(G1+3))
            if(bo==5 and gp == 0 and Inwhile==0 and Inif==0):
                genquad(">= ,",rtx+" ,",opr3+" ,","_ ")
            if(bo==6 and gp == 0):
                genquad(">= ,",w1+" ,",opr3+" ,","_ ")
        elif token.tokenString=='>':
            token=lex()
            opr1 = token.tokenString
            if(bo==5 and gp == 0 and Inif == 1):
                genquad("> ,",rtx+" ,",opr1+" ,",str(G1+3))
            if(bo==5 and gp == 0 and Inwhile == 1):
                genquad("> ,",rtx+" ,",opr1+" ,",str(G1+3))
            if(bo==5 and gp == 0 and Inwhile ==0 and Inif==0):
                genquad("> ,",rtx+" ,",opr1+" ,","_ ")
            if(bo==6 and gp == 0):
                genquad("> ,",w1+" ,",opr1+" ,","_ ")
        elif token.tokenString=='<':
            
            token=lex()
            opr2 = token.tokenString
            if(bo==5 and gp == 0 and Inif==1):
                genquad("< ,",rtx+" ,",opr2+" ,",str(G1+3))
            if(bo==5 and gp == 0 and Inwhile==1):
                genquad("< ,",rtx+" ,",opr2+" ,",str(G1+3))
            if(bo==5 and gp == 0 and Inwhile==0 and Inif==0):
                genquad("< ,",rtx+" ,",opr2+" ,","_ ")
            if(bo==6 and gp == 0):
                genquad("< ,",w1+" ,",opr2+" ,","_ ")
        elif token.tokenString=='<>':
            token=lex()
            opr4 = token.tokenString
            if(bo==5 and gp == 0 and Inif==1):
                genquad("<> ,",rtx+" ,",opr4+" ,",str(IfG1+3))
            if(bo==5 and gp == 0 and Inwhile==1):
                genquad("<> ,",rtx+" ,",opr4+" ,",str(G1+3))
            if(bo==5 and gp == 0 and Inwhile==0 and Inif==0):
                genquad("<> ,",rtx+" ,",opr4+" ,","_ ")
            if(bo==6 and gp == 0):
                genquad("<> ,",w1+" ,",opr4+" ,","_ ")
# ***************************************************************************   

    

# ***************************************************************************   

    def MUL_OP():
        global token
        
        if token.tokenString=='*':
            token=lex()
        elif token.tokenString=='/':
            token=lex()

# ***************************************************************************   
    def INTEGER():
        global token
        if ((token.tokenString[0] in digits) or ((token.tokenString) in digits)):
            token=lex()

# ***************************************************************************
    def ID():
        global token
        global tolist

        if((token.tokenString not in Desmeumenes_lexeis) ):
            
         
            if ((token.tokenString[0] in sletters) or (token.tokenString[0] in cletters)): 
                token = lex()        
# ***************************************************************************   
    program()
suntaktikos()

f1 = open('test.int','w')
for gv in range(0,length):
    f1.write(str(ListOfQuads1[gv]) + "\n")
    
f1.close
print("Intermediate code has been completed Successfully!")

# ***************************************************************************
if(WriteOnC==1):
    f2 = open('test.c','w')
    for gv in range(0,Clistlength):
        f2.write(str(CList[gv]) + "\n")
    f2.close

if(WriteOnArrayOfSymbols == 1):
    
    f3 = open('test.symb','w')
    for gv in range(0,len(ArrayOfSyms)):
        f3.write(str(ArrayOfSyms[gv]) + "\n")
    f3.close
f4 = open('test.asm','w')
for gv in range(0,len(FinalCodeList)):
    f4.write(str(FinalCodeList[gv]) + "\n")
f4.close    
print("Finalcode has been completed Successfully!")