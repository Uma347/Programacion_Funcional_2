object Hola {

  def sfiboE(x:Int):Unit={
    var a = 0
    var b = 1
    var c = 1
	var d = 0
    for(i <- 0 to (x-1)){
      print(a+" ")
      d=a+b+c
	  a=b
      b=c
	  c=d   
    }
  }
  def fiboR(x:Int):Int={
    if(x==0) return 0 
    else if(x==1) 1
    else if(x==2) 1
    else fiboR(x-1) + fiboR(x-2) + fiboR(x-3)
  }

  def sfiboR(x:Int):Unit={
    for(i <- 0 to (x-1)){
      print(fiboR(i)+" ")   
    }
  }
  
  def main(args:Array[String]):Unit = { 
    println("Introduce un numero: ")
    val num = scala.io.StdIn.readInt()
	println("Sucesion fibonacci con funcion estructurada")
    sfiboE(num)
	println("\nSucesion fibonacci con funcion recursiva")
    sfiboR(num)
  }
  
}