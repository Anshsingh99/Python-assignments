import mathsmodule as m
class inavlidOption(Exception):
    def __init__(self, *msg):
        super().__init__(*msg)

obj=m.mathsmod()
i=1
while i==1:
    try:
        print("Enter 1 For Arithmatic Operation\n"\
            "Enter 2 For Trigometric Operation\n"\
            "Enter 3 For Power Operation\n"\
            "Enter 4 For Angular Operation\n"\
            "Enter 5 For Set Operations"  )
        c=int(input('Enter number: '))
        if(c==1):
            obj.arithfunc()
        elif(c==2):
            obj.trigofunc()
        elif(c==3):
            obj.powerfunctions()
        elif(c==4):
            obj.angularfunc()
        elif(c==5):
            obj.setoperat()
        else:
            raise inavlidOption("Invalid choice")
    except inavlidOption as io:
        print(io.args[0])
    a=int(input('Enter 1 to continue else any key exit: '))
    if a!=1:
        exit()
    else:
        i=a
