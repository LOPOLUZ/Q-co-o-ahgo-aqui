from tkinter import * #para importar la libreria tkinter

raiz=Tk() #para importar la clase Tk 

raiz.title("Joder ya caracoles")
raiz.resizable(1,1)#Tamaño que puede adquirir la ventana
raiz.iconbitmap("")#nombre de la foto acabada en .ico debe de estar en la misma carpeta
#raiz.geometry("500x500")#Para el tamaño de la ventana 
raiz.config(bg="red")# config sirve para muchas cosas aqui bg significa background
#cambiar extension del archivo por .pyw para que no abra la cmd  
miFrame=Frame()#creamos nuestro frame
miFrame.pack(side="left" )#lo enpaquetamos, tamnien podemos darle una direccion(left, right, bottom, top) y un anchor (n de norte , e de est, w de west, s  de sur) tambien fil para que se auto dimensione x horizontalmente e y verticalmente (para que se expanda en y depebemos de poner el comadno expad="true"), both para ambos )
miFrame.config(bg="blue") #primero debemos de darle tamañoa  nuestro frmae
miFrame.config( width="500",height="500") #le damos el ancho y la altura


#bordes
miFrame.config(bd=35)
miFrame.config(relief="groove")
#cursor
miFrame.config(cursor="hand2") #pirate cursor de calavera




















raiz.mainloop() #mainloop siempre debe de estar al final
