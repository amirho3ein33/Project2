#Practice 1
#def plus( x, y):
#    print(x + y)
#a = int(input("Enter first number :"))
#b = int(input("Enter second number :"))
#plus(a,b)

#Practice 2
#def plus(x,*y):
#    su=0
#    su+=x
#    for i in y:
#        su+=i
#    print (su)
#plus(1)
#plus(1,2,3,4)

#Practice 3
def fib(n):
    if(n == 1 or n == 2):
        return (1)
    else:
        return (fib(n - 1)+fib(n - 2))
n=int(input("Enter your number :"))
print(fib(n))
