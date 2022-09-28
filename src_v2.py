import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
import control as ct
from IPython.display import display
from tkinter import *



root = Tk()
root.title("Control & Stability")
root.iconbitmap("D:\Python\ico\CS.ico")
root.geometry("400x400")



w001hz = 2*sp.pi*10

# Functions

def remove_text():
    tf_label.config(text="")

def display_poles():
    global tf_label
    m = ct.poles(H)
    print(m)
    tf_label = Label(frame_1_poles,text=m)
    tf_label.grid(row=4,column=0)
    




def clicked_plot_bode():
    fig = plt.subplots()
    ct.bode(H, dB=True)
    plt.show()
    
    
    
    
def clicked_plot_nyquist():
    sampletime = 0.01
    H_sampled = ct.sample_system(H, sampletime, 'tustin')
    fig = plt.subplots()
    ct.nyquist_plot([H_sampled, H])
    plt.show()

def create_tf():
    global H
    
    numerator = num.get()
    numerator_splitted = numerator.split()
    for i in range(len(numerator_splitted)):
        numerator_splitted[i] = int(numerator_splitted[i])
    
   
    denominator = denom.get()
    denominator_splitted = denominator.split()
    for j in range(len(denominator_splitted)):
        denominator_splitted[j] = int(denominator_splitted[j])

    
    y = np.array(numerator_splitted)
    x = np.array(denominator_splitted)
   
    
    H = ct.tf(y,x)
    print(H)
    
    display_poles()
    
    
    num.delete(0, END)
    denom.delete(0, END)
    
    
    
# Create Frame

frame_tf = LabelFrame(root, text="Transfer Function",padx=10,pady=10)
frame_tf.grid(row=0,column=0, rowspan=2,padx=10,pady=(10,0))
    
frame_1_poles = LabelFrame(root,text="Poles",padx=10, pady=10)
frame_1_poles.grid(row=3,column=0,padx=10,pady=(10, 0))

frame_2_plot = LabelFrame(root,text="Plotting",padx=10,pady=10)
frame_2_plot.grid(row=0,column=3)

# Create Text Boxes

global num
global denom

num  = Entry(frame_tf, width = 10)# Numerator
num.grid(row=0,column=1, pady=(10,0))

denom = Entry(frame_tf, width = 10)# Denominator
denom.grid(row=1, column=1, pady=(10,0))



# Create Text Box Labels

num_label = Label(frame_tf, text="Numerator : ")
num_label.grid(row=0, column=0,pady=(10,0))

denum_label = Label(frame_tf, text="Denominator : ")
denum_label.grid(row=1, column=0, pady=(10,0))


# Create a button

my_btn = Button(frame_tf, text="Test!",command=create_tf)
my_btn.grid(row=0, column=2, rowspan=2,padx=10,pady=16,ipady=23)


my_btn_del = Button(frame_1_poles,text="Del",command=remove_text)
my_btn_del.grid(row=0,column=0)

# Creating Radio Buttons

r = IntVar()

Radiobutton(frame_2_plot, text= "Bode Plot", variable=r,value= 1, command=clicked_plot_bode).pack()
Radiobutton(frame_2_plot, text= "Nyquist Plot", variable=r, value= 2, command=clicked_plot_nyquist).pack()


root.mainloop()