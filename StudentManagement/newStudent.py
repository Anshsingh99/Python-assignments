name=[]
rollno=[]
addr=[]
pno=[]

def add():
    i=0
    f=open("Sturecord.txt","+a")
    try:
        print("Enter Students Details: ")
        name.append(input("Enter Name Of The Student: "))
        rollno.append(input("Enter Roll No. Of Student: "))
        addr.append(input("Enter Address Of Student:"))
        pno.append(input("Enter Phone No. Of Student: "))

        f.writelines(["Student Roll No.= "+rollno[i]+"\n"])
        f.writelines(["Student Name= "+name[i]+"\n"])
        f.writelines(["Student Address= "+addr[i]+"\n"])
        f.writelines(["Student Phone NO.= "+pno[i]+"\n"])    
        i+=1
    except:
        if(IOError):
            print("Error In Storing Data")
        elif(IndexError):
            print("Error In Accessing Index")
        else:
            print("Record Added Successfully")
