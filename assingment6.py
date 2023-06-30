
def df(roll,name):
    li=[roll,name]
    t1=(roll,name)
    se={roll,name}
    dic={
        "rollno":roll,
        "name":name
    }
    print("Values Are Stored:- ")
    print(li)
    print(t1)
    print(se)
    print(dic)

    print("Enter New Rollno and Name to Store it:") #HERE VALUES ARE CHANGING AT RUN TIME
    r=input()
    n=input()

    li.append([r,n])
    t2=(r,n)
    t1=t1+t2
    se.add((r,n))
    d={
        "rollno_new":roll,
        "name_new":name
    }
    dic.update(d)
    print("Values After Change:- ")
    print(li)
    print(t1)
    print(se)
    print(dic)

df("21","ansh")


