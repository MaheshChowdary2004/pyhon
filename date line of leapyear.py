date=input("enter date:")
c=date.split("/")
b=list(map(int,c))
print(b)
input_year=(b[2])
if(input_year%400==0 or input_year%100!=0 and input_year==0):
    print("%d leap year"%input_year)
else:
    print("%d not a leap:"%input_year)
