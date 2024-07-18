def HappyNumber(n):    
    rem=n
    sum=0;    
        
    #Calculates the sum of squares of digits    
    while(rem > 0):
        digit=rem%10;    
        sum = sum+digit**2    
        rem =rem//10;    
    return sum
num=int(input("enter the number:"))
result = num
while(result != 1 and result != 4):    
    result = HappyNumber(result);    
     
#Happy number always ends with 1    
if(result == 1):    
    print(" is a happy number");    
#Unhappy number ends in a cycle of repeating numbers which contain 4    
elif(result == 4):    
    print(" is not a happy number");   
