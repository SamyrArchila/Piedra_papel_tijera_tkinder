from tkinter import *
from tkinter import messagebox
import random

ventana_juego = Tk()

ventana_juego.title("PIEDRA, PAPEL O TIJERA")

ventana_juego.geometry("800x700")

ventana_juego.resizable(0,0)

ventana_juego.config(bg="grey")

respuestas = 0

def piedra():
    maq = random.randint(1,3)
    if maq == 1:
        t_resultado.insert(INSERT,"empataste, los dos jugadores sacaron piedra " + "\n")
        respuestas =+ 1
    
    if maq == 2:
        t_resultado.insert(INSERT,"ganaste, el jugador saco papel y la CPU piedra " + "\n")
        respuestas =+1
        
    if maq == 3:
        t_resultado.insert(INSERT,"perdiste, el jugador saco tijeras y la CPU piedra " + "\n")
        respuestas =+1

def papel():
    maq = random.randint(1,3)
    if maq == 1:
        t_resultado.insert(INSERT,"ganaste, el jugador saco papel y la CPU piedra " + "\n")
        respuestas =+1

    if maq == 2:
        t_resultado.insert(INSERT,"empatasre, los dos sacaron papel " + "\n")
        respuestas =+1

    if maq == 3:
        t_resultado.insert(INSERT,"perdiste, el jugador saco papel y la CPU tijeras " + "\n")
        respuestas =+1


def tijeras():
    maq = random.randint(1,3)
    if maq == 1:
        t_resultado.insert(INSERT,"perdiste, el jugador saco tijeras y la CPU piedra " + "\n")
        respuestas =+1

    if maq == 2:
        t_resultado.insert(INSERT,"ganaste, el jugaodor saco tijeras y la CPU papel " + "\n")
        respuestas =+1

    if maq == 3:
        t_resultado.insert(INSERT,"emptaste, los dos sacaron tjeras " + "\n")
        respuestas =+1


#-------------------------------
#Frame1 - entrada de datos
#-------------------------------
frame_1 = Frame(ventana_juego)
frame_1.config(bg="ivory2",width=780, height=200)
frame_1.place(x=10,y=10)


# Imagen - logo de la app
logo = PhotoImage(file="img/LOGO1.png")
label_logo = Label(frame_1, image=logo)
label_logo.place(x=10, y=10)

#-------------------------------
#             Titulo
#-------------------------------

titulo = Label(frame_1, text="PIEDRA PAPEL O TIJERA...")
titulo.config(bg="yellow", fg="blue", font=("Arial", 18))
titulo.place(x=405, y=10)

titulo = Label(frame_1, text="      Samyr Alejandro Archila Guiza      ")
titulo.config(bg="yellow", fg="blue", font=("Arial", 18))
titulo.place(x=370, y=50)

frame_2 = Frame(ventana_juego)
frame_2.config(bg="ivory2",width=780, height=250)
frame_2.place(x=10,y=230)

img_bt_tijeras = PhotoImage(file = "img/TIJERA.png")
bt_tijeras = Button(frame_2, image=img_bt_tijeras, width = 200, height = 220, command= tijeras)
bt_tijeras.place(x=40, y=7)

img_bt_piedra = PhotoImage(file="img/PIEDRA.png")
bt_piedra = Button(frame_2,image=img_bt_piedra, width= 200, height= 220, command= piedra)
bt_piedra.place(x= 300, y=7)


img_bt_papel = PhotoImage(file="img/PAPEL.png")
bt_papel = Button(frame_2,image=img_bt_papel, width=200, height=220, command= papel)
bt_papel.place(x=550,y=7)


frame_3 = Frame(ventana_juego)
frame_3.config(bg="ivory2",width=780, height=180)
frame_3.place(x=10,y=500)

# Comando de texto
t_resultado = Text(frame_3, width = 49, height=6)
t_resultado.config(bg="green", fg = "white", font = ("courier",20))
t_resultado.pack()

ventana_juego.mainloop()
    



