object ScalaLambda {
    
    def fiboR(n:Int,f1:Int,f2:Int,f3:Int, fun:(Int,Int,Int)=>Int):Unit = {
        if (n >= 0) {
            var f = fun(f1, f2, f3)
            print(f)
            print(" ")
            fiboR(n-1, f2, f3, f, fun)
        }
    }

    def main(args:Array[String]):Unit = {
		val fiboE = (n:Int) =>{
			var a = 0
			var b = 0
			var c = 1
			var d = 0
			for(i <- 0 to n) {
				d = c + b + a
				a = b
				b = c
				c = d 
			}
			a}
        var suma3 = (f1:Int, f2:Int, f3:Int) => f1 + f2 + f3
        var sfiboR = (n:Int) => fiboR((n-1), -1, 1, 0, suma3)
        println("Introduce un numero")
        var num = scala.io.StdIn.readInt()
		println("Sucesion fibonacci con funcion estructurada (lambda)")
        for(i <- 0 to num-1) {
			print(fiboE(i)+" ") }
		println()
		println("Sucesion fibonacci con funcion recursiva (lambda)")
        sfiboR(num)
    }
}