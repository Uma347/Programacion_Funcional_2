object Hola {

  def fsuperior(funciontipo:(Int)=>Unit):Unit={
    funciontipo(5)
  }

  def sfiboE(x:Int):Unit={
    var a = 0
    var b = 1
    var c = 1
	var d = 0
    for(w <- 0 to x+1){
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
    else fiboR(x-1) + fiboR(x-2)+ fiboR(x-3)
  }

  def sfiboR(x:Int):Unit={
    for(w <- 0 to x+1){
      print(fiboR(w)+" ")    
    }
  }
  
  def main(args:Array[String]):Unit = {
    println("Ingresa un numero")
    val a = scala.io.StdIn.readInt()
	println("Sucesion fibonacci funcion estructurada (orden superior)")
    fsuperior(sfiboE)
    println()
	println("Sucesion fibonacci funcion recursiva (orden superior)")
    fsuperior(sfiboR)
  }
  
}