from tkinter import *

def set_text(text):
    l.delete(0,END)
    l.insert(0,text)
    return

root = Tk()

root.minsize(500,500)
root.maxsize(500,500);

show=Label(root, text="|Welcome|")
show.pack()
show1=Label(root,text="_______________________")
show1.pack()


textlab1=Label(root, text="Enter First Number:")
textlab1.pack()
e1 = Entry(root)
e1.pack()

textlab2=Label(root, text="Enter Second Number:")
textlab2.pack()
e2 = Entry(root)
e2.pack()
l = Entry(root)
def callback():
    total = int(e1.get()) + int(e2.get())
    return total

b = Button(root, text="add them", command=set_text(callback()))

for widget in ( l, b):
    widget.pack()

b.mainloop()