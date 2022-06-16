fiboR :: Integer -> Integer
fiboR 0 = 0
fiboR 1 = 1
fiboR 2 = 1
fiboR n = fiboR(n-1) + fiboR(n-2) + fiboR(n-3)

sFibo :: Integer -> (Integer ->Integer) -> IO() 
sFibo n fun = do
    if n >= 0
    then do
       sFibo (n-1) fun
       putStr $ (show(fun n)++" ")
    else putStr ""

main :: IO()
main = do
    putStrLn ("Introduce un numero:")
    n <- getLine
    let x = read n :: Integer
    let fibonnaci = sFibo (x-1)
    putStrLn ("Fibonnaci con funcion de orden Superior")
    fibonnaci fiboR