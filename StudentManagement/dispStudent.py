import StudentManagement.newStudent as ns
def display():
    print("~~~~~~Students Details~~~~~~")
    for i in range(0,len(ns.rollno)):
            print("Student Roll No.= "+ns.rollno[i])
            print("Student Name= "+ns.name[i])
            print("Student Address= "+ns.addr[i])
            print("Student Phone NO.= "+ns.pno[i])
            i+=1