from Tkinter import*
from PIL import ImageTk


def siguiente():
    siguientelb = Label(ventana2, text ="x")
    siguientelb.grid(row=2, column =1)

def siguiente2():
    siguientelb = Label(ventana2, text ="x")
    siguientelb.grid(row=2, column =2)

def siguiente3():
    siguientelb = Label(ventana2, text ="corecto")
    siguientelb.grid(row=2, column =3)


ventana =Tk()
ventana2=Tk()
frame = Frame(ventana)
frame.pack()

canvas = Canvas(frame, bg="black", width=500, height=550)
canvas.pack()

photoimage = ImageTk.PhotoImage(file="007.png")
canvas.create_image(300,300, image=photoimage)

siguiente= Button(ventana2,text="Pikachu",command=siguiente,width= 20)
siguiente.grid(row=1 , column=1)
siguiente= Button(ventana2,text="Chamander",command=siguiente2 ,width= 20)
siguiente.grid(row=1 , column=2)
siguiente= Button(ventana2,text="Squirtle",command=siguiente3 ,width= 20)
siguiente.grid(row=1 , column=3)






ventana.mainloop()
ventana2.mainloop()





# pokemon
