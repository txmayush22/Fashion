from tkinter import *
root=Tk()
root.geometry("1350x700")


##################################################################################################################
canvas_polo = Canvas(root,background='sky blue', width = 1000, height = 700)      
canvas_polo.place(x=150,y=0)

entry=Entry(root)
entry.place(x = 0,y = 0)

#blue
imgPoloBlue= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/Polo/poloBlue.png")      
canvas_polo.create_image(10,10, anchor=NW, image=imgPoloBlue)

labelPoloBlue=Label(canvas_polo,text="Polo Blue").place(x = 40,y = 160) 
labelPoloBluePrice=Label(canvas_polo,text="$20").place(x = 55,y = 185)
#red
imgPoloRed= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/Polo/poloRed.png")      
canvas_polo.create_image(420,10, anchor=NW, image=imgPoloRed)

labelPoloRed=Label(canvas_polo,text="Polo Red").place(x = 450,y = 160) 
labelPoloRedPrice=Label(canvas_polo,text="$25").place(x = 465,y = 185)

#grey
imgPoloGrey= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/Polo/poloGrey.png")      
canvas_polo.create_image(830,10, anchor=NW, image=imgPoloGrey)

labelPoloGrey=Label(canvas_polo,text="Polo Grey").place(x = 860,y = 160) 
labelPoloGreyPrice=Label(canvas_polo,text="$30").place(x = 875,y = 185)

#green
imgPoloGreen= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/Polo/poloGreen.png")      
canvas_polo.create_image(10,450, anchor=NW, image=imgPoloGreen)

labelPoloGreen=Label(canvas_polo,text="Polo Green").place(x = 40,y = 600) 
labelPoloGreenPrice=Label(canvas_polo,text="$25").place(x = 60,y = 625)

#yellow
imgPoloYellow= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/Polo/poloYellow.png")      
canvas_polo.create_image(420,450, anchor=NW, image=imgPoloYellow)

labelPoloYellow=Label(canvas_polo,text="Polo Yellow").place(x = 450,y = 600) 
labelPoloYellowPrice=Label(canvas_polo,text="$20").place(x = 465,y = 625)

#white
imgPoloWhite= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/Polo/poloWhite.png")      
canvas_polo.create_image(830,450, anchor=NW, image=imgPoloWhite)

labelPoloWhite=Label(canvas_polo,text="Polo White").place(x = 860,y = 600) 
labelPoloWhitePrice=Label(canvas_polo,text="$20").place(x = 875,y = 625)


####################################################################################################
######################

####################################################################################################

canvas_fullsleeve = Canvas(root,background='navy blue', width = 1000, height = 700)
canvas_fullsleeve.place(x=1500,y=0)
#blue
imgFullSleeveBlue= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/FullSleeve/poloBlue.png")      
canvas_fullsleeve.create_image(10,10, anchor=NW, image=imgFullSleeveBlue)

labelFullSleeveBlue=Label(canvas_fullsleeve,text="Full Sleeve Blue").place(x = 40,y = 160) 
labelFullSleeveBluePrice=Label(canvas_fullsleeve,text="$200").place(x = 55,y = 185)
#red
imgFullSleeveRed= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/FullSleeve/poloRed.png")      
canvas_fullsleeve.create_image(420,10, anchor=NW, image=imgFullSleeveRed)

labelFullSleeveRed=Label(canvas_fullsleeve,text="Full Sleeve Red").place(x = 450,y = 160) 
labelFullSleeveRedPrice=Label(canvas_fullsleeve,text="$25").place(x = 465,y = 185)

#grey
imgFullSleeveGrey= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/FullSleeve/poloGrey.png")      
canvas_fullsleeve.create_image(830,10, anchor=NW, image=imgFullSleeveGrey)

labelFullSleeveGrey=Label(canvas_fullsleeve,text="Full Sleeve Grey").place(x = 860,y = 160) 
labelFullSleeveGreyPrice=Label(canvas_fullsleeve,text="$30").place(x = 875,y = 185)

#green
imgFullSleeveGreen= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/FullSleeve/poloGreen.png")      
canvas_fullsleeve.create_image(10,450, anchor=NW, image=imgFullSleeveGreen)

labelFullSleeveGreen=Label(canvas_fullsleeve,text="Full Sleeve Green").place(x = 40,y = 600) 
labelFullSleeveGreenPrice=Label(canvas_fullsleeve,text="$25").place(x = 60,y = 625)

#yellow
imgFullSleeveYellow= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/FullSleeve/poloYellow.png")      
canvas_fullsleeve.create_image(420,450, anchor=NW, image=imgFullSleeveYellow)

labelFullSleeveYellow=Label(canvas_fullsleeve,text="Full Sleeve Yellow").place(x = 450,y = 600) 
labelFullSleeveYellowPrice=Label(canvas_fullsleeve,text="$20").place(x = 465,y = 625)

#white
imgFullSleeveWhite= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/FullSleeve/poloWhite.png")      
canvas_fullsleeve.create_image(830,450, anchor=NW, image=imgFullSleeveWhite)

labelFullSleeveWhite=Label(canvas_fullsleeve,text="Full Sleeve White").place(x = 860,y = 600) 
labelFullSleeveWhitePrice=Label(canvas_fullsleeve,text="$20").place(x = 875,y = 625)



####################################################################################################


canvas_Hoodie = Canvas(root,background='white', width = 1000, height = 700)
canvas_Hoodie.place(x=1500,y=0)

imgHoodieBlue= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/Hoodie/poloBlue.png")      
canvas_Hoodie.create_image(10,10, anchor=NW, image=imgHoodieBlue)

labelHoodieeBlue=Label(canvas_Hoodie,text="Hoodie Blue").place(x = 40,y = 160) 
labelHoodieBluePrice=Label(canvas_Hoodie,text="$200").place(x = 55,y = 185)
#red
imgHoodieRed= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/Hoodie/poloRed.png")      
canvas_Hoodie.create_image(420,10, anchor=NW, image=imgHoodieRed)

labelHoodieRed=Label(canvas_Hoodie,text="Hoodie Red").place(x = 450,y = 160) 
labelHoodieRedPrice=Label(canvas_Hoodie,text="$25").place(x = 465,y = 185)

#grey
imgHoodieGrey= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/Hoodie/poloGrey.png")      
canvas_Hoodie.create_image(830,10, anchor=NW, image=imgHoodieGrey)

labelHoodieGrey=Label(canvas_Hoodie,text="Hoodie Grey").place(x = 860,y = 160) 
labelHoodieGreyPrice=Label(canvas_Hoodie,text="$30").place(x = 875,y = 185)

#green
imgHoodieGreen= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/Hoodie/poloGreen.png")      
canvas_Hoodie.create_image(10,450, anchor=NW, image=imgHoodieGreen)

labelHoodieGreen=Label(canvas_Hoodie,text="Hoodie Green").place(x = 40,y = 600) 
labelHoodieGreenPrice=Label(canvas_Hoodie,text="$25").place(x = 60,y = 625)

#yellow
imgHoodieYellow= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/Hoodie/poloYellow.png")      
canvas_Hoodie.create_image(420,450, anchor=NW, image=imgHoodieYellow)

labelHoodieYellow=Label(canvas_Hoodie,text="Hoodie Yellow").place(x = 450,y = 600) 
labelHoodieYellowPrice=Label(canvas_Hoodie,text="$20").place(x = 465,y = 625)

#white
imgHoodieWhite= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/Hoodie/poloWhite.png")      
canvas_Hoodie.create_image(830,450, anchor=NW, image=imgHoodieWhite)

labelHoodieWhite=Label(canvas_Hoodie,text="Hoodie White").place(x = 860,y = 600) 
labelHoodieWhitePrice=Label(canvas_Hoodie,text="$20").place(x = 875,y = 625)


###################################################################################################################################
######################################################################################################################################
canvas_Coat = Canvas(root,background='orange', width = 1000, height = 700)
canvas_Coat.place(x=1500,y=0)

imgCoatBlue= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/Coat/poloBlue.png")      
canvas_Coat.create_image(10,10, anchor=NW, image=imgCoatBlue)

labelCoatBlue=Label(canvas_Coat,text="Coat Blue").place(x = 40,y = 160) 
labelCoatBluePrice=Label(canvas_Coat,text="$200").place(x = 55,y = 185)
#red
imgCoatRed= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/Coat/poloRed.png")      
canvas_Coat.create_image(420,10, anchor=NW, image=imgCoatRed)

labelCoatBlueRed=Label(canvas_Coat,text="Coat Red").place(x = 450,y = 160) 
labelCoatRedPrice=Label(canvas_Coat,text="$25").place(x = 465,y = 185)

#grey
imgCoatGrey= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/Coat/poloGrey.png")      
canvas_Coat.create_image(830,10, anchor=NW, image=imgCoatGrey)

labelCoatGrey=Label(canvas_Coat,text="Coat Grey").place(x = 860,y = 160) 
labelCoatGreyPrice=Label(canvas_Coat,text="$30").place(x = 875,y = 185)

#green
imgCoatGreen= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/Coat/poloGreen.png")      
canvas_Coat.create_image(10,450, anchor=NW, image=imgCoatGreen)

labelCoatGreen=Label(canvas_Coat,text="Coat Green").place(x = 40,y = 600) 
labelCoatGreenPrice=Label(canvas_Coat,text="$25").place(x = 60,y = 625)

#yellow
imgCoatYellow= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/Coat/poloYellow.png")      
canvas_Coat.create_image(420,450, anchor=NW, image=imgCoatYellow)

labelCoatYellow=Label(canvas_Coat,text="Coat Yellow").place(x = 450,y = 600) 
labelCoatYellowPrice=Label(canvas_Coat,text="$20").place(x = 465,y = 625)

#white
imgCoatWhite= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/Coat/poloWhite.png")      
canvas_Coat.create_image(830,450, anchor=NW, image=imgCoatWhite)

labelCoatWhite=Label(canvas_Coat,text="Coat White").place(x = 860,y = 600) 
labelCoatWhitePrice=Label(canvas_Coat,text="$20").place(x = 875,y = 625)


###################################################################################################################################
######################################################################################################################################
canvas_Jersey = Canvas(root,background='purple', width = 1000, height = 700)
canvas_Jersey.place(x=1500,y=0)

imgJerseyBlue= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/Jersey/poloBlue.png")      
canvas_Jersey.create_image(10,10, anchor=NW, image=imgJerseyBlue)

labelJerseyBlue=Label(canvas_Jersey,text="Jersey Blue").place(x = 40,y = 160) 
labelJerseyBluePrice=Label(canvas_Jersey,text="$200").place(x = 55,y = 185)
#red
imgJerseyRed= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/Jersey/poloRed.png")      
canvas_Jersey.create_image(420,10, anchor=NW, image=imgJerseyRed)

labelJerseyBlueRed=Label(canvas_Jersey,text="Jersey Red").place(x = 450,y = 160) 
labelJerseyRedPrice=Label(canvas_Jersey,text="$25").place(x = 465,y = 185)

#grey
imgJerseyGrey= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/Jersey/poloGrey.png")      
canvas_Jersey.create_image(830,10, anchor=NW, image=imgJerseyGrey)

labelJerseyGrey=Label(canvas_Jersey,text="Jersey Grey").place(x = 860,y = 160) 
labelJerseyGreyPrice=Label(canvas_Jersey,text="$30").place(x = 875,y = 185)

#green
imgJerseyGreen= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/Jersey/poloGreen.png")      
canvas_Jersey.create_image(10,450, anchor=NW, image=imgJerseyGreen)

labelJerseyGreen=Label(canvas_Jersey,text="Jersey Green").place(x = 40,y = 600) 
labelJerseyGreenPrice=Label(canvas_Jersey,text="$25").place(x = 60,y = 625)

#yellow
imgJerseyYellow= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/Jersey/poloYellow.png")      
canvas_Jersey.create_image(420,450, anchor=NW, image=imgJerseyYellow)

labelJerseyYellow=Label(canvas_Jersey,text="Jersey Yellow").place(x = 450,y = 600) 
labelJerseyYellowPrice=Label(canvas_Jersey,text="$20").place(x = 465,y = 625)

#white
imgJerseyWhite= PhotoImage(file="E:/Assignments/python/BY JHONTY g/Fashion/Jersey/poloWhite.png")      
canvas_Jersey.create_image(830,450, anchor=NW, image=imgJerseyWhite)

labelJerseyWhite=Label(canvas_Jersey,text="Jersey White").place(x = 860,y = 600) 
labelJerseyWhitePrice=Label(canvas_Jersey,text="$20").place(x = 875,y = 625)













##############################################################################################################################################################

#New CMD added today####################################################################################################
def b1n():
    canvas_fullsleeve.place(x=150,y=0)
    canvas_polo.place(x=1500,y=0)
    b1n.place(x=1500,y=0)
    b2n.place(x=1200,y=400)
    b2p.place(x=10,y=400)    
def b2n():
    canvas_fullsleeve.place(x=1500,y=0)
    canvas_Hoodie.place(x=150,y=0)
    b3n.place(x=1200,y=400)
    b3p.place(x=10,y=400)
    b2n.place(x=1500,y=0)
    b2p.place(x=1500,y=0)
def b2p():
    canvas_polo.place(x=150,y=0)
    canvas_fullsleeve.place(x=1500,y=0)
    b2n.place(x=1500,y=0)
    b2p.place(x=1500,y=0)
    b1n.place(x=1200,y=400) 
def b3n():
    canvas_Coat.place(x=150,y=0)
    canvas_Hoodie.place(x=1500,y=0)
    b3p.place(x=1500,y=400)
    b3n.place(x=1500,y=400)
    b4n.place(x=1200,y=400)
    b4p.place(x=10,y=400)
def b3p():
    canvas_fullsleeve.place(x=150,y=0)
    canvas_Hoodie.place(x=1500,y=0)
    b3p.place(x=1500,y=0)
    b3n.place(x=1500,y=0)
    b2n.place(x=1200,y=400)
    b2p.place(x=10,y=400)
def b4n():
    canvas_Jersey.place(x=150,y=0)
    canvas_Coat.place(x=1500,y=0)
    b5p.place(x=10,y=400)
    b4n.place(x=1500,y=400)
def b4p():
    canvas_Coat.place(x=1500,y=0)
    canvas_Hoodie.place(x=150,y=0)
    b3p.place(x=10,y=400)
    b3n.place(x=1200,y=400)
    b4p.place(x=1500,y=400)
    b4n.place(x=1500,y=400)
def b5p():
    canvas_Jersey.place(x=1500,y=0)
    canvas_Coat.place(x=150,y=0)
    b4n.place(x=1200,y=400)
    b4p.place(x=10,y=400)   
    b5p.place(x=1500,y=400) 





b1n= Button(root,text="b1n",command=b1n)
b1n.place(x=1200,y=400,width=100,height=50)

b2n=Button(root,text="b2n",command=b2n)
b2n.place(x=1500,y=0,width=100,height=50)


b2p=Button(root,text="b2p",command=b2p)
b2p.place(x=1500,y=0,width=100,height=50)

b3p=Button(root,text="b3p",command=b3p)
b3p.place(x=1500,y=400,width=100,height=50)


b3n=Button(root,text="b3n",command=b3n)
b3n.place(x=1500,y=400,width=100,height=50)

b4n=Button(root,text="b4n",command=b4n)
b4n.place(x=1500,y=400,width=100,height=50)

b4p=Button(root,text="b4p",command=b4p)
b4p.place(x=1500,y=400,width=100,height=50)

b5p=Button(root,text="b5p",command=b5p)
b5p.place(x=1500,y=400,width=100,height=50)





