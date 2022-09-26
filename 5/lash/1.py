import tkinter as tk
from PIL import Image

pic=Image.open("/home/tom/vscode/HTML/pic/termail.jpg","r")
pic.convert("RGBA")
pic.save("/home/tom/vscode/HTML/pic/new.png")
win=tk.Tk()
win.geometry("800x1600")
lab2=tk.Label(win,background="black",foreground="white")

def fun(event):
   # print(str(event.x)+"\n"+str(event.y_root))
    lab2['text'] = str(event.x)+"\n"+str(event.y)

furry = tk.PhotoImage(file="/home/tom/vscode/HTML/pic/new.png")
lab=tk.Label(win,image=furry)
lab.place(x=0,y=0)
lab2.place(x=750,y=0)

win.bind("<Motion>",func=fun)
win.mainloop()