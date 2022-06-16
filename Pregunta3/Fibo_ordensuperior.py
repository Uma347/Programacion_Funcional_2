def desp(funcion, x=0):
    return funcion(x)

def f_ordensuperior(t):
    if t=="r":
        print("Sucesión Fibonacci con funcion recursiva")
        def fiborecursivo(x=0):
            if x==0: 
                return 0
            if x<=2: 
                return 1
            return fiborecursivo(x-1)+fiborecursivo(x-2)+fiborecursivo(x-3)

        def sucesionfiboR(x=0):
            if x==0:
                return ""
            return(sucesionfiboR(x-1)+ str(fiborecursivo(x-1))+" ")
        
        return sucesionfiboR
    if t=="e":
        print("Sucesión Fibonacci con funcion estructurada")
        def sucesionfiboE(x=0):
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
        return sucesionfiboE
       
print("Introduzca un número:", end=" ")
num=int(input())
print(desp(f_ordensuperior("e"),num))
print(desp(f_ordensuperior("r"),num))