namespace Library1

module modfibos =
    let generafibo3 n =
        let mutable result=""
        let mutable v1 = 0
        let mutable v2 = 1
        let mutable v3 = 1
        let mutable aux = 1
        for i in 0..n do
           result <- result+" "+v1.ToString()
           aux <- (v1 + v2) + v3
           v1 <- v2
           v2 <- v3
           v3 <- aux                   
        result
    
    let rec fib3 n =
        if n=0 then 0
        elif n=1 then 1
        elif n=2 then 1
        else fib3(n-1) + fib3(n-2)+ fib3(n-3)

    let genera n =
        let mutable s = ""
        for i in 0..n do
            s<-s+" "+ (fib3 i).ToString()
        s


type Class1() = 
    member this.X = "F#"
