i=1 
while i==1:
    first=int(input('Enter first number: '))
    second=int(input('Enter second number: '))
    op=input('Enter the operator (*,/,+,-,%): ')
    if op=='+':
        print('addition ='+ str((first+second)))
    elif op=='-':
        print('subtraction ='+ str((first-second)))
    elif op=='*':
        print('Multiplication ='+ str((first*second)))
    elif op=='/':
        print('Division ='+ str((first/second)))
    elif op=='%':
        print('Remainder ='+ str((first%second)))
    else:
        print('invalid choice')
    a=int(input('Enter 1 to continue else any key exit: '))
    if a!=1:
        exit()
    n=a