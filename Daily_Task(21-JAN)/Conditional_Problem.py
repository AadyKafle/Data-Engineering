#1
#to check if number is +ve ,-ve or 0

x = int(input('Enter a number to check'))

if(x==0):
    print(f'the number {x} is Zero')
elif(x<0):
    print(f'the number {x} is negative')
else:
    print(f'the number {x} is positive')

#to check the marks of a student

y = int(input('Enter your marks to check'))

if( x>40 and x<80) :
    print(f'Yeah you passed')
elif(x>=80):
    print(f'Congrats, you got distinction')
elif(x<40):
    print(f'You are a Failure in Life')