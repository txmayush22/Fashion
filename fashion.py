from tkinter import *
root=Tk()
root.geometry("1350x700")




##################################################################################################################

canvas_polo = Canvas(root,background='sky blue', width = 1000, height = 700)      
canvas_polo.pack()

entry=Entry(root)
entry.place(x = 0,y = 0)

#blue
imgPoloBlue= PhotoImage(file="E:\Assignments\python\BY JHONTY g\Fashion\Polo\poloBlue.png")      
canvas_polo.create_image(10,10, anchor=NW, image=imgPoloBlue)

labelPoloBlue=Label(canvas_polo,text="Polo Blue").place(x = 40,y = 160) 
labelPoloBluePrice=Label(canvas_polo,text="$20").place(x = 55,y = 185)
#red
imgPoloRed= PhotoImage(file="E:\Assignments\python\BY JHONTY g\Fashion\Polo\poloRed.png")      
canvas_polo.create_image(420,10, anchor=NW, image=imgPoloRed)

labelPoloRed=Label(canvas_polo,text="Polo Red").place(x = 450,y = 160) 
labelPoloRedPrice=Label(canvas_polo,text="$25").place(x = 465,y = 185)

#grey
imgPoloGrey= PhotoImage(file="E:\Assignments\python\BY JHONTY g\Fashion\Polo\poloGrey.png")      
canvas_polo.create_image(830,10, anchor=NW, image=imgPoloGrey)

labelPoloGrey=Label(canvas_polo,text="Polo Grey").place(x = 860,y = 160) 
labelPoloGreyPrice=Label(canvas_polo,text="$30").place(x = 875,y = 185)

#green
imgPoloGreen= PhotoImage(file="E:\Assignments\python\BY JHONTY g\Fashion\Polo\poloGreen.png")      
canvas_polo.create_image(10,450, anchor=NW, image=imgPoloGreen)

labelPoloGreen=Label(canvas_polo,text="Polo Green").place(x = 40,y = 600) 
labelPoloGreenPrice=Label(canvas_polo,text="$25").place(x = 60,y = 625)

#yellow
imgPoloYellow= PhotoImage(file="E:\Assignments\python\BY JHONTY g\Fashion\Polo\poloYellow.png")      
canvas_polo.create_image(420,450, anchor=NW, image=imgPoloYellow)

labelPoloYellow=Label(canvas_polo,text="Polo Yellow").place(x = 450,y = 600) 
labelPoloYellowPrice=Label(canvas_polo,text="$20").place(x = 465,y = 625)

#white
imgPoloWhite= PhotoImage(file="E:\Assignments\python\BY JHONTY g\Fashion\Polo\poloWhite.png")      
canvas_polo.create_image(830,450, anchor=NW, image=imgPoloWhite)

labelPoloWhite=Label(canvas_polo,text="Polo White").place(x = 860,y = 600) 
labelPoloWhitePrice=Label(canvas_polo,text="$20").place(x = 875,y = 625)


####################################################################################################


####################################################################################################
def displayFullSleeve():
    canvas_polo.pack_forget()
    canvas_Hoodie.pack_forget()
    canvas_fullsleeve.pack()


canvas_fullsleeve = Canvas(root,background='navy blue', width = 1000, height = 700)

buttonFullSleeve= Button(root,text="next",command=displayFullSleeve)
buttonFullSleeve.place(x=5,y=5,width=40,height=40)

entry=Entry(root)
entry.place(x = 0,y = 0)

#blue
imgFullSleeveBlue= PhotoImage(file="E:\Assignments\python\BY JHONTY g\Fashion\FullSleeve\poloBlue.png")      
canvas_fullsleeve.create_image(10,10, anchor=NW, image=imgFullSleeveBlue)

labelFullSleeveBlue=Label(canvas_fullsleeve,text="Full Sleeve Blue").place(x = 40,y = 160) 
labelFullSleeveBluePrice=Label(canvas_fullsleeve,text="$200").place(x = 55,y = 185)
#red
imgFullSleeveRed= PhotoImage(file="E:\Assignments\python\BY JHONTY g\Fashion\FullSleeve\poloRed.png")      
canvas_fullsleeve.create_image(420,10, anchor=NW, image=imgFullSleeveRed)

labelFullSleeveRed=Label(canvas_fullsleeve,text="Full Sleeve Red").place(x = 450,y = 160) 
labelFullSleeveRedPrice=Label(canvas_fullsleeve,text="$25").place(x = 465,y = 185)

#grey
imgFullSleeveGrey= PhotoImage(file="E:\Assignments\python\BY JHONTY g\Fashion\FullSleeve\poloGrey.png")      
canvas_fullsleeve.create_image(830,10, anchor=NW, image=imgFullSleeveGrey)

labelFullSleeveGrey=Label(canvas_fullsleeve,text="Full Sleeve Grey").place(x = 860,y = 160) 
labelFullSleeveGreyPrice=Label(canvas_fullsleeve,text="$30").place(x = 875,y = 185)

#green
imgFullSleeveGreen= PhotoImage(file="E:\Assignments\python\BY JHONTY g\Fashion\FullSleeve\poloGreen.png")      
canvas_fullsleeve.create_image(10,450, anchor=NW, image=imgFullSleeveGreen)

labelFullSleeveGreen=Label(canvas_fullsleeve,text="Full Sleeve Green").place(x = 40,y = 600) 
labelFullSleeveGreenPrice=Label(canvas_fullsleeve,text="$25").place(x = 60,y = 625)

#yellow
imgFullSleeveYellow= PhotoImage(file="E:\Assignments\python\BY JHONTY g\Fashion\FullSleeve\poloYellow.png")      
canvas_fullsleeve.create_image(420,450, anchor=NW, image=imgFullSleeveYellow)

labelFullSleeveYellow=Label(canvas_fullsleeve,text="Full Sleeve Yellow").place(x = 450,y = 600) 
labelFullSleeveYellowPrice=Label(canvas_fullsleeve,text="$20").place(x = 465,y = 625)

#white
imgFullSleeveWhite= PhotoImage(file="E:\Assignments\python\BY JHONTY g\Fashion\FullSleeve\poloWhite.png")      
canvas_fullsleeve.create_image(830,450, anchor=NW, image=imgFullSleeveWhite)

labelFullSleeveWhite=Label(canvas_fullsleeve,text="Full Sleeve White").place(x = 860,y = 600) 
labelFullSleeveWhitePrice=Label(canvas_fullsleeve,text="$20").place(x = 875,y = 625)



####################################################################################################
def displayHoodie():
    canvas_polo.pack_forget()
    canvas_fullsleeve.pack_forget()
    canvas_Hoodie.pack()


canvas_Hoodie = Canvas(root,background='white', width = 1000, height = 700)

buttonHoodie= Button(root,text="3rd",command=displayHoodie)
buttonHoodie.place(x=50,y=18,width=40,height=30)




imgHoodieBlue= PhotoImage(file="E:\Assignments\python\BY JHONTY g\Fashion\Hoodie\poloBlue.png")      
canvas_Hoodie.create_image(10,10, anchor=NW, image=imgHoodieBlue)

labelHoodieeBlue=Label(canvas_Hoodie,text="Hoodie Blue").place(x = 40,y = 160) 
labelHoodieBluePrice=Label(canvas_Hoodie,text="$200").place(x = 55,y = 185)
#red
imgHoodieRed= PhotoImage(file="E:\Assignments\python\BY JHONTY g\Fashion\Hoodie\poloRed.png")      
canvas_Hoodie.create_image(420,10, anchor=NW, image=imgHoodieRed)

labelHoodieRed=Label(canvas_Hoodie,text="Hoodie Red").place(x = 450,y = 160) 
labelHoodieRedPrice=Label(canvas_Hoodie,text="$25").place(x = 465,y = 185)

#grey
imgHoodieGrey= PhotoImage(file="E:\Assignments\python\BY JHONTY g\Fashion\Hoodie\poloGrey.png")      
canvas_Hoodie.create_image(830,10, anchor=NW, image=imgHoodieGrey)

labelHoodieGrey=Label(canvas_Hoodie,text="Hoodie Grey").place(x = 860,y = 160) 
labelHoodieGreyPrice=Label(canvas_Hoodie,text="$30").place(x = 875,y = 185)

#green
imgHoodieGreen= PhotoImage(file="E:\Assignments\python\BY JHONTY g\Fashion\Hoodie\poloGreen.png")      
canvas_Hoodie.create_image(10,450, anchor=NW, image=imgHoodieGreen)

labelHoodieGreen=Label(canvas_Hoodie,text="Hoodie Green").place(x = 40,y = 600) 
labelHoodieGreenPrice=Label(canvas_Hoodie,text="$25").place(x = 60,y = 625)

#yellow
imgHoodieYellow= PhotoImage(file="E:\Assignments\python\BY JHONTY g\Fashion\Hoodie\poloYellow.png")      
canvas_Hoodie.create_image(420,450, anchor=NW, image=imgHoodieYellow)

labelHoodieYellow=Label(canvas_Hoodie,text="Hoodie Yellow").place(x = 450,y = 600) 
labelHoodieYellowPrice=Label(canvas_Hoodie,text="$20").place(x = 465,y = 625)

#white
imgHoodieWhite= PhotoImage(file="E:\Assignments\python\BY JHONTY g\Fashion\Hoodie\poloWhite.png")      
canvas_Hoodie.create_image(830,450, anchor=NW, image=imgHoodieWhite)

labelHoodieWhite=Label(canvas_Hoodie,text="Hoodie White").place(x = 860,y = 600) 
labelHoodieWhitePrice=Label(canvas_Hoodie,text="$20").place(x = 875,y = 625)



#New CMD added today
buttonFullSleeve= Button(root,text="<",command=displayFullSleeve)
buttonFullSleeve.place(x=5,y=400,width=100,height=50)

buttonHoodie= Button(root,text=">",command=displayHoodie)
buttonHoodie.place(x=1200,y=400,width=100,height=50)
