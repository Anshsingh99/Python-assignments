import StudentManagement.newStudent as ns
def dele():
    rn=input("Enter The Roll NO. To Delete Details: ")
    i=ns.rollno.index(rn)
    ns.name.pop(i)
    ns.rollno.pop(i)
    ns.addr.pop(i)
    ns.pno.pop(i)
    print("Record Deleted Successfully!!")