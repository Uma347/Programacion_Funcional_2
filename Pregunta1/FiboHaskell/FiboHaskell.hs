import System.Info

main = do
  print "Introduzca un numero"
  n1 <- getLine
  let x = read n1 :: Integer
  
  let fiboR :: Integer->Integer; fiboR 1= (0);fiboR 2=(1);fiboR 3=(1);fiboR n= (fiboR (n-1) + fiboR (n-2) + fiboR (n-3))
  let sfiboR :: Integer->String; sfiboR 0=""; sfiboR n= sfiboR(n-1)++show (fiboR n) ++" "
  
   
  print "Sucesion fibonacci con funcion recursiva"
  putStrLn $ show(sfiboR x)
