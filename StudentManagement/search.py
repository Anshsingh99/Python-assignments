import StudentManagement.newStudent as ns
def search():   
    rn=input("Enter The Roll NO. To See Details: ")
    i=ns.rollno.index(rn)
    print("Student Roll No.= "+ns.rollno[i])
    print("Student Name= "+ns.name[i])
    print("Student Address= "+ns.addr[i])
    print("Student Phone NO.= "+ns.pno[i])
