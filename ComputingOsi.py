import math
from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter import filedialog
import time


def about_():
    root_a = Tk()
    root_a.title("About")
    root_a.minsize(300,300)
    root_a.maxsize(300,300);  
    aboutLable = Label(root_a, text="Program for computing oscillatory shear index \nmade by Nikola Nikolic\nKragujevac 2019")
    aboutLable.pack()
    root_a.mainloop()



    

root = Tk()


###################################################################
def _main_():
    def openFile_():
        fileName = filedialog.askopenfilename(filetypes = (("SHEAR_STRESSES",'*.txt'),('All files', "*.*")) )
        return fileName
    location =  openFile_() 

    start = time.time()
    with open(location, 'r') as file:
         data = file.read().split("\n")


    SHEAR_STRESSES = []

    for i in range(1,len(data)):
            stress_com_ =  data[i].split()
            if i%2 == 1 :
                 SHEAR_STRESSES.append([float(i) for i in stress_com_]) 
    
    #print(SHEAR_STRESSES)

    def integral(f,startIntX,endIntX) :
        result = 0
        dt = 0.001
        t = startIntX
        while t < endIntX :
             result += dt*f
             t += dt
        return result  

    Mod_Tau=[]

    for i in range(0,len(SHEAR_STRESSES)):
         sum_component = math.sqrt( (SHEAR_STRESSES[i][0])**2 + (SHEAR_STRESSES[i][1])**2 + (SHEAR_STRESSES[i][2])**2 )
         Mod_Tau.append(sum_component)

##print("sum_component")
#print(Mod_Tau)

    I_Mod_WSS = []

    for i in range(0,len(SHEAR_STRESSES)):
        Tmag = integral(Mod_Tau[i],0+i-1,0.2+i-1)
        I_Mod_WSS.append(Tmag)


#print("Tmag")
#print(I_Mod_WSS)

    I_WSS = []

    for i in range(0,len(SHEAR_STRESSES)):
         component_T_xyz = []
         component_T_xyz.append(integral(SHEAR_STRESSES[i][0],0+i-1,0.2+i-1))
         component_T_xyz.append(integral(SHEAR_STRESSES[i][1],0+i-1,0.2+i-1))
         component_T_xyz.append(integral(SHEAR_STRESSES[i][2],0+i-1,0.2+i-1))
         I_WSS.append(component_T_xyz)

#print("I_WSS")
#print(I_WSS)

    Mod_I_WSS = []

    for i in range(0,len(SHEAR_STRESSES)):
        sum_comp_T = math.sqrt( (I_WSS[i][0])**2 + (I_WSS[i][1])**2 + (I_WSS[i][2])**2 )
        Mod_I_WSS.append(sum_comp_T)

#print("Tmean")
#print(Mod_I_WSS)

    OSI = []

    for i in range(0,len(SHEAR_STRESSES)):
        if Mod_I_WSS[i] == 0 or I_Mod_WSS[i] == 0 :
            osi_t = 0
        else :
             osi_t= 0.5*(1-(Mod_I_WSS[i]/I_Mod_WSS[i]))
        OSI.append(abs(osi_t*10**14))

#print("OSI")
#print(OSI)
#print("OSI")

    f = open('OSI_RESULT.txt','w')
    end = time.time()
    f.write("..............................RESULT..................................\n\n") 
    f.write("Running Time... "+str(round(end - start, 2))+" sec \n\n")
    for i in range(0,len(OSI)):
          f.write("For Nodes :" +str(i)+ " OSI is :"+"%.2f" % OSI[i]+
          "        SHEAR STRESSES: "+str(SHEAR_STRESSES[i][0])+
          " " +str(SHEAR_STRESSES[i][1])+
          " "+str(SHEAR_STRESSES[i][2])+ "\n")
    
    f.write("...........................................................\n")  
    
    result = open("OSI_RESULT.txt").read()
    R = Text(root,heigh = 85,width = 250)
    R.pack()
    R.insert(END,result)
 
###################################################################


root.title("Program for computing oscillatory shear index")
root.minsize(1050,600)
root.maxsize(1050,600)


# create a toplevel menu
menubar = Menu(root)

menubar.add_command(label="About", command=about_)
menubar.add_command(label="Quit", command=root.quit)

# display the menu
root.config(menu=menubar)

TitleLabel = Label(root,text = "Program for computing oscillatory shear index",borderwidth=3, relief="sunken")
TitleLabel.config(font=("Courier" ,15, "bold",), bg="#e0e0e0", )
TitleLabel.pack()

inp1_Label = Label(root,text = "Pick shear stress file from your directory ",borderwidth=3, relief="flat")
inp1_Label.place(x = 300, y = 52)
inp1_Label.config(font=("Courier", 10, "bold",), bg="#e0e0e0", )
inp1_Label.pack()

img = ImageTk.PhotoImage(Image.open("image_1.png"))
panel = Label(root, image = img)
panel.pack(side = "left", fill = "both")


#inp1_Label = Label(root,text = "Choise shear stress file from your directory ")
#inp1_Label.place(x = 380, y = 52)

inp1_Label = Label(root,text = "-----------------------------PICK--FILE--FOR--RESULT------------------------------")
inp1_Label.place(x = 380+50, y = 52+50) 
    

button_1 = Button(root, text='Open File ', command=_main_)  
button_1.place(x = 720, y = 30)
root.mainloop()

















