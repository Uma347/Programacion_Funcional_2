
def sucecionfiboE(x):
    a,b,c=0,1,1
    s=""
    for i in range(0,x):
        if i==0:
            s=s+"0 "
        else:
            if i<=2:
                s=s+"1 "
            else:
                s=s+str(a+b+c)+" "
                a,b,c=b,c,a+b+c
    return s
def fiborecursivo(x):
    if x==0: 
        return 0
    if x<=2: 
        return 1
    return fiborecursivo(x-1)+fiborecursivo(x-2)+fiborecursivo(x-3)

def sucesionfiboR(x):
   if x==0:
       return ""
   return(sucesionfiboR(x-1)+ str(fiborecursivo(x-1))+" ")
    
print("Introduzca un número:", end=" ")
num=int(input())
print("Sucesión Fibonacci con funcion estructurada")
print(sucecionfiboE(num))
print("Sucesión Fibonacci con funcion recursiva")
print(sucesionfiboR(num))
