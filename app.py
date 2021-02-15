'''import math
from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter import filedialog'''

def integral(f,a,b) :
    result = 0
    dt = 0.0001
    t = a
    while t < b :
        result += dt*f(t)
        t += dt
    return result  

def func_T_mean(x):
    return x

def func_T_mag (x):
    return abs(x)

Tmean = abs(integral(func_T_mean,-1,0)/-1)
Tmag = integral(func_T_mag,-0.4,0)/-1

print("INTEGRAL :"+str(integral(func_T_mean,0,2)))

print("Tmean :"+str(Tmean))
print("Tmag :"+str(Tmag))


OSI = (1/2)*(1-(Tmean/ Tmag))
print("OSI :"+str(OSI))






'''
def about_():
    root_a = Tk()
    root_a.title("About")
    root_a.minsize(300,300)
    root_a.maxsize(300,300);  
    aboutLable = Label(root_a, text="Programe for computing oscillatory shear index \nmade by Nikola Nikolic\nKragujevac 2019")
    aboutLable.pack()
    root_a.mainloop()


root = Tk()

root.title("Programe for computing oscillatory shear index")
root.minsize(800,500)
root.maxsize(800,500)





# create a toplevel menu
menubar = Menu(root)

menubar.add_command(label="About", command=about_)
menubar.add_command(label="Quit", command=root.quit)

# display the menu
root.config(menu=menubar)

TitleLabel = Label(root,text = "Programe for computing oscillatory shear index)",borderwidth=3, relief="sunken")
TitleLabel.config(font=("Courier", 15, "bold",), bg="#e0e0e0", )
TitleLabel.pack()

img = ImageTk.PhotoImage(Image.open("image_1.png"))
panel = Label(root, image = img)
panel.pack(side = "left", fill = "both")


inp1_Label = Label(root,text = "Enter time ciklus from 0 to : ")
inp1_Label.place(x = 380, y = 30)

entry_box_1 = Entry(root, width=10 )
entry_box_1.place(x = 570, y = 30)

inp1_Label = Label(root,text = "Enter Local Stress WSS : ")
inp1_Label.place(x = 380, y = 100)

entry_box_1 = Entry(root, width=10 )
entry_box_1.place(x = 570, y = 100)

button_1 = Button(root, text='Analyze') # , command=''
button_1.place(x = 570, y = 138)

inp1_Label = Label(root,text = "RESULT : Oscillatory shear index is :")
inp1_Label.place(x = 380, y = 230)

entry_box_1 = Entry(root, width=10 )
entry_box_1.place(x = 570, y = 230)







root.mainloop()

'''