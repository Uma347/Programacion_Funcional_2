object ScalaFunTemporales {
    // Fibonnaci con funciones temporales
    def generarFibo(n:Int,f1:Int,f2:Int,f3:Int, fun:(Int,Int,Int)=>Int):Unit = {
        if (n >= 0) {
            var f = fun(f1, f2, f3)
            print(f)
            print(" ")
            generarFibo(n-1, f2, f3, f, fun)
        }
    }

    def main(args:Array[String]):Unit = {
        var suma3terminos = (f1:Int, f2:Int, f3:Int) => f1 + f2 + f3
        var fibonnaci = (n:Int) => generarFibo(n, -1, 1, 0, suma3terminos)
        
        println("Generar lo n terminos:")
        println("Fibonnaci con funciones temporales")
        var n = scala.io.StdIn.readInt()
        fibonnaci(n)
    }
}