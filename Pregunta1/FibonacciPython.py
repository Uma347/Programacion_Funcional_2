
def sucecionfiboE(x):
    a,b,c=0,1,1
    s=""
    for i in range(1,x+1):
        if i==1:
            s=s+"0 "
        else:
            if i<=3:
                s=s+"1 "
            else:
                s=s+str(a+b+c)+" "
                a,b,c=b,c,a+b+c
    return s
def fiborecursivo(x):
    if x<=1: 
        return 0
    if x<=3: 
        return 1
    return fiborecursivo(x-1)+fiborecursivo(x-2)+fiborecursivo(x-3)

def sucesionfiboR(x):
   if x==0:
       return ""
   return(sucesionfiboR(x-1)+ str(fiborecursivo(x))+" ")
    
print("Introduzca un número:", end=" ")
num=int(input())
print("Sucesión Fibonacci con funcion estructurada")
print(sucecionfiboE(num))
print("Sucesión Fibonacci con funcion recursiva")
print(sucesionfiboR(num))
