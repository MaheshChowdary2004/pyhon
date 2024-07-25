def pow(x,n):
    return x**n
def add(x,n):
    return x+n
def sub(x,n):
    return x-n
def mul(x,n):
    return x*n
def div(x,n):
    if n==0:
        return "Error! Division by zero."
    return x / n
def main():
    print("Choose an operation:")
    print("1. Power (Pow(x,n))")
    print("2. Addition (Add(x,n))")
    print("3. Subtraction (Sub(x,n))")
    print("4. Multiplication (Mul(x,n))")
    print("5. Division (Div(x,n))")
    choice = input("Enter choice (1/2/3/4/5): ")
    if choice in ['1','2','3','4','5']:
        x = float(input("Enter the value of x: "))
        n = float(input("Enter the value of n: "))
        if choice == '1':
            print(f"Result: {pow(x,n)}")
        elif choice == '2':
            print(f"Result: {add(x,n)}")
        elif choice == '3':
            print(f"Result: {sub(x,n)}")
        elif choice == '4':
            print(f"Result: {mul(x,n)}")
        elif choice == '5':
            print(f"Result: {div(x,n)}")
    else:
        print("Invalid choice!")
if __name__ == "__main__":
    main()
