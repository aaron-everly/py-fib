import turtle  
ttl = turtle.Turtle() 
wndw = turtle.Screen()   

ttl.color('blue')


lengths = []

n = 8

def fib(n):
    a = 0
    b = 1
    value = 0

    n = int(n)


    for i in range(2, n + 1):
        value = a + b
        a = b
        b = value
        lengths.insert(i, value)

    return lengths

fib(n)

# first square
ttl.forward(lengths[1] * 10)  
ttl.left(90)  
ttl.forward(lengths[1] * 10)  
ttl.left(90)  
ttl.forward(lengths[1] * 10)  
ttl.left(90)  

# second square
ttl.forward(lengths[1] * 10 + lengths[1] * 10)  
ttl.left(90)  
ttl.forward(lengths[1] * 10)  
ttl.left(90)  
ttl.forward(lengths[1] * 10)  
ttl.left(90)  

# third square
ttl.right(90)
ttl.forward(lengths[1] * 10)  
ttl.left(90)
ttl.forward(lengths[2] * 10 + lengths[2] * 10)
ttl.left(90)  
ttl.forward(lengths[1] * 10 + lengths[1] * 10)
ttl.left(90)  
ttl.forward(lengths[3] * 10)  
ttl.left(90)  

# fourth square
ttl.right(90)
ttl.forward(lengths[1] * 10 / 2)  
ttl.right(90)
ttl.forward(lengths[2] * 10 + lengths[2] * 10)
ttl.right(90)  
ttl.forward(lengths[2] * 10 + lengths[2] * 10)
ttl.right(90)  
ttl.forward(lengths[2] * 10 + lengths[2] * 10) 
ttl.right(90)  

# fourth square
ttl.right(90)
ttl.forward(lengths[2] * 10 + lengths[2] * 10) 
ttl.left(90)
ttl.forward(lengths[1] * 10 + lengths[2] * 10 + lengths[3] * 10 + lengths[3] * 10)
ttl.left(90)  
ttl.forward(lengths[1] * 10 + lengths[2] * 10 + lengths[3] * 10)
ttl.left(90)  
ttl.forward(lengths[1] * 10 + lengths[2] * 10 + lengths[3] * 10) 
ttl.left(90)  

# fifth square
ttl.left(90)
ttl.forward(lengths[3] * 10 + lengths[3] * 10) 
ttl.left(90)
ttl.forward(lengths[3] * 10 + lengths[3] * 10 + lengths[3] * 10)
ttl.left(90)  
ttl.forward(lengths[3] * 10 + lengths[3] * 10 + lengths[3] * 10)
ttl.left(90)  
ttl.forward(lengths[3] * 10 + lengths[3] * 10 + lengths[3] * 10) 
ttl.right(90)  

# sixth square
ttl.left(90)
ttl.forward(lengths[3] * 10 + lengths[3] * 10) 
ttl.right(90)
ttl.forward(lengths[1] * 10 + lengths[1] * 10 + lengths[6] * 10)
ttl.right(90)  
ttl.forward(lengths[1] * 10 + lengths[1] * 10 + lengths[6] * 10)
ttl.right(90)  
ttl.forward(lengths[1] * 10 + lengths[1] * 10 + lengths[6] * 10) 
ttl.right(90)  


ttl.end_fill()
turtle.done()