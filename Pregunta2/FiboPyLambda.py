

from functools import reduce
 
fiboE = lambda n: reduce(lambda x,n:[x[1],x[2],x[0]+x[1]+x[2]], range(n),[0,1,1])[0]
sfibE = lambda n: reduce(lambda c,n: c+str(fiboE(n))+" ",range(n),"")
                    
fiboR = lambda n: 0 if n == 0 else  ( 1 if n <= 2 else fiboR(n-1) + fiboR(n-2)+ fiboR(n-3))
sfiboR= lambda n: "" if n == 0 else sfiboR(n-1)+ str(fiboR(n-1))+ " "

print("Introduzca un número:", end=" ")
num=int(input())
print("Sucesión Fibonacci con funcion estructurada(lambda)")
print(sfibE(num))
print("Sucesión Fibonacci con funcion recursiva(lambda)")
print(sfiboR(num))

