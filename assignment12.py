import StudentManagement.deletee as sdel
import StudentManagement.newStudent as sadd
import StudentManagement.search as ssear
import StudentManagement.dispStudent as sdis
import StudentManagement.count as scount
class inavlidOption(Exception):
    def __init__(self, *msg):
        super().__init__(*msg)
        
i=1
while i==1:
    try:
        print("Enter 1 To Add Student Record\n"\
              "Enter 2 To Display All Student Record\n"\
              "Enter 3 To Delete a Student Record\n"\
              "Enter 4 To Search a Student Record\n"\
              "Enter 5 To Count Number Of Record"  )
        c=int(input('Enter number: '))
        if(c==1):
            sadd.add()
        elif(c==2):
            sdis.display()
        elif(c==3):
            sdel.dele()
        elif(c==4):
            ssear.search()
        elif(c==5):
            scount.counted()
        else:
            raise inavlidOption("Invalid choice")
    except inavlidOption as io:
        print(io.args[0])
    a=int(input('Enter 1 to continue else any key exit: '))
    if a!=1:
        exit()
    else:
        i=a