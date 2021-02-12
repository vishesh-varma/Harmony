#TK Imports
import tkinter as tk
from PIL import ImageTk, Image
import tkinter.filedialog
import json

#Local Imports
import back

#Initializing the Spotify Clients
back.initialize()

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
    link=musfield.get()
    link=link.strip()

    downloadcheck=back.download(link)
    #FinalMessage.destroy()
    if downloadcheck == 1:
        FinalMessage.configure(text="Download Complete")
        #FinalMessage.pack()
    else:
        FinalMessage.configure(text="Wrong Link Provided")
        #FinalMessage.pack()

#Defining The Window

Root=tk.Tk()
Root.configure(bg='#24292e')
Root.title("Harmony v1.1")
Root.iconbitmap('./assets/logo.ico')

#Accessing data.json and getting the dictionary
with open("data.json") as f:
    Data=json.load(f)

#Creating the widgets

#Image Widget
fimage=ImageTk.PhotoImage(Image.open('./assets/fimage.png'))
imglabel=tk.Label(Root,image=fimage, bg='#24292e')

#Directory Input
Dirfield=tk.Entry(Root, bg="#1C222A", fg='white')
Dirfield.insert(0,f"{Data['Directory']}")

#Directory Button
Dirbutt=tk.Button(Root,text="Select Directory", command=dirselection, bg='#24292e', fg="white")

#Text widget to tell the user to Enter the spotify link below
tell=tk.Label(Root,text="Enter the link or search in the text field below:", bg='#24292e', fg="white")

#Input widget to get the link
musfield=tk.Entry(Root, bg="#1C222A", fg='white')

#Button to download the song
dowbutt=tk.Button(Root, text="Download!", command=dlmusic, bg='#24292e', fg="white")

#Final Download Confirmation Message
FinalMessage=tk.Label(Root, text=" ", bg='#24292e', fg="white")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Packing stuff onto the GUI
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
imglabel.pack(pady=10)
Dirfield.pack(pady=5)
Dirbutt.pack(pady=10)
tell.pack(pady=10, padx=10)
musfield.pack(pady=5)
dowbutt.pack(pady=5)
FinalMessage.pack(pady=5)



Root.mainloop()

