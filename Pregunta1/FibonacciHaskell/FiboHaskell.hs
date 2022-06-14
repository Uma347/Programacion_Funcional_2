sFiboE :: Integer -> Integer -> Integer -> Integer -> IO() 
sFiboE n a b c = do
    if n >= 0
    then do
       let d = a+b+c
       putStr $ (show(d)++" ")
       sFiboE (n-1) b c d
    else putStr ""

fiboR :: Integer -> Integer
fiboR 0 = 0
fiboR 1 = 1
fiboR 2 = 1
fiboR n = fiboR(n-1) + fiboR(n-2) + fiboR(n-3)

sFiboR :: Integer -> IO() 
sFiboR n = do
    if n >= 0
    then do
       sFiboR (n-1)
       putStr $ (show(fiboR n)++" ")
    else putStr ""

main :: IO()
main = do
    putStrLn ("Introduxca un numero:")
    n <- getLine
    putStrLn ("Sucesion fibonacci con funcion estructural")
    sFiboE ((read n)-1) (-1) 1 0
    putStrLn ("\nSucesion fibonacci con funcion recursiva")
    sFiboR ((read n)-1)
