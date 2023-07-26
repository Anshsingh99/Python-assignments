# assignment operator
x = 3
print("Before:",x)
x+= 2
print("after +=:",x)
x = 10
print("Before:",x)
x-=4
print("after -=:",x)
x = 10
print("Before:",x)
x*= 2
print("after *=:",x)
x = 10
print("Before:",x)
x/= 2
print("after /=:",x)

# special (membership) operator
name = "ansh"
print("in operator: ","a" in name)

# comparison (relational) operator
x = 5
y = 10
print("x:",x,"y:",y)
print("Equal:",x==y)
print("not equal:",x!=y)
print("greater than:",x>y)
print("less than:",x<y)

#arithmetic operator
a = 78
b = 57
print("a:",a,"b:",b)
print("add:",a+b)
print("Subtract:",a-b)
print("multiply:",a*b)
print("divide:",a/b)
print("mod:",a%b)
print("exponent:",a**b)
print("floor division:",a//b)

# bitwise operator
a = 9
b = 2
print("a:",a,"b:",b)
print("bitwise and:",a&b)
print("bitwise or:",a|b)
print("bitwise xor:",a^b)
print("right shift:",a>>b)
print("left shift:",a<<b)

# logical operator
a = True
b = False
print("a:",a,"b:",b)
print("and operator:",a and b)
print("or operator:",a or b)
print("not operator:",not a)

# Identity operator
a = 10
b = 10
print("a:",a)
print("is operator:",a is b)
print("is not operator:",a is not 10)
