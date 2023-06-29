def df(roll,name):
    li=[roll,name]
    tu=(roll,name)
    se={roll,name}
    dic={
        "rollno":roll,
        "name":name
    }
    print("Values Are Stored:- ")
    print(li)
    print(tu)
    print(se)
    print(dic)
print("Enter Rollno and Name to Store it:")
r=input()
n=input()
df(r,n)
print("Enter New Rollno and Name to Store it:") #HERE VALUES ARE CHANGING AT RUN TIME
r=input()
n=input()
df(r,n)