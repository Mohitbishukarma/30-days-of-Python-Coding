
import tkinter

def resize():
    pass
tk = tkinter.Tk()
text = tkinter.Label(tk,text = "Mohit")
text.pack()

btn = tkinter.Button(tk,text="Quit",command=tk.quit, bg="red",fg="white")
btn.pack(fill=tkinter.X ,expand= 1)

scale = tkinter.Scale(tk, from_= 1, to= 10, orient=tkinter.HORIZONTAL , command= resize)
scale.set(3)
scale.pack(fill=tkinter.X,expand= 1)
tk.mainloop()