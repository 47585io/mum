import tkinter as tk
from PIL import Image

pic=Image.open("/home/tom/vscode/HTML/pic/termail.jpg","r")
pic.convert("RGBA")
pic.save("/home/tom/vscode/HTML/pic/new.png")
win=tk.Tk()
win.geometry("700x1600")
lab2=tk.Label(win,background="black",foreground="white")

def fun(event):
   # print(str(event.x)+"\n"+str(event.y_root))
    lab2['text'] = str(event.x)+"\n"+str(event.y)
    lab2.place(x=event.x,y=event.y)

furry = tk.PhotoImage(file="/home/tom/vscode/HTML/pic/new.png")
lab=tk.Label(win,image=furry)
lab.pack()

win.bind("<Motion>",func=fun)
win.mainloop()