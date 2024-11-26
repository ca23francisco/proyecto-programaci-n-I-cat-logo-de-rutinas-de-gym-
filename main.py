# MANUEL DE JESÚS VIGIL CHICA VC23019
# Emerson Alexander Alfaro Hidalgo AH23012
# Francisco Adonay Cabrera Álvarez CA23055
import tkinter as tk
import os
from database import BaseDeDatos
from interface import InterfazGimnasio

def main():
    db = BaseDeDatos()
    ventana = tk.Tk()
    ventana.title("Programa de Ejercicios")
    ventana.geometry("720x800")
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_imagen = os.path.join(ruta_actual, "imagenes", "49e8a2f874cffe0e4e9c6926fb3756b5.png")
    if os.path.exists(ruta_imagen):
        background_image = tk.PhotoImage(file=ruta_imagen)
    else:
        print(f"Error: La imagen no existe en la ruta: {ruta_imagen}")
        return
    interfaz = InterfazGimnasio(ventana, db, background_image)
    ventana.mainloop()

if __name__ == "__main__":
    main()
