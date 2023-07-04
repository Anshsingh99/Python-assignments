import tkinter as tk
import webbrowser as wb
root=tk.Tk()
root.title("NAVIGATE")
l=tk.Label(root,text="Enter the anime name to search",
           font=("Times New Roman",20))
l.grid()
e1=tk.Entry(root,font=("Times New Roman",20),width=25)
e1.grid()
def search():
    name=e1.get()
    wb.open("https://aniwatch.to/search?keyword="+name)
    print(f"Navigating to 'ZORO.TV' to search {name}")
b=tk.Button(root,text="SEARCH",font=("TIMES NEW ROMAN",15),
            command=search,bg="skyblue",
            activebackground="lightblue")
b.grid()
tk.mainloop()