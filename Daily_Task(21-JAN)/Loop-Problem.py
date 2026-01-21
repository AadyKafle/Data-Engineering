#sum of all number of a list
lst = list(map(int, input("Enter list of numbers separated by a space: ").split()))
sum=0
for i in range(0,len(lst)) :
    sum=sum+lst[i]

print(f'the sum of list is {sum}')

#fibonacci series print
a=0
b=1
n=int(input('enter n of fibonacci series'))
if(n==1):
    print('fibonacci series: 0')
elif(n>1):
      for i in range(n):
        print(a)
        a , b = b,a +b