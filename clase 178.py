from tkinter import*
from random import*
root=Tk()
root.geometry("500x500")
root.config(bg="lightblue")

label_1=Label(root,text="a")
label_1.place(relx=0.5,rely=0.5,anchor=CENTER)


class clase:
    def __init__(self):
        self.score=0
        
    def a():
        self.array1=["ROJO","AZUL","AMARILLO","VERDE","MORADO","CAFE","NARANJA","BLANCO","ROSA"]
        self.var1=randint(0,8)
        self.array2=["red","blue","yellow","brown","purple","pink","green","orange","white"]
        self.var2=randint(0,8)
        label_1["text"]=self.array1[self.var1] 
                     
obj1=clase()
button_1=Button(root,text="Jugar",command=obj1.a)
button_1.place(relx=0.6,rely=0.6,anchor=CENTER)



root.mainloop()
