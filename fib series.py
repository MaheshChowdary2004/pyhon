def fib(n):
    if(n<0 or n==0):
        print("invalid")
    elif(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return fib(n-1)-fib(n-2)
n=int(input("terms"))
f=fib(n)
print(f)
