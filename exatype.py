# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
import tkinter.font as tkfont
import random as rnd
import time as time

fenetre =tk.Tk()
fenetre.geometry('1280x720')
fenetre.minsize(1280,720)
fenetre.title('Exatype')

font = tkfont.Font(family='VCR OSD Mono', size=50)
ptfont = tkfont.Font(family='VCR OSD Mono', size=25)

alpha='abcdefghijklmnopqrstuvwxyz'
zqsd='zqsd'


#MENU
fenetre1=tk.Frame(fenetre,bg='blue')
fenetre1.pack(fill=tk.BOTH,expand=1)

radio=tk.Frame(fenetre1)
radio.pack(anchor=tk.CENTER,side=tk.TOP)
texte=tk.StringVar()
alp=tk.Radiobutton(radio,text='alphabet',font=ptfont,value=alpha,variable=texte).pack(anchor=tk.CENTER,side=tk.LEFT)
zq=tk.Radiobutton(radio,text='zqsd',font=ptfont,value=zqsd,variable=texte).pack(anchor=tk.CENTER,side=tk.LEFT)
texte.set(alpha)

w = tk.Scale(fenetre1, from_=0, to=14, orient=tk.HORIZONTAL)
w.pack(fill=tk.X)
w.set(5)



#JEUX
fenetre2=tk.Frame(fenetre, bg='black')

line=tk.StringVar()
line.set('##########')
good=tk.StringVar()



def rando():
    global a
    global done
    #la=rnd.randint(5,50)
    #rnd.seed(la)
    a=''
    done =''
    lol=texte.get()
    for i in range(w.get()):
        b=rnd.randint(0,len(lol)-1)
        a=a+lol[b]
        done = done + ' '
    
    line.set(a)
    good.set(done)
    
start=0
finish=0
def f(event):
    global a
    global done
    global start,finish
    k=event.keysym
    
    
    if done[-1]==' ':
        start = time.time()

        
    if k == a[0] :
        done=done[1:]+a[0]
        a=a[1:]+' '
        
    if a[0]==' ':
        finish = time.time()
        print(round(finish-start,3))
        gomenu()
        
    line.set(a)
    good.set(done)
        

gauche = tk.Frame(fenetre2,bg='black')
gauche.pack(side=tk.LEFT,fill=tk.BOTH,expand=1)
droite=tk.Frame(fenetre2,bg='black')
droite.pack(side=tk.RIGHT,fill=tk.BOTH,expand=1)

textefinis=tk.Label(gauche,bg='white',textvariable=good,fg='blue',font=font).pack(anchor=tk.CENTER,side=tk.RIGHT)

texe = tk.Label(droite, bg='white',textvariable=line,font=font).pack(anchor=tk.CENTER,side=tk.LEFT)





#BOUTON CHANGEMENT DE FENETRE
def gogame():
    fenetre1.pack_forget()
    fenetre2.pack(fill=tk.BOTH,expand=1)
    fenetre.bind("<Key>",f)
    rando()
    
def gomenu():
    fenetre2.pack_forget()
    fenetre1.pack(fill=tk.BOTH,expand=1)
    
    

boutongame = tk.Button(fenetre1,text='gogame',command=gogame).pack(anchor=tk.CENTER,side=tk.BOTTOM)

fenetre.mainloop()
