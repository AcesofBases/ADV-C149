# -*- coding: utf-8 -*-
"""
Created on Fri May 13 15:51:12 2022

@author: Ace
"""
from tkinter import *
import random

root=Tk()

root.title("Random Word Generator")
root.geometry("500x500")

word_lab=Label(root)

def pick_random():
     alpha_list=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","X","Z"]
     random_no1=random.randint(0,25)
     random_no2=random.randint(0,25)
     random_no3=random.randint(0,25)
     random_no4=random.randint(0,25)
     random_no5=random.randint(0,25)
     random_alpha1= alpha_list[random_no1]
     random_alpha2= alpha_list[random_no2]
     random_alpha3= alpha_list[random_no3]
     random_alpha4= alpha_list[random_no4]
     random_alpha5= alpha_list[random_no5]
     word_lab["text"]=random_alpha1+random_alpha2+random_alpha3+random_alpha4+random_alpha5
btn = Button(root,text="What Is Your Random Word" ,command=pick_random)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
word_lab.place(relx=0.5,rely=0.7,anchor=CENTER)



root.mainloop()