print("Enter a number: ")
n = input()
print("") 
print("sequence or number? (s/n): ")
c = input()
print("") 


def fib(n):
    a = 0
    b = 1
    value = 0

    n = int(n)
    if c == "s":
        print(a)
        print(b)

    for i in range(2, n + 1):
        value = a + b
        a = b
        b = value

        if c == "s":
            print(value)
    
    if c == "n":
        n = str(n)
        value = str(value)
        print("Fib of " + n + " is: " + value)

fib(n)
