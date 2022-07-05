#Start
from tkinter import *
from random import *
import OLL_Algo

#Variables
height = 1000
width = 1200


Shuffle_Moves = []
Moves = []
j = 1
Moves_For_Solve = []
Solved = 0
Count = 0
Move_Letter_Choice = ["U","U'","D","D'","R","R'","L","L'","F","F'","B","B'","M","M'","E","E'","S","S'","Uw","Uw'","Dw","Dw'","Rw","Rw'","Lw","Lw'","Fw","Fw'","Bw","Bw'"]
w = "White"
y = "Yellow"
o = "Orange"
g = "Green"
r = "Red"
b = "Blue"
Solved_Cube = [
    [
        w,w,w,
        w,w,w,
        w,w,w
    ],
    [
        y,y,y,
        y,y,y,
        y,y,y
    ],
	[
        r,r,r,
        r,r,r,
        r,r,r
    ],
	[
        g,g,g,
        g,g,g,
        g,g,g
    ],
	[
        o,o,o,
        o,o,o,
        o,o,o
    ],
    [
        b,b,b,
        b,b,b,
        b,b,b
    ]
    ]

Cube =[
    [
        w,r,w,
        w,w,g,
        b,w,b
    ],
    [
        y,y,y,
        y,y,y,
        y,y,y
    ],
	[
        g,b,r,
        r,r,r,
        r,r,r
    ],
	[
        w,o,w,
        g,g,g,
        g,g,g
    ],
	[
        o,w,g,
        o,o,o,
        o,o,o
    ],
    [
        o,w,r,
        b,b,b,
        b,b,b
    ]
    ]

def White_Side_Of_Cube():
    for j in range(3):
        c.create_rectangle(j*50+300,50,j*50+350,100, fill=Cube[0][j])
    for j in range(3):
        c.create_rectangle(j*50+300,100,j*50+350,150, fill=Cube[0][j+3])
    for j in range(3):
        c.create_rectangle(j*50+300,150,j*50+350,200, fill=Cube[0][j+6])

def Yellow_Side_Of_Cube():
    for j in range(3):
        c.create_rectangle(j*50+300,450,j*50+350,500, fill=Cube[1][j])
    for j in range(3):
        c.create_rectangle(j*50+300,500,j*50+350,550, fill=Cube[1][j+3])
    for j in range(3):
        c.create_rectangle(j*50+300,550,j*50+350,600, fill=Cube[1][j+6])

def Orange_Side_Of_Cube():
    for j in range(3):
        c.create_rectangle(j*50+50,250,j*50+100,300, fill=Cube[2][j])
    for j in range(3):
        c.create_rectangle(j*50+50,300,j*50+100,350, fill=Cube[2][j+3])
    for j in range(3):
        c.create_rectangle(j*50+50,350,j*50+100,400, fill=Cube[2][j+6])

def Green_Side_Of_Cube():
    for j in range(3):
        c.create_rectangle(j*50+300,250,j*50+350,300, fill=Cube[3][j])
    for j in range(3):
        c.create_rectangle(j*50+300,300,j*50+350,350, fill=Cube[3][j+3])
    for j in range(3):
        c.create_rectangle(j*50+300,350,j*50+350,400, fill=Cube[3][j+6])

def Red_Side_Of_Cube():
    for j in range(3):
        c.create_rectangle(j*50+550,250,j*50+600,300, fill=Cube[4][j])
    for j in range(3):
        c.create_rectangle(j*50+550,300,j*50+600,350, fill=Cube[4][j+3])
    for j in range(3):
        c.create_rectangle(j*50+550,350,j*50+600,400, fill=Cube[4][j+6])

def Blue_Side_Of_Cube():
    for j in range(3):
        c.create_rectangle(j*50+800,250,j*50+850,300, fill=Cube[5][j])
    for j in range(3):
        c.create_rectangle(j*50+800,300,j*50+850,350, fill=Cube[5][j+3])
    for j in range(3):
        c.create_rectangle(j*50+800,350,j*50+850,400, fill=Cube[5][j+6])

def Main_Cube():
    White_Side_Of_Cube()
    Yellow_Side_Of_Cube()
    Orange_Side_Of_Cube()
    Green_Side_Of_Cube()
    Red_Side_Of_Cube()
    Blue_Side_Of_Cube()

def Reload():
    c.update()
    c.after(500)

def R(): #Hotovo
    Edit_Left_Up = [
        [Cube[3][2],Cube[3][5],Cube[3][8]],
        [Cube[0][2],Cube[0][5],Cube[0][8]],
        [Cube[5][6],Cube[5][3],Cube[5][0]],
        [Cube[1][2],Cube[1][5],Cube[1][8]],
        [Cube[4][0],Cube[4][1],Cube[4][2],Cube[4][3],Cube[4][5],Cube[4][6],Cube[4][7],Cube[4][8]]
        ]
    Cube[0][2]=Edit_Left_Up[0][0]
    Cube[0][5]=Edit_Left_Up[0][1]
    Cube[0][8]=Edit_Left_Up[0][2]
    Cube[5][6]=Edit_Left_Up[1][0]
    Cube[5][3]=Edit_Left_Up[1][1]
    Cube[5][0]=Edit_Left_Up[1][2]
    Cube[1][2]=Edit_Left_Up[2][0]
    Cube[1][5]=Edit_Left_Up[2][1]
    Cube[1][8]=Edit_Left_Up[2][2]
    Cube[3][2]=Edit_Left_Up[3][0]
    Cube[3][5]=Edit_Left_Up[3][1]
    Cube[3][8]=Edit_Left_Up[3][2]
    Cube[4][0]=Edit_Left_Up[4][5]
    Cube[4][1]=Edit_Left_Up[4][3]
    Cube[4][2]=Edit_Left_Up[4][0]
    Cube[4][5]=Edit_Left_Up[4][1]
    Cube[4][8]=Edit_Left_Up[4][2]
    Cube[4][7]=Edit_Left_Up[4][4]
    Cube[4][6]=Edit_Left_Up[4][7]
    Cube[4][3]=Edit_Left_Up[4][6]
    refresh()

def R_(): #Hotovo
    Edit_Left_Down = [
        [Cube[3][2],Cube[3][5],Cube[3][8]],
        [Cube[0][2],Cube[0][5],Cube[0][8]],
        [Cube[5][6],Cube[5][3],Cube[5][0]],
        [Cube[1][2],Cube[1][5],Cube[1][8]],
        [Cube[4][0],Cube[4][1],Cube[4][2],Cube[4][3],Cube[4][5],Cube[4][6],Cube[4][7],Cube[4][8]]
        ]
    Cube[0][2]=Edit_Left_Down[2][0]
    Cube[0][5]=Edit_Left_Down[2][1]
    Cube[0][8]=Edit_Left_Down[2][2]
    Cube[5][6]=Edit_Left_Down[3][0]
    Cube[5][3]=Edit_Left_Down[3][1]
    Cube[5][0]=Edit_Left_Down[3][2]
    Cube[1][2]=Edit_Left_Down[0][0]
    Cube[1][5]=Edit_Left_Down[0][1]
    Cube[1][8]=Edit_Left_Down[0][2]
    Cube[3][2]=Edit_Left_Down[1][0]
    Cube[3][5]=Edit_Left_Down[1][1]
    Cube[3][8]=Edit_Left_Down[1][2]
    Cube[4][0]=Edit_Left_Down[4][2]
    Cube[4][1]=Edit_Left_Down[4][4]
    Cube[4][2]=Edit_Left_Down[4][7]
    Cube[4][3]=Edit_Left_Down[4][1]
    Cube[4][6]=Edit_Left_Down[4][0]
    Cube[4][7]=Edit_Left_Down[4][3]
    Cube[4][8]=Edit_Left_Down[4][5]
    Cube[4][5]=Edit_Left_Down[4][6]
    refresh()

def L_(): #Hotovo
    Edit_Right_Up = [
        [Cube[3][0],Cube[3][3],Cube[3][6]],
        [Cube[0][0],Cube[0][3],Cube[0][6]],
        [Cube[5][8],Cube[5][5],Cube[5][2]],
        [Cube[1][0],Cube[1][3],Cube[1][6]],
        [Cube[2][0],Cube[2][1],Cube[2][2],Cube[2][3],Cube[2][5],Cube[2][6],Cube[2][7],Cube[2][8]]
        ]
    Cube[0][0]=Edit_Right_Up[0][0]
    Cube[0][3]=Edit_Right_Up[0][1]
    Cube[0][6]=Edit_Right_Up[0][2]
    Cube[5][8]=Edit_Right_Up[1][0]
    Cube[5][5]=Edit_Right_Up[1][1]
    Cube[5][2]=Edit_Right_Up[1][2]
    Cube[1][0]=Edit_Right_Up[2][0]
    Cube[1][3]=Edit_Right_Up[2][1]
    Cube[1][6]=Edit_Right_Up[2][2]
    Cube[3][0]=Edit_Right_Up[3][0]
    Cube[3][3]=Edit_Right_Up[3][1]
    Cube[3][6]=Edit_Right_Up[3][2]
    Cube[2][0]=Edit_Right_Up[4][2]
    Cube[2][1]=Edit_Right_Up[4][4]
    Cube[2][2]=Edit_Right_Up[4][7]
    Cube[2][5]=Edit_Right_Up[4][6]
    Cube[2][8]=Edit_Right_Up[4][5]
    Cube[2][7]=Edit_Right_Up[4][3]
    Cube[2][6]=Edit_Right_Up[4][0]
    Cube[2][3]=Edit_Right_Up[4][1]
    refresh()

def L(): #Hotovo
    Edit_Right_Down = [
        [Cube[3][0],Cube[3][3],Cube[3][6]],
        [Cube[0][0],Cube[0][3],Cube[0][6]],
        [Cube[5][8],Cube[5][5],Cube[5][2]],
        [Cube[1][0],Cube[1][3],Cube[1][6]],
        [Cube[2][0],Cube[2][1],Cube[2][2],Cube[2][3],Cube[2][5],Cube[2][6],Cube[2][7],Cube[2][8]]
        ]
    Cube[0][0]=Edit_Right_Down[2][0]
    Cube[0][3]=Edit_Right_Down[2][1]
    Cube[0][6]=Edit_Right_Down[2][2]
    Cube[5][8]=Edit_Right_Down[3][0]
    Cube[5][5]=Edit_Right_Down[3][1]
    Cube[5][2]=Edit_Right_Down[3][2]
    Cube[1][0]=Edit_Right_Down[0][0]
    Cube[1][3]=Edit_Right_Down[0][1]
    Cube[1][6]=Edit_Right_Down[0][2]
    Cube[3][0]=Edit_Right_Down[1][0]
    Cube[3][3]=Edit_Right_Down[1][1]
    Cube[3][6]=Edit_Right_Down[1][2]
    Cube[2][0]=Edit_Right_Down[4][5]
    Cube[2][1]=Edit_Right_Down[4][3]
    Cube[2][2]=Edit_Right_Down[4][0]
    Cube[2][5]=Edit_Right_Down[4][1]
    Cube[2][8]=Edit_Right_Down[4][2]
    Cube[2][7]=Edit_Right_Down[4][4]
    Cube[2][6]=Edit_Right_Down[4][7]
    Cube[2][3]=Edit_Right_Down[4][6]
    refresh()

def F(): #Hotovo
    Edit_Front_Right = [
        [Cube[3][0],Cube[3][1],Cube[3][2],Cube[3][3],Cube[3][5],Cube[3][6],Cube[3][7],Cube[3][8]],
        [Cube[0][6],Cube[0][7],Cube[0][8]],
        [Cube[4][0],Cube[4][3],Cube[4][6]],
        [Cube[1][0],Cube[1][1],Cube[1][2]],
        [Cube[2][2],Cube[2][5],Cube[2][8]]
        ]
    Cube[0][6]=Edit_Front_Right[4][2]
    Cube[0][7]=Edit_Front_Right[4][1]
    Cube[0][8]=Edit_Front_Right[4][0]
    Cube[4][0]=Edit_Front_Right[1][0]
    Cube[4][3]=Edit_Front_Right[1][1]
    Cube[4][6]=Edit_Front_Right[1][2]
    Cube[1][0]=Edit_Front_Right[2][2]
    Cube[1][1]=Edit_Front_Right[2][1]
    Cube[1][2]=Edit_Front_Right[2][0]
    Cube[2][2]=Edit_Front_Right[3][0]
    Cube[2][5]=Edit_Front_Right[3][1]
    Cube[2][8]=Edit_Front_Right[3][2]
    Cube[3][0]=Edit_Front_Right[0][5]
    Cube[3][1]=Edit_Front_Right[0][3]
    Cube[3][2]=Edit_Front_Right[0][0]
    Cube[3][5]=Edit_Front_Right[0][1]
    Cube[3][8]=Edit_Front_Right[0][2]
    Cube[3][7]=Edit_Front_Right[0][4]
    Cube[3][6]=Edit_Front_Right[0][7]
    Cube[3][3]=Edit_Front_Right[0][6]
    refresh()

def F_(): #Hotovo
    Edit_Front_Left = [
        [Cube[3][0],Cube[3][1],Cube[3][2],Cube[3][3],Cube[3][5],Cube[3][6],Cube[3][7],Cube[3][8]],
        [Cube[0][6],Cube[0][7],Cube[0][8]],
        [Cube[4][0],Cube[4][3],Cube[4][6]],
        [Cube[1][0],Cube[1][1],Cube[1][2]],
        [Cube[2][2],Cube[2][5],Cube[2][8]]
        ]
    Cube[0][6]=Edit_Front_Left[2][0]
    Cube[0][7]=Edit_Front_Left[2][1]
    Cube[0][8]=Edit_Front_Left[2][2]
    Cube[4][0]=Edit_Front_Left[3][2]
    Cube[4][3]=Edit_Front_Left[3][1]
    Cube[4][6]=Edit_Front_Left[3][0]
    Cube[1][0]=Edit_Front_Left[4][0]
    Cube[1][1]=Edit_Front_Left[4][1]
    Cube[1][2]=Edit_Front_Left[4][2]
    Cube[2][2]=Edit_Front_Left[1][2]
    Cube[2][5]=Edit_Front_Left[1][1]
    Cube[2][8]=Edit_Front_Left[1][0]
    Cube[3][0]=Edit_Front_Left[0][2]
    Cube[3][1]=Edit_Front_Left[0][4]
    Cube[3][2]=Edit_Front_Left[0][7]
    Cube[3][3]=Edit_Front_Left[0][1]
    Cube[3][6]=Edit_Front_Left[0][0]
    Cube[3][7]=Edit_Front_Left[0][3]
    Cube[3][8]=Edit_Front_Left[0][5]
    Cube[3][5]=Edit_Front_Left[0][6]
    refresh()

def B_(): #Hotovo
    Edit_Back_Right = [
        [Cube[5][0],Cube[5][1],Cube[5][2],Cube[5][3],Cube[5][5],Cube[5][6],Cube[5][7],Cube[5][8]],
        [Cube[0][0],Cube[0][1],Cube[0][2]],
        [Cube[2][0],Cube[2][3],Cube[2][6]],
        [Cube[1][6],Cube[1][7],Cube[1][8]],
        [Cube[4][2],Cube[4][5],Cube[4][8]]
        ]
    Cube[0][0] = Edit_Back_Right[4][0]
    Cube[0][1] = Edit_Back_Right[4][1]
    Cube[0][2] = Edit_Back_Right[4][2]
    Cube[2][0] = Edit_Back_Right[1][2]
    Cube[2][3] = Edit_Back_Right[1][1]
    Cube[2][6] = Edit_Back_Right[1][0]
    Cube[1][6] = Edit_Back_Right[2][0]
    Cube[1][7] = Edit_Back_Right[2][1]
    Cube[1][8] = Edit_Back_Right[2][2]
    Cube[4][2] = Edit_Back_Right[3][2]
    Cube[4][5] = Edit_Back_Right[3][1]
    Cube[4][8] = Edit_Back_Right[3][0]
    Cube[5][0] = Edit_Back_Right[0][5]
    Cube[5][1] = Edit_Back_Right[0][3]
    Cube[5][2] = Edit_Back_Right[0][0]
    Cube[5][5] = Edit_Back_Right[0][1]
    Cube[5][8] = Edit_Back_Right[0][2]
    Cube[5][7] = Edit_Back_Right[0][4]
    Cube[5][6] = Edit_Back_Right[0][7]
    Cube[5][3] = Edit_Back_Right[0][6]
    refresh()

def B(): #Hotovo
    Edit_Back_Left = [
        [Cube[5][0],Cube[5][1],Cube[5][2],Cube[5][3],Cube[5][5],Cube[5][6],Cube[5][7],Cube[5][8]],
        [Cube[0][0],Cube[0][1],Cube[0][2]],
        [Cube[2][0],Cube[2][3],Cube[2][6]],
        [Cube[1][6],Cube[1][7],Cube[1][8]],
        [Cube[4][2],Cube[4][5],Cube[4][8]]
        ]
    Cube[0][0] = Edit_Back_Left[2][2]
    Cube[0][1] = Edit_Back_Left[2][1]
    Cube[0][2] = Edit_Back_Left[2][0]
    Cube[2][0] = Edit_Back_Left[3][0]
    Cube[2][3] = Edit_Back_Left[3][1]
    Cube[2][6] = Edit_Back_Left[3][2]
    Cube[1][6] = Edit_Back_Left[4][2]
    Cube[1][7] = Edit_Back_Left[4][1]
    Cube[1][8] = Edit_Back_Left[4][0]
    Cube[4][2] = Edit_Back_Left[1][0]
    Cube[4][5] = Edit_Back_Left[1][1]
    Cube[4][8] = Edit_Back_Left[1][2]
    Cube[5][0] = Edit_Back_Left[0][2]
    Cube[5][1] = Edit_Back_Left[0][4]
    Cube[5][2] = Edit_Back_Left[0][7]
    Cube[5][5] = Edit_Back_Left[0][6]
    Cube[5][8] = Edit_Back_Left[0][5]
    Cube[5][7] = Edit_Back_Left[0][3]
    Cube[5][6] = Edit_Back_Left[0][0]
    Cube[5][3] = Edit_Back_Left[0][1]
    refresh()

def U_(): #Hotovo
    Edit_Up_Right = [
        [Cube[0][0],Cube[0][1],Cube[0][2],Cube[0][3],Cube[0][5],Cube[0][6],Cube[0][7],Cube[0][8]],
        [Cube[5][0],Cube[5][1],Cube[5][2]],
        [Cube[2][0],Cube[2][1],Cube[2][2]],
        [Cube[3][0],Cube[3][1],Cube[3][2]],
        [Cube[4][0],Cube[4][1],Cube[4][2]]
        ]
    Cube[3][0] = Edit_Up_Right[2][0]
    Cube[3][1] = Edit_Up_Right[2][1]
    Cube[3][2] = Edit_Up_Right[2][2]
    Cube[4][0] = Edit_Up_Right[3][0]
    Cube[4][1] = Edit_Up_Right[3][1]
    Cube[4][2] = Edit_Up_Right[3][2]
    Cube[5][0] = Edit_Up_Right[4][0]
    Cube[5][1] = Edit_Up_Right[4][1]
    Cube[5][2] = Edit_Up_Right[4][2]
    Cube[2][0] = Edit_Up_Right[1][0]
    Cube[2][1] = Edit_Up_Right[1][1]
    Cube[2][2] = Edit_Up_Right[1][2]
    Cube[0][0] = Edit_Up_Right[0][2]
    Cube[0][1] = Edit_Up_Right[0][4]
    Cube[0][2] = Edit_Up_Right[0][7]
    Cube[0][5] = Edit_Up_Right[0][6]
    Cube[0][8] = Edit_Up_Right[0][5]
    Cube[0][7] = Edit_Up_Right[0][3]
    Cube[0][6] = Edit_Up_Right[0][0]
    Cube[0][3] = Edit_Up_Right[0][1]
    refresh()

def U(): #Hotovo
    Edit_Up_Left = [
        [Cube[0][0],Cube[0][1],Cube[0][2],Cube[0][3],Cube[0][5],Cube[0][6],Cube[0][7],Cube[0][8]],
        [Cube[5][0],Cube[5][1],Cube[5][2]],
        [Cube[2][0],Cube[2][1],Cube[2][2]],
        [Cube[3][0],Cube[3][1],Cube[3][2]],
        [Cube[4][0],Cube[4][1],Cube[4][2]]
        ]
    Cube[3][0] = Edit_Up_Left[4][0]
    Cube[3][1] = Edit_Up_Left[4][1]
    Cube[3][2] = Edit_Up_Left[4][2]
    Cube[4][0] = Edit_Up_Left[1][0]
    Cube[4][1] = Edit_Up_Left[1][1]
    Cube[4][2] = Edit_Up_Left[1][2]
    Cube[5][0] = Edit_Up_Left[2][0]
    Cube[5][1] = Edit_Up_Left[2][1]
    Cube[5][2] = Edit_Up_Left[2][2]
    Cube[2][0] = Edit_Up_Left[3][0]
    Cube[2][1] = Edit_Up_Left[3][1]
    Cube[2][2] = Edit_Up_Left[3][2]
    Cube[0][0] = Edit_Up_Left[0][5]
    Cube[0][1] = Edit_Up_Left[0][3]
    Cube[0][2] = Edit_Up_Left[0][0]
    Cube[0][5] = Edit_Up_Left[0][1]
    Cube[0][8] = Edit_Up_Left[0][2]
    Cube[0][7] = Edit_Up_Left[0][4]
    Cube[0][6] = Edit_Up_Left[0][7]
    Cube[0][3] = Edit_Up_Left[0][6]
    refresh()

def D(): #Hotovo
    Edit_Down_Right = [
        [Cube[1][0],Cube[1][1],Cube[1][2],Cube[1][3],Cube[1][5],Cube[1][6],Cube[1][7],Cube[1][8]],
        [Cube[5][6],Cube[5][7],Cube[5][8]],
        [Cube[2][6],Cube[2][7],Cube[2][8]],
        [Cube[3][6],Cube[3][7],Cube[3][8]],
        [Cube[4][6],Cube[4][7],Cube[4][8]]
        ]
    Cube[3][6] = Edit_Down_Right[2][0]
    Cube[3][7] = Edit_Down_Right[2][1]
    Cube[3][8] = Edit_Down_Right[2][2]
    Cube[4][6] = Edit_Down_Right[3][0]
    Cube[4][7] = Edit_Down_Right[3][1]
    Cube[4][8] = Edit_Down_Right[3][2]
    Cube[5][6] = Edit_Down_Right[4][0]
    Cube[5][7] = Edit_Down_Right[4][1]
    Cube[5][8] = Edit_Down_Right[4][2]
    Cube[2][6] = Edit_Down_Right[1][0]
    Cube[2][7] = Edit_Down_Right[1][1]
    Cube[2][8] = Edit_Down_Right[1][2]
    Cube[1][0] = Edit_Down_Right[0][5]
    Cube[1][1] = Edit_Down_Right[0][3]
    Cube[1][2] = Edit_Down_Right[0][0]
    Cube[1][5] = Edit_Down_Right[0][1]
    Cube[1][8] = Edit_Down_Right[0][2]
    Cube[1][7] = Edit_Down_Right[0][4]
    Cube[1][6] = Edit_Down_Right[0][7]
    Cube[1][3] = Edit_Down_Right[0][6]
    refresh()

def D_(): #Hotovo
    Edit_Down_Left = [
        [Cube[1][0],Cube[1][1],Cube[1][2],Cube[1][3],Cube[1][5],Cube[1][6],Cube[1][7],Cube[1][8]],
        [Cube[5][6],Cube[5][7],Cube[5][8]],
        [Cube[2][6],Cube[2][7],Cube[2][8]],
        [Cube[3][6],Cube[3][7],Cube[3][8]],
        [Cube[4][6],Cube[4][7],Cube[4][8]]
        ]
    Cube[3][6] = Edit_Down_Left[4][0]
    Cube[3][7] = Edit_Down_Left[4][1]
    Cube[3][8] = Edit_Down_Left[4][2]
    Cube[4][6] = Edit_Down_Left[1][0]
    Cube[4][7] = Edit_Down_Left[1][1]
    Cube[4][8] = Edit_Down_Left[1][2]
    Cube[5][6] = Edit_Down_Left[2][0]
    Cube[5][7] = Edit_Down_Left[2][1]
    Cube[5][8] = Edit_Down_Left[2][2]
    Cube[2][6] = Edit_Down_Left[3][0]
    Cube[2][7] = Edit_Down_Left[3][1]
    Cube[2][8] = Edit_Down_Left[3][2]
    Cube[1][0] = Edit_Down_Left[0][2]
    Cube[1][1] = Edit_Down_Left[0][4]
    Cube[1][2] = Edit_Down_Left[0][7]
    Cube[1][5] = Edit_Down_Left[0][6]
    Cube[1][8] = Edit_Down_Left[0][5]
    Cube[1][7] = Edit_Down_Left[0][3]
    Cube[1][6] = Edit_Down_Left[0][0]
    Cube[1][3] = Edit_Down_Left[0][1]
    refresh()

def E_(): #Hotovo
    Edit_Mid_S_H_Right = [
        [Cube[2][3],Cube[2][4],Cube[2][5]],
        [Cube[3][3],Cube[3][4],Cube[3][5]],
        [Cube[4][3],Cube[4][4],Cube[4][5]],
        [Cube[5][3],Cube[5][4],Cube[5][5]]
        ]
    Cube[2][3] = Edit_Mid_S_H_Right[3][0]
    Cube[2][4] = Edit_Mid_S_H_Right[3][1]
    Cube[2][5] = Edit_Mid_S_H_Right[3][2]
    Cube[3][3] = Edit_Mid_S_H_Right[0][0]
    Cube[3][4] = Edit_Mid_S_H_Right[0][1]
    Cube[3][5] = Edit_Mid_S_H_Right[0][2]
    Cube[4][3] = Edit_Mid_S_H_Right[1][0]
    Cube[4][4] = Edit_Mid_S_H_Right[1][1]
    Cube[4][5] = Edit_Mid_S_H_Right[1][2]
    Cube[5][3] = Edit_Mid_S_H_Right[2][0]
    Cube[5][4] = Edit_Mid_S_H_Right[2][1]
    Cube[5][5] = Edit_Mid_S_H_Right[2][2]
    refresh()

def E__(): #Hotovo
    Edit_Mid_S_H_Left = [
        [Cube[2][3],Cube[2][4],Cube[2][5]],
        [Cube[3][3],Cube[3][4],Cube[3][5]],
        [Cube[4][3],Cube[4][4],Cube[4][5]],
        [Cube[5][3],Cube[5][4],Cube[5][5]]
        ]
    Cube[4][3] = Edit_Mid_S_H_Left[3][0]
    Cube[4][4] = Edit_Mid_S_H_Left[3][1]
    Cube[4][5] = Edit_Mid_S_H_Left[3][2]
    Cube[5][3] = Edit_Mid_S_H_Left[0][0]
    Cube[5][4] = Edit_Mid_S_H_Left[0][1]
    Cube[5][5] = Edit_Mid_S_H_Left[0][2]
    Cube[2][3] = Edit_Mid_S_H_Left[1][0]
    Cube[2][4] = Edit_Mid_S_H_Left[1][1]
    Cube[2][5] = Edit_Mid_S_H_Left[1][2]
    Cube[3][3] = Edit_Mid_S_H_Left[2][0]
    Cube[3][4] = Edit_Mid_S_H_Left[2][1]
    Cube[3][5] = Edit_Mid_S_H_Left[2][2]
    refresh()

def M_(): #Hotovo
    Edit_Mid_V_Up = [
        [Cube[0][1],Cube[0][4],Cube[0][7]],
        [Cube[1][1],Cube[1][4],Cube[1][7]],
        [Cube[3][1],Cube[3][4],Cube[3][7]],
        [Cube[5][1],Cube[5][4],Cube[5][7]]
        ]
    Cube[0][1] = Edit_Mid_V_Up[2][0]
    Cube[0][4] = Edit_Mid_V_Up[2][1]
    Cube[0][7] = Edit_Mid_V_Up[2][2]
    Cube[5][1] = Edit_Mid_V_Up[0][2]
    Cube[5][4] = Edit_Mid_V_Up[0][1]
    Cube[5][7] = Edit_Mid_V_Up[0][0]
    Cube[1][1] = Edit_Mid_V_Up[3][2]
    Cube[1][4] = Edit_Mid_V_Up[3][1]
    Cube[1][7] = Edit_Mid_V_Up[3][0]
    Cube[3][1] = Edit_Mid_V_Up[1][0]
    Cube[3][4] = Edit_Mid_V_Up[1][1]
    Cube[3][7] = Edit_Mid_V_Up[1][2]
    refresh()

def M(): #Hotovo
    Edit_Mid_V_Down = [
        [Cube[0][1],Cube[0][4],Cube[0][7]],
        [Cube[1][1],Cube[1][4],Cube[1][7]],
        [Cube[3][1],Cube[3][4],Cube[3][7]],
        [Cube[5][1],Cube[5][4],Cube[5][7]]
        ]
    Cube[0][1] = Edit_Mid_V_Down[3][2]
    Cube[0][4] = Edit_Mid_V_Down[3][1]
    Cube[0][7] = Edit_Mid_V_Down[3][0]
    Cube[5][1] = Edit_Mid_V_Down[1][2]
    Cube[5][4] = Edit_Mid_V_Down[1][1]
    Cube[5][7] = Edit_Mid_V_Down[1][0]
    Cube[1][1] = Edit_Mid_V_Down[2][0]
    Cube[1][4] = Edit_Mid_V_Down[2][1]
    Cube[1][7] = Edit_Mid_V_Down[2][2]
    Cube[3][1] = Edit_Mid_V_Down[0][0]
    Cube[3][4] = Edit_Mid_V_Down[0][1]
    Cube[3][7] = Edit_Mid_V_Down[0][2]
    refresh()

def S_(): #Hotovo
    Edit_Mid_Up_Right = [
        [Cube[0][3],Cube[0][4],Cube[0][5]],
        [Cube[4][1],Cube[4][4],Cube[4][7]],
        [Cube[1][3],Cube[1][4],Cube[1][5]],
        [Cube[2][1],Cube[2][4],Cube[2][7]]
        ]
    Cube[0][3] = Edit_Mid_Up_Right[3][2]
    Cube[0][4] = Edit_Mid_Up_Right[3][1]
    Cube[0][5] = Edit_Mid_Up_Right[3][0]
    Cube[4][1] = Edit_Mid_Up_Right[0][0]
    Cube[4][4] = Edit_Mid_Up_Right[0][1]
    Cube[4][7] = Edit_Mid_Up_Right[0][2]
    Cube[1][3] = Edit_Mid_Up_Right[1][2]
    Cube[1][4] = Edit_Mid_Up_Right[1][1]
    Cube[1][5] = Edit_Mid_Up_Right[1][0]
    Cube[2][1] = Edit_Mid_Up_Right[2][0]
    Cube[2][4] = Edit_Mid_Up_Right[2][1]
    Cube[2][7] = Edit_Mid_Up_Right[2][2]
    refresh()

def S__(): #Hotovo
    Edit_Mid_Up_Left = [
        [Cube[0][3],Cube[0][4],Cube[0][5]],
        [Cube[4][1],Cube[4][4],Cube[4][7]],
        [Cube[1][3],Cube[1][4],Cube[1][5]],
        [Cube[2][1],Cube[2][4],Cube[2][7]]
        ]
    Cube[0][3] = Edit_Mid_Up_Left[1][0]
    Cube[0][4] = Edit_Mid_Up_Left[1][1]
    Cube[0][5] = Edit_Mid_Up_Left[1][2]
    Cube[4][1] = Edit_Mid_Up_Left[2][2]
    Cube[4][4] = Edit_Mid_Up_Left[2][1]
    Cube[4][7] = Edit_Mid_Up_Left[2][0]
    Cube[1][3] = Edit_Mid_Up_Left[3][0]
    Cube[1][4] = Edit_Mid_Up_Left[3][1]
    Cube[1][5] = Edit_Mid_Up_Left[3][2]
    Cube[2][1] = Edit_Mid_Up_Left[0][2]
    Cube[2][4] = Edit_Mid_Up_Left[0][1]
    Cube[2][7] = Edit_Mid_Up_Left[0][0]
    refresh()

def Try_To_Solve_It(j, Moves_For_Solve, Solved, Solved_Cube, Cube, Count):
    while(Solved != 1 and Count != 100):
        if(Solved_Cube != Cube):
            Move_Solve = choice(Move_Letter_Choice)
            if(Move_Solve == "L'"):
                L_()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "L"):
                L()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "R"):
                R()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "R'"):
                R_()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "F"):
                F()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "F'"):
                F_()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "B'"):
                B_()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "B"):
                B()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "U'"):
                U_()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "U"):
                U()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "D"):
                D()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "D'"):
                D_()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "E"):
                E_()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "E'"):
                E__()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "M'"):
                M_()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "M"):
                M()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "S"):
                S_()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "S'"):
                S__()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "Uw"): #Hotovo
                U()
                E__()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "Uw'"): #Hotovo
                U_()
                E_()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "Dw"): #Hotovo
                D()
                E_()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "Dw'"): #Hotovo
                D_()
                E__()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "Rw"): #Hotovo
                R()
                M_()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "Rw'"): #Hotovo
                R_()
                M()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "Lw"): #Hotovo
                L()
                M()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "Lw'"): #Hotovo
                L_()
                M_()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "Fw"): #Hotovo
                F()
                S_()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "Fw'"): #Hotovo
                F_()
                S__()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "Bw"): #Hotovo
                B()
                S__()
                Moves_For_Solve.append(Move_Solve)
            elif(Move_Solve == "Bw'"): #Hotovo
                B_()
                S_()
                Moves_For_Solve.append(Move_Solve)
        else:
            Solved = 1
            break
        Count += 1
    if(Solved == 1 and Count <= 100):
        print("Podarilo sa")
        with open('readme.txt', 'a') as f:
            f.writelines("Shuffle")
            f.write('\n')
            f.writelines("---------")
            f.write('\n')
            f.writelines(Shuffle_Moves)
            f.write('\n')
            f.writelines("Solve")
            f.write('\n')
            f.writelines("---------")
            f.write('\n')
            for i in Moves_For_Solve:
                if(j == len(Moves_For_Solve)):
                    f.writelines(i)
                else:
                    f.writelines(i+" - ")
                j += 1
            f.write('\n')
    else:
        Count = 0
        j = 0
        Moves_For_Solve = []
        print("Nepodarilo sa")
        c.after(2000, Reset_Cube())

def Sexy_Move():
    R()
    Reload()
    U()
    Reload()
    R_()
    Reload()
    U_()
    Reload()

def OLL():
    R_()
    Reload()
    F()
    Reload()
    R_()
    Reload()
    for i in range(2):
        B()
        Reload()
    R()
    Reload()
    F_()
    Reload()
    R_()
    Reload()
    for i in range(2):
        B()
        Reload()
    for i in range(2):
        R_()
        Reload()
    Check_PLL()

def Check_PLL():
    i = 0
    Position = 0
    for i in range(2,6):
        if(Cube[i][0] == "Orange" and Cube[i][1] == Cube[i][0] and Cube[i][2]  == Cube[i][0]):
            Position = i
            break
        elif(Cube[i][0] == "Green"  and Cube[i][1] == Cube[i][0] and Cube[i][2]  == Cube[i][0]):
            Position = i
            break
        elif(Cube[i][0] == "Red"  and Cube[i][1] == Cube[i][0] and Cube[i][2]  == Cube[i][0]):
            Position = i
            break
        elif(Cube[i][0] == "Blue"  and Cube[i][1] == Cube[i][0] and Cube[i][2]  == Cube[i][0]):
            Position = i
            break
    if(Position == 2):
        U()
        Reload()
    elif(Position == 3):
        for i in range(2):
            U_()
            Reload()
    elif(Position == 4):
        U_()
        Reload()
    if(Cube[3][0] == Cube[3][2] and Cube[3][1] == Cube[2][4] and Cube[4][0] == Cube[4][2] and Cube[4][1] == Cube[3][4]):
        PLL_Left()
    elif(Cube[2][0] == Cube[2][2] and Cube[2][1] == Cube[3][4] and Cube[3][0] == Cube[3][2] and Cube[3][1] == Cube[4][4]):
        PLL_Right()
    elif(Cube[3][1] == Cube[5][4] and Cube[2][1] == Cube[4][4]):
        PLL_Mid_OP()
    else:
        while(Cube[3][1] != Cube[2][0] and Cube[2][1] != Cube[3][0]):
            U_()
        PLL_Mid_NX()
    Check_Cube()

def Check_Cube():
    for _ in range(4):
        if(Solved_Cube == Cube):
            return True
        U_()

    return False
        
    
def White_side():
    while(Cube[0] != ["White","White","White","White","White","White","White","White","White"]):
        while(Cube[0][6] != "White"):
            L()
            Reload()
            D_()
            Reload()
            L_()
            Reload()
            D()
            Reload()
        U()
    Check_OLL()

def Check_OLL():
    i = 0
    Position = 0
    for i in range(2,6):
        if(Cube[i][0] == "Orange" and Cube[i][1] == Cube[i][0] and Cube[i][2]  == Cube[i][0] or Cube[i][0] == "Orange" and Cube[i][2] == Cube[i][0]):
            Position = i
            break
        elif(Cube[i][0] == "Green"  and Cube[i][1] == Cube[i][0] and Cube[i][2]  == Cube[i][0] or Cube[i][0] == "Green" and Cube[i][2] == Cube[i][0]):
            Position = i
            break
        elif(Cube[i][0] == "Red"  and Cube[i][1] == Cube[i][0] and Cube[i][2]  == Cube[i][0] or Cube[i][0] == "Red" and Cube[i][2] == Cube[i][0]):
            Position = i
            break
        elif(Cube[i][0] == "Blue"  and Cube[i][1] == Cube[i][0] and Cube[i][2]  == Cube[i][0] or Cube[i][0] == "Blue" and Cube[i][2] == Cube[i][0]):
            Position = i
            break
    if(Position == 2):
        U()
        Reload()
    elif(Position == 3):
        for i in range(2):
            U_()
            Reload()
    elif(Position == 4):
        U_()
        Reload()
    OLL()
                
def PLL_Right():
    R()
    Reload()
    U_()
    Reload()
    R()
    Reload()
    U()
    Reload()
    R()
    Reload()
    U()
    Reload()
    R()
    Reload()
    U_()
    Reload()
    R_()
    Reload()
    U_()
    Reload()
    for i in range(2):
        R_()
        c.update()
        c.after(500)

def PLL_Left():
    L_()
    Reload()
    U()
    Reload()
    L_()
    Reload()
    U_()
    Reload()
    L_()
    Reload()
    U_()
    Reload()
    L_()
    Reload()
    U()
    Reload()
    L()
    Reload()
    U()
    Reload()
    for i in range(2):
        L()
        c.update()
        c.after(500)
#zapisat do stringu a potom funkciou robit
def PLL_Mid_OP():
    for i in range(2):
        M()
        c.update()
        c.after(500)
    U_()
    Reload()
    for i in range(2):
        M()
        c.update()
        c.after(500)
    for i in range(2):
        U()
        c.update()
        c.after(500)
    for i in range(2):
        M()
        c.update()
        c.after(500)
    U_()
    Reload()
    for i in range(2):
        M()
        c.update()
        c.after(500)

def PLL_Mid_NX():
    U_()
    Reload()
    M_()
    Reload()
    U_()
    Reload()
    for i in range(2):
        M()
        c.update()
        c.after(500)
    U_()
    Reload()
    for i in range(2):
        M()
        c.update()
        c.after(500)
    U_()
    Reload()
    M_()
    Reload()
    for i in range(2):
        U_()
        c.update()
        c.after(500)
    for i in range(2):
        M()
        c.update()
        c.after(500)

def White_Cross():
    while([Cube[0][1], Cube[0][3], Cube[0][4], Cube[0][5], Cube[0][7]] != ["White","White","White","White","White"]):
        if([Cube[0][1], Cube[0][4], Cube[0][7]] == ["White","White","White"]):
            U_()
            c.update()
            c.after(500)
        elif([Cube[0][3], Cube[0][4], Cube[0][5]] == ["White","White","White"]):
            F()
            c.update()
            c.after(500)
            Sexy_Move()
            c.update()
            c.after(500)
            F_()
            c.update()
            c.after(500)
        elif([Cube[0][7], Cube[0][4], Cube[0][5]] == ["White","White","White"]):
            F()
            c.update()
            c.after(500)
            S_()
            c.update()
            c.after(500)
            Sexy_Move()
            c.update()
            c.after(500)
            S__()
            c.update()
            c.after(500)
            F_()
            c.update()
            c.after(500)
        elif([Cube[0][1], Cube[0][4], Cube[0][5]] == ["White","White","White"]):
            U()
            c.update()
            c.after(500)
        elif([Cube[0][1], Cube[0][4], Cube[0][3]] == ["White","White","White"]):
            for i in range(2):
                U_()
                c.update()
                c.after(500)
        elif([Cube[0][7], Cube[0][4], Cube[0][3]] == ["White","White","White"]):
            U_()
            c.update()
            c.after(500)
        elif(Cube[0][4] == "White"):
            F()
            c.update()
            c.after(500)
            Sexy_Move()
            c.update()
            c.after(500)
            F_()
            c.update()
            c.after(500)
    White_side()

def refresh():
    c.delete("All")
    Main_Cube()

def shuffle_cube():
    Shuffle_Moves = []
    for i in range(randrange(20,40)):
        Shuffle_Moves.append(choice(Move_Letter_Choice))
    shuffle(Shuffle_Moves)
    for i in range(len(Shuffle_Moves)):
        if(Shuffle_Moves[i] == "L'"):
            L_() 
        elif(Shuffle_Moves[i] == "L"):
            L()
        elif(Shuffle_Moves[i] == "R"):
            R()
        elif(Shuffle_Moves[i] == "R'"):
            R_()
        elif(Shuffle_Moves[i] == "F"):
            F()
        elif(Shuffle_Moves[i] == "F'"):
            F_()
        elif(Shuffle_Moves[i] == "B'"):
            B_()
        elif(Shuffle_Moves[i] == "B"):
            B()
        elif(Shuffle_Moves[i] == "U'"):
            U_()
        elif(Shuffle_Moves[i] == "U"):
            U()
        elif(Shuffle_Moves[i] == "D"):
            D()
        elif(Shuffle_Moves[i] == "D'"):
            D_()
    print(Shuffle_Moves)
    refresh()

def Reset_Cube():
    global Cube
    Cube = [
    [
        w,w,w,
        w,w,w,
        w,w,w
    ],
	[
        y,y,y,
        y,y,y,
        y,y,y
    ],
	[
        o,o,o,
        o,o,o,
        o,o,o
    ],
	[
        g,g,g,
        g,g,g,
        g,g,g
    ],
	[
        r,r,r,
        r,r,r,
        r,r,r
    ],
    [
        b,b,b,
        b,b,b,
        b,b,b
    ]
    ]
    refresh()
"""
def solve_back():
    for i in reversed(Moves):
"""

def Key_Check(event):
    if(event.char == "L'"): #Hotovo
        L_() 
    elif(event.char == "L"): #Hotovo
        L()
    elif(event.char == "R"): #Hotovo
        R()
    elif(event.char == "R'"): #Hotovo
        R_()
    elif(event.char == "F"): #Hotovo
        F()
    elif(event.char == "F'"): #Hotovo
        F_()
    elif(event.char == "B'"): #Hotovo
        B_()
    elif(event.char == "B"): #Hotovo
        B()
    elif(event.char == "U'"): #Hotovo
        U_()
    elif(event.char == "U"): #Hotovo
        U()
    elif(event.char == "D"): #Hotovo
        D()
    elif(event.char == "D'"): #Hotovo
        D_()
    elif(event.char == "E"): #Hotovo
        E_()
    elif(event.char == "E'"): #Hotovo
        E__()
    elif(event.char == "M'"): #Hotovo
        M_()
    elif(event.char == "M"): #Hotovo
        M()
    elif(event.char == "S"): #Hotovo
        S_()
    elif(event.char == "S'"): #Hotovo
        S__()
    elif(event.char == "Uw"): #Hotovo
        U()
        E__()
    elif(event.char == "Uw'"): #Hotovo
        U_()
        E_()
    elif(event.char == "Dw"): #Hotovo
        D()
        E_()
    elif(event.char == "Dw'"): #Hotovo
        D_()
        E__()
    elif(event.char == "Rw"): #Hotovo
        R()
        M_()
    elif(event.char == "Rw'"): #Hotovo
        R_()
        M()
    elif(event.char == "Lw"): #Hotovo
        L()
        M()
    elif(event.char == "Lw'"): #Hotovo
        L_()
        M_()
    elif(event.char == "Fw"): #Hotovo
        F()
        S_()
    elif(event.char == "Fw'"): #Hotovo
        F_()
        S__()
    elif(event.char == "Bw"): #Hotovo
        B()
        S__()
    elif(event.char == "Bw'"): #Hotovo
        B_()
        S_()
    elif(event.char == "o"):
        skuska_OLL()
    elif(event.char == "p"):
        skuska_PLL()
    elif(event.char == "s"):
        Check_PLL()
    elif(event.char == "a"):
        OLL()
    elif(event.char == "i"):
        White_Cross()
    elif(event.char == "t"):
        Try_To_Solve_It(j, Moves_For_Solve, Solved, Solved_Cube, Cube, Count)

def skuska_OLL():
    Counter = 0
    while(True):
        if([Cube[0][1], Cube[0][3], Cube[0][4], Cube[0][5], Cube[0][7]] == [w,w,w,w,w]):
            while(True):
                if([Cube[0][0],Cube[0][1],Cube[0][2],Cube[0][3],Cube[0][4],Cube[0][5],Cube[0][6],Cube[0][7],Cube[0][8]] == [w,w,w,w,w,w,w,w,w]):
                    break
                elif(Cube[0][6] == w):
                    U()
                    Reload()
                else:
                    L()
                    Reload()
                    D_()
                    Reload()
                    L_()
                    Reload()
                    D()
                    Reload()
            break
        elif([Cube[0][3], Cube[0][4], Cube[0][5]] == [w,w,w]):
            Counter = 5
            F()
            Reload()
            Sexy_Move()
            F_()
            Reload()
            pass
        elif([Cube[0][4], Cube[0][5], Cube[0][7]] == [w,w,w]):
            Counter = 5
            F()
            Reload()
            Sexy_Move()
            F_()
            Reload()
            pass
        elif(Counter == 4):
            F()
            Reload()
            Sexy_Move()
            F_()
            Reload()
            pass
        else:
            U()
            Reload()
            Counter += 1
        """
        if([Cube[0][4], Cube[2][0], Cube[2][1], Cube[2][2], Cube[3][1], Cube[4][0], Cube[4][1], Cube[4][2], Cube[5][1]] == [w,w,w,w,w,w,w,w,w]):
            OLL_1()
            break
        elif([Cube[0][4], Cube[2][1], Cube[2][2], Cube[3][1], Cube[4][0], Cube[4][1], Cube[5][0], Cube[5][1], Cube[5][2]] == [w,w,w,w,w,w,w,w,w]):
            OLL_2()
            break
        else:
            U()
            Reload()
        """

def skuska_PLL():
    Found = 0
    while(Found == 0):
        if(Check_Cube()):
            print("Postavil si kocku ty kokot")
            Found = 1
            break
        else:
            for _ in range(4):
                if((([Cube[5][0],Cube[5][1],Cube[5][2]] == [r,r,r]) or ([Cube[5][0],Cube[5][1],Cube[5][2]] == [o,o,o]) or ([Cube[5][0],Cube[5][1],Cube[5][2]] == [g,g,g]) 
                or ([Cube[5][0],Cube[5][1],Cube[5][2]] == [b,b,b])) and ((Cube[2][0] == Cube[2][2]) and (Cube[3][0] == Cube[3][2]) and (Cube[4][0] == Cube[4][2])) and (((Cube[2][1] == Cube[3][4]) 
                and (Cube[3][1] == Cube[4][4]) and (Cube[4][1] == Cube[2][4])) or ((Cube[2][1] == Cube[4][4]) and (Cube[3][1] == Cube[2][4]) and (Cube[4][1] == Cube[3][4])))):
                    Found = 1
                    R()
                    Reload()
                    U_()
                    Reload()
                    R()
                    Reload()
                    U()
                    Reload()
                    R()
                    Reload()
                    U()
                    Reload()
                    R()
                    Reload()
                    U_()
                    Reload()
                    R_()
                    Reload()
                    U_()
                    Reload()
                    R()
                    Reload()
                    R()
                    Reload()
                    break
                else:
                    U_()
                    Reload()
                break
            elif(((Cube[2][0] == Cube[2][2]) and (Cube[3][0] == Cube[3][2]) and (Cube[4][0] == Cube[4][2]) and (Cube[5][0] == Cube[5][2]))):
                Found = 1
                R()
                Reload()
                U_()
                Reload()
                R()
                Reload()
                U()
                Reload()
                R()
                Reload()
                U()
                Reload()
                R()
                Reload()
                U_()
                Reload()
                R_()
                Reload()
                U_()
                Reload()
                R()
                Reload()
                R()
                Reload()
                break
            elif(Cube[5][0] == Cube[5][2]):
                Found = 1
                R_()
                Reload()
                F()
                Reload()
                R_()
                Reload()
                B()
                Reload()
                B()
                Reload()
                R()
                Reload()
                F_()
                Reload()
                R_()
                Reload()
                B()
                Reload()
                B()
                Reload()
                R()
                Reload()
                R()
                Reload()
                break
            else:
                U_()
                Reload()
            if(Found != 1):    
                R_()
                Reload()
                F()
                Reload()
                R_()
                Reload()
                B()
                Reload()
                B()
                Reload()
                R()
                Reload()
                F_()
                Reload()
                R_()
                Reload()
                B()
                Reload()
                B()
                Reload()
                R()
                Reload()
                R()
                Reload()
                

def OLL_1():
    R()
    Reload()
    U()
    Reload()
    U()
    Reload()
    R()
    Reload()
    R()
    Reload()
    F()
    Reload()
    R()
    Reload()
    F_()
    Reload()
    U()
    Reload()
    U()
    Reload()
    R_()
    Reload()
    F()
    Reload()
    R()
    Reload()
    F_()
    Reload()

def OLL_2():
    R()
    M_()
    Reload()
    U()
    Reload()
    R_()
    M()
    Reload()



#Canvas
root = Tk()
root.title('text')
c = Canvas(master=root, height = height, width = width)
c.pack()
Main_Cube()

root.bind('<Key>', Key_Check)
#End
root.mainloop()
