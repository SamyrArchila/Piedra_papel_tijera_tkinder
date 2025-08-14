import tkinter as tk
from tkinter import PhotoImage
import random
import os

# ------------------ util: rutas e imágenes ------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "img")
MAX_PX = 120  # tamaño máximo deseado por lado

def cargar_imagen(nombre, max_px=MAX_PX):
    """Carga una imagen desde img/ y la reduce por factor entero si es grande."""
    ruta = os.path.join(IMG_DIR, nombre)
    img = PhotoImage(file=ruta)
    w, h = img.width(), img.height()
    # reducir por factor entero para que encaje (PhotoImage solo acepta enteros)
    factor = max(1, max(w // max_px, h // max_px))
    if factor > 1:
        img = img.subsample(factor, factor)
    return img

# ------------------ ventana ------------------
root = tk.Tk()
root.title("Piedra, Papel o Tijera")
root.geometry("700x400")
root.resizable(False, False)

# ------------------ UI ------------------
frame_top = tk.Frame(root, width=700, height=180, bg="white")
frame_top.pack_propagate(False)
frame_top.pack()

lbl_resultado = tk.Label(frame_top, text="Elige una opción", font=("Arial", 20), bg="white")
lbl_resultado.pack(pady=(20, 6))

lbl_jugador = tk.Label(frame_top, text="Jugador: —", font=("Arial", 14), bg="white")
lbl_jugador.pack()

lbl_pc = tk.Label(frame_top, text="PC: —", font=("Arial", 14), bg="white")
lbl_pc.pack()

frame_btns = tk.Frame(root, width=700, height=200, bg="#dcdcdc")
frame_btns.pack_propagate(False)
frame_btns.pack()

# ------------------ lógica ------------------
def jugar(eleccion_jugador):
    opciones = ["Piedra", "Papel", "Tijera"]
    eleccion_pc = random.choice(opciones)

    lbl_jugador.config(text=f"Jugador: {eleccion_jugador}")
    lbl_pc.config(text=f"PC: {eleccion_pc}")

    if eleccion_jugador == eleccion_pc:
        lbl_resultado.config(text="Empate 😐")
    elif (eleccion_jugador == "Piedra" and eleccion_pc == "Tijera") or \
         (eleccion_jugador == "Papel" and eleccion_pc == "Piedra") or \
         (eleccion_jugador == "Tijera" and eleccion_pc == "Papel"):
        lbl_resultado.config(text="¡Ganaste! 🎉")
    else:
        lbl_resultado.config(text="Perdiste ☹️")

# ------------------ imágenes + botones ------------------
img_piedra  = cargar_imagen("piedra.png")
img_papel   = cargar_imagen("papel.png")
img_tijeras = cargar_imagen("tijeras.png")

# OJO: no pongas width/height en los botones con image (cortan la imagen)
bt_piedra  = tk.Button(frame_btns, image=img_piedra,  command=lambda: jugar("Piedra"),  cursor="hand2", bd=2)
bt_papel   = tk.Button(frame_btns, image=img_papel,   command=lambda: jugar("Papel"),   cursor="hand2", bd=2)
bt_tijeras = tk.Button(frame_btns, image=img_tijeras, command=lambda: jugar("Tijera"), cursor="hand2", bd=2)

# una distribución simple en grid
frame_btns.columnconfigure((0,1,2), weight=1)
bt_piedra.grid(row=0, column=0, pady=40)
bt_papel.grid(row=0, column=1, pady=40)
bt_tijeras.grid(row=0, column=2, pady=40)

root.mainloop()


