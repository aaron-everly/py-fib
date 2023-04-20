import turtle  
ttl = turtle.Turtle() 
wndw = turtle.Screen()   

ttl.color('blue')


heights = []
widths = []

n = 12

def fib(n):
    a = 0
    b = 1
    value = 0

    n = int(n)


    for i in range(2, n + 1):
        value = a + b
        a = b
        b = value
        widths.insert(i, value)
        
    return widths

fib(n)

# first square
ttl.forward(widths[1] * 10)  
ttl.left(90)  
ttl.forward(widths[1] * 10)  
ttl.left(90)  
ttl.forward(widths[1] * 10)  
ttl.left(90)  

# second square
ttl.forward(widths[1] * 10 + widths[1] * 10)  
ttl.left(90)  
ttl.forward(widths[1] * 10)  
ttl.left(90)  
ttl.forward(widths[1] * 10)  
ttl.left(90)  

# third square
ttl.right(90)
ttl.forward(widths[1] * 10)  
ttl.left(90)
ttl.forward(widths[2] * 10 + widths[2] * 10)
ttl.left(90)  
ttl.forward(widths[1] * 10 + widths[1] * 10)
ttl.left(90)  
ttl.forward(widths[3] * 10)  
ttl.left(90)  

# fourth square
ttl.right(90)
ttl.forward(widths[1] * 10 / 2)  
ttl.right(90)
ttl.forward(widths[2] * 10 + widths[2] * 10)
ttl.right(90)  
ttl.forward(widths[2] * 10 + widths[2] * 10)
ttl.right(90)  
ttl.forward(widths[2] * 10 + widths[2] * 10) 
ttl.right(90)  

# fourth square
ttl.right(90)
ttl.forward(widths[2] * 10 + widths[2] * 10) 
ttl.left(90)
ttl.forward(widths[1] * 10 + widths[2] * 10 + widths[3] * 10 + widths[3] * 10)
ttl.left(90)  
ttl.forward(widths[1] * 10 + widths[2] * 10 + widths[3] * 10)
ttl.left(90)  
ttl.forward(widths[1] * 10 + widths[2] * 10 + widths[3] * 10) 
ttl.left(90)  

# fifth square
ttl.left(90)
ttl.forward(widths[3] * 10 + widths[3] * 10) 
ttl.left(90)
ttl.forward(widths[3] * 10 + widths[3] * 10 + widths[3] * 10)
ttl.left(90)  
ttl.forward(widths[3] * 10 + widths[3] * 10 + widths[3] * 10)
ttl.left(90)  
ttl.forward(widths[3] * 10 + widths[3] * 10 + widths[3] * 10) 
ttl.right(90)  

# sixth square
ttl.left(90)
ttl.forward(widths[3] * 10 + widths[3] * 10) 
ttl.right(90)
ttl.forward(widths[1] * 10 + widths[1] * 10 + widths[6] * 10)
ttl.right(90)  
ttl.forward(widths[1] * 10 + widths[1] * 10 + widths[6] * 10)
ttl.right(90)  
ttl.forward(widths[1] * 10 + widths[1] * 10 + widths[6] * 10) 
ttl.right(90)  


ttl.end_fill()
turtle.done()