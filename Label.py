from tkinter import *

root=Tk() #le damos a la raiz la funcion

Frame=Frame(root, width=500, heigh=500) #creamos el frame y le damos un espacio

Frame.pack() #lo empaquetamos

Label=Label(Frame, text="Esto esta yendo calide", fg="red",image="mi_imagen" font=("calibre", 20))# en la funcion label podemos modificar la forma del texto de muchas formas

Label.place(x=50, y=0)#tambien se puede empaquetar(pack) , pero entonces el ancho y largo se adaptaria al tamaño del texto

mi_imagen=PhotoImage(file="nombre del archivo")#podemos meter la imagen en label para que aparezca





root.mainloop() #el mainloop siempre al final