a=[]
print('ENTER 5 VALUES')
for i in range(1,6):
    a.append(int(input("enter element: ")))
print(a)
print('sum of list ='+ str(sum(a)))
print('Minimum value of list ='+ str(min(a)))
print('Maximum value of list ='+ str(max(a)))
a.sort()
print('List in assending order = '+str(a))
a.reverse()
print('List in desending order = '+str(a))
c=tuple(a)
print('List as a tuple = '+str(c))
del a # list a is deleted
