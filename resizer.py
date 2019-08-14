from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter import *
import os,os.path
from PIL import Image
from threading import Thread

size=65
loww=100
highh=2200
acc=3

def setval():
    global size,loww,highh,acc,w1,w2,w3
    size=int(Entry1.get())
    loww=int(w1.get())
    highh=int(w2.get())
    acc=int(w3.get())

def bfile():
    filename = askopenfilename(filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*")))
    basee=os.path.basename(filename)
    resize(imga=filename,base=basee)
    successful()
    
def bfolder():
    image_list=[]
    folder_selected = filedialog.askdirectory(title='Select your pictures folder',initialdir = "/",) 
    files = os.listdir(folder_selected)
    files_img = [i for i in files if i.endswith('.jpg' or 'png' or 'jpeg')]
    for e in files_img:
        name=os.path.basename(e)
        resize('%s//%s' % (folder_selected,e) ,name)
    successful()

def ofolder():
    window.update()
    os.startfile("resized")
    
def successful():
    messagebox.showinfo(" Confirmation Box "," Your Task is Complete ")
    
    
def resize(imga , base):
    class mythread(Thread):
        def run(self):
            global size,loww,highh,acc
            sizes=size
            low=loww
            high=highh

            accuracy=acc*1000
            sizes=sizes*1000
            basewidth=(low+high)//2
            img=Image.open(imga)
            while low<high:
                wpercent = (basewidth/float(img.size[0]))
                hsize = int((float(img.size[1])*float(wpercent)))
                img = img.resize((basewidth,hsize), Image.ANTIALIAS)
                img.save('resized/%s_new.jpg' %base)
                b = os.path.getsize('resized/%s_new.jpg' %base)
                if sizes-accuracy<=b<=sizes+accuracy:
                    break
                elif b < sizes:
                    low = basewidth
                else:
                    high = basewidth - 1
                basewidth=(high+low+1)//2
            
    t1=mythread()
    t1.start()
    
window = Tk()
window.title(" RESIZER by @bhi ")
lbl = Label(window, text=" Easy Image Resize ",  bg="black", fg="red", font=("jokerman", 25))
lbl.grid(column=0, row = 0,  sticky=W+E+N+S,pady=1,columnspan=2)

lbl = Label(window, text=" Enter size in KB ",  bg="black", fg="white", font=("jokerman", 15))
lbl.grid(column=0, row = 4,  sticky=W+E+N+S,padx=4, pady=6)

Entry1 = Entry(window,justify=CENTER,bd=2,font=("jokerman", 15))
Entry1.grid(column=0,row=6,sticky=W+E+N+S,padx=5,pady=3)

btn = Button(window, text="Browse file", font=("jokerman", 15), command=bfile)
btn.grid(column=0, row=1,  sticky=W+E+N+S, padx=4, pady=6)

btn = Button(window, text="Select folder", font=("jokerman", 15), command=bfolder)
btn.grid(column=0, row=2,  sticky=W+E+N+S, padx=4, pady=3)

btn = Button(window, text="Resized Images", font=("jokerman", 15), command=ofolder)
btn.grid(column=0, row=3,  sticky=W+E+N+S, padx=4, pady=3)

lbl = Label(window, text=" Advanced Settings ",  bg="black", fg="white", font=("jokerman", 20))
lbl.grid(column=1, row=1,  sticky=W+E+N+S, padx=4, pady=3)

w1 = Scale(window, from_=0, to=6000, length=400,tickinterval=500,orient=HORIZONTAL,label="LOW")
w1.set(100)
w1.grid(column=1,row=2 , padx=1, pady=1)

w2 = Scale(window, from_=0, to=6000 , orient=HORIZONTAL,length=400,tickinterval=500,label="HIGH",)
w2.set(2200)
w2.grid(column=1,row=3 , padx=1, pady=1)

w3= Scale(window, from_=0, to=50 ,orient=HORIZONTAL,length=400,tickinterval=5,label="PRECISION")
w3.set(3)
w3.grid(column=1,row=4,  padx=1, pady=1)

bt=Button(window, text='Set values',bg="black",fg="blue" ,command=setval,font=("jokerman", 20))
bt.grid(column=0,row=7 ,sticky=W+E+N+S, padx=5, pady=5,columnspan=2)

window.mainloop()