# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 11:38:44 2021

@author: chnt2
"""

from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry('400x200')
u1 = Label(text="Enter the user name")
u1.pack()
ue1 = Entry(top, bd =3)
ue1.pack()
L1 = Label(text="Enter the password")
L1.pack()
E1 = Entry(top, bd =3)
E1.pack()


import pandas as pd    
     
data = pd.read_csv("userpassdata.csv")    
    
 
dic=data.to_dict()


def login():
    y=ue1.get()
    yy=E1.get()
        
    ul=list(dic.values())
    print("the no of user and their passwords:",ul)
    ur=ul[0]
    print("the user name----------------entered:",y)
    userd=list(ur.values())
    #print(userd,"the list of user names")
    
    if y in userd:
        for a in ul[0]:
            if ur[a]==y:
                yo=ul[1][a]
                if yy==yo:
                    from tkinter import filedialog
      
                    # Function for opening the
                    # file explorer window
                    def displaydata():
                        import tkinter
                        import csv
                        
                        root = tkinter.Tk()
                        
                        # open file
                        with open("database.csv", newline = "") as file:
                           reader = csv.reader(file)
                        
                           # r and c tell us where to grid the labels
                           r = 0
                           for col in reader:
                              c = 0
                              for row in col:
                                 # i've added some styling
                                 label = tkinter.Label(root, width = 10, height = 2, \
                                                       text = row, relief = tkinter.RIDGE)
                                 label.grid(row = r, column = c)
                                 c += 1
                              r += 1
                        
                        root.mainloop()
                        
                    def browseFiles():
                        
                        filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Json File","*.json*"),))
                          
                        # Change label contents
                        label_file_explorer.configure(text="File Opened: "+filename)
                        pr=str(filename)
                        if "data" in pr:
                            at=pr.index("data")
                            print("The Selected Json file",pr[at:])
                            
                            
                            import json
                             
                            # Opening JSON file
                            f = open(pr[at:],)
                             
                            # returns JSON object as
                            # a dictionary
                            data = json.load(f)
                             
                            # Iterating through the json
                            # list
                            l=[]
                            ga=list(data[0].keys())
                            print("the keys:---in json file are:",ga)
                            for i in data:
                                fa=list(i.values())
                                l.append(fa)
                                #print(fa)
                             
                            # Closing file
                            f.close()
                            import csv

                            header =ga
                            data = l
                            
                            with open('database.csv', 'w', encoding='UTF8', newline='') as f:
                                writer = csv.writer(f)
                            
                                # write the header
                                writer.writerow(header)
                            
                                # write multiple rows
                                writer.writerows(data)
                            messagebox.showinfo("notification","the data is stored \nin database file")
                            

                            
                          
                                                                                                                      
                    # Create the root window
                    window = Tk()
                      
                    # Set window title
                    window.title('File Explorer')
                      
                    # Set window size
                    window.geometry("500x500")
                      
                    #Set window background color
                    window.config(background = "white")
                      
                    # Create a File Explorer label
                    label_file_explorer = Label(window,text = "logged in as : "+y,width = 100, height = 4,fg = "red")
                    button_display = Button(window,text = "Display data",command = displaydata,bg='blue')
                      
                          
                    button_explore = Button(window,text = "Browse Files",command = browseFiles,bg='green')
                      
                    button_exit = Button(window,text = "logout",bg='red')
                      
                    label_file_explorer.grid(column = 1, row = 1)
                      
                    button_explore.grid(column = 1, row = 2)
                      
                    button_exit.grid(column = 1,row = 3)
                    button_display.grid(column=1,row=4)
                      
                    # Let the window wait for any events
                    window.mainloop()
                    
                    
                else:
                    
                    messagebox.showinfo("notification","try again wrong password")
       
    else:
        #print()
        messagebox.showinfo("notification","try again wrong user name")
       




def newuser():
    y=ue1.get()
    yy=E1.get()
    
    from csv import writer
      
    List=[y,yy]
    with open('userpassdata.csv', 'a') as f_object:
      
        writer_object = writer(f_object)
        writer_object.writerow(List)
        f_object.close()
    messagebox.showinfo("notification","user created\n now close the application and try again")
    
btn = Button(top, text = 'login',command=login)

btn.pack(side='top') 

btn = Button(top, text = 'new user',command=newuser)
 
btn.pack(side = 'top') 
top.mainloop()
