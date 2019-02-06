from Tkinter import *
import Tkinter
import tkMessageBox
import os
from tkFileDialog  import askopenfilename
import cv2
from PIL import Image
import ImageChops
import numpy as np
import math, operator
#from matplotlib import *
#import matplotlib.pyplot as plt
#import tkmessageBox
    
def compare():
    path = askopenfilename()
    print path
    

    path1 = askopenfilename()
    print path1

    i1 = Image.open(path)
    i2 = Image.open(path1)
    
    
    diff = ImageChops.difference(i1,i2)
    print diff

    result = not np.any(diff)

    if result is True:
     print "The images are same"
     
    else:
     #cv2.imwrite("result.jpg", diff)
     print "The images are different"
     
     

    h = diff.histogram()
#print h
    sq = (value*((index%256)**2) for index, value in enumerate(h))
    sum_of_squares = sum(sq)
    rms = math.sqrt(sum_of_squares/float(i1.size[0] * i1.size[1]))
    #return rms
    print "Difference: " + str(round((rms/100),2)) + '%'
    
    if result is True:
     tkMessageBox.showinfo("Information","The images are same")
     
    
    else:
     tkMessageBox.showinfo("Information","The images are different")
    
     tkMessageBox.showinfo("Difference",str(round((rms/100),2))+ '%')
     
    
root = Tk()
menu = Menu(root)
root.title("Image Comparison")
root.geometry("500x300")
root.configure(background='NavajoWhite3')
#orchid1
#plum2
#wheat2
#thistle2
#NavajoWhite3
#khaki

Label(root, 
		 text="Take two images from folder",
		 fg = "black",
                 bg = "NavajoWhite3",
                
        justify = CENTER,
      padx =10,
		 font = "Helvetica 16 bold italic").pack()


Button(root, 
       text='COMPARE', 
       fg="darkgreen", 
       command=compare).pack(side=LEFT, padx=10)

Button(text='Quit', 
       command=root.quit,
       fg="red").pack(side=LEFT, padx=10)



mainloop()
  
