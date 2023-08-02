def fileHandle(file="demo.txt"):
    try:
        f=open(file,"+a")
        f.writelines(["rollno=21 ","Name=Ansh ","Class=Tyif "])
        f.seek(0)
        print(f.readlines())
    except IOError:
        print("File Operation Failed")

fileHandle()

