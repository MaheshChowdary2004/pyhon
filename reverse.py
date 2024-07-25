string=input('Enter the string:')
reverse=''
for i in range(len(string),0,-1):
   reverse+=string[i-1]
print('The reverse string is',reverse)
