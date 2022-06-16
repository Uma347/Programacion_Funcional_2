fiboR =
    let x 0 = 0
        x 1 = 1
        x 2 = 1
        x n = fiboR (n-3) + fiboR (n-2) + fiboR (n-1)
        fx = map x [0 .. ]
    in \f -> (fx !! f)

fiboE n = take n . map head $ iterate (\(a:b:c:d) -> b:c:(a+b+c):d) [0,1,1]

main = do 
    putStrLn "Ingrese un numero"
    n <- getLine
    let num = (read n :: Int)
    putStrLn "Sucesion fibonacci con funcion estructurada: "
    print (fiboE num)
    putStrLn "Sucesion fibonacci con funcion recursiva "
    print (map fiboR[0..num-1])