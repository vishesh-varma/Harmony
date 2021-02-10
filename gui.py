#TK Imports
import tkinter as tk
from PIL import ImageTk, Image
import tkinter.filedialog
import json

#Local Imports

#Defining the widget commands

def dirselection():
    Dirfield.delete(0,tk.END)
    directory=tkinter.filedialog.askdirectory(title="Select Download Directory", initialdir=Data["Directory"])
    Dirfield.insert(0,directory)
    Data["Directory"]=directory
    #changes the directory location in data
    with open('data.json', 'w') as f:
        json.dump(Data, f)

def dlmusic():
    pass

#Defining The Window

Root=tk.Tk()
Root.configure(bg='#24292e')
Root.title("Harmony v1.1")

#Accessing data.json and getting the dictionary
with open("data.json") as f:
    Data=json.load(f)

#Creating the widgets

#Image Widget
fimage=ImageTk.PhotoImage(Image.open('./assets/fimage.png'))
imglabel=tk.Label(Root,image=fimage)

#Directory Input
Dirfield=tk.Entry(Root)
Dirfield.insert(0,f"{Data['Directory']}")

#Directory Button
Dirbutt=tk.Button(Root,text="Select Directory", command=dirselection)

#Text widget to tell the user to Enter the spotify link below
tell=tk.Label(Root,text="Enter the link in the text field below:")

#Input widget to get the link
musfield=tk.Entry(Root)

#Button to download the song
dowbutt=tk.Button(Root, text="Download!", command=dlmusic)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Packing stuff onto the GUI
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
imglabel.pack()
Dirbutt.pack()
Dirfield.pack()
tell.pack()
musfield.pack()
dowbutt.pack()



Root.mainloop()

