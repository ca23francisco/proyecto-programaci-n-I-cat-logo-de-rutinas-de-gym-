# MANUEL DE JESÚS VIGIL CHICA VC23019
# Emerson Alexander Alfaro Hidalgo AH23012
# Francisco Adonay Cabrera Álvarez CA23055
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import os

class InterfazGimnasio:
    def __init__(self, ventana, db, background_image):
        self.ventana = ventana
        self.db = db
        self.background_image = background_image
        self.crear_interfaz_principal()

    def crear_interfaz_principal(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

        background_label = tk.Label(self.ventana, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        etiqueta_zona = tk.Label(self.ventana, text="Elige la zona a entrenar", bg="black", fg="white", font=("Arial", 18))
        etiqueta_zona.pack(pady=20, anchor="center")

        frame_botones = tk.Frame(self.ventana, bg="black")
        frame_botones.pack(pady=30)

        tk.Button(frame_botones, text="Tren superior", bg="white", fg="black",
                  command=lambda: self.mostrar_grupos_musculares("tren_superior"), width=20, height=3).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(frame_botones, text="Tren inferior", bg="white", fg="black",
                  command=lambda: self.mostrar_grupos_musculares("tren_inferior"), width=20, height=3).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(frame_botones, text="Zona media", bg="white", fg="black",
                  command=lambda: self.mostrar_grupos_musculares("zona_media"), width=20, height=3).pack(side=tk.LEFT, padx=10, pady=10)

    def mostrar_grupos_musculares(self, categoria):
        GruposMusculares(self.ventana, self.db, self.background_image, categoria).mostrar()

class GruposMusculares:
    def __init__(self, ventana, db, background_image, categoria):
        self.ventana = ventana
        self.db = db
        self.background_image = background_image
        self.categoria = categoria

    def mostrar(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

        background_label = tk.Label(self.ventana, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        if self.categoria == "tren_superior":
            grupos = ["Pecho", "Espalda"]
            color = "white"
        elif self.categoria == "tren_inferior":
            grupos = ["Piernas", "Pantorrilla"]
            color = "white"
        elif self.categoria == "zona_media":
            grupos = ["Abdomen", "Cintura"]
            color = "white"
        else:
            grupos = []
            color = "black"

        etiqueta = tk.Label(self.ventana, text=f"Selecciona un grupo muscular de {self.categoria.replace('_', ' ')}",
                            bg=color, fg="black", font=("Arial", 18))
        etiqueta.pack(pady=30)

        frame_botones = tk.Frame(self.ventana, bg="black")
        frame_botones.pack(pady=10)

        for grupo in grupos:
            tk.Button(frame_botones, text=grupo, bg=color, fg="black",
                      command=lambda g=grupo: self.mostrar_rutinas(g), height=2, width=15).pack(side=tk.LEFT, padx=20, pady=10)

        tk.Button(self.ventana, text="Volver al menú principal", command=self.volver_al_menu_principal,
                  bg="black", fg="white", width=20, height=2).pack(pady=20)

    def mostrar_rutinas(self, grupo_muscular):
        Rutinas(self.ventana, self.db, self.background_image, self.categoria, grupo_muscular).mostrar()

    def volver_al_menu_principal(self):
        InterfazGimnasio(self.ventana, self.db, self.background_image).crear_interfaz_principal()

class Rutinas:
    def __init__(self, ventana, db, background_image, categoria, grupo_muscular):
        self.ventana = ventana
        self.db = db
        self.background_image = background_image
        self.categoria = categoria
        self.grupo_muscular = grupo_muscular
        self.rutinas = self.db.obtener_rutinas(grupo_muscular)
        self.indice_rutina = 0

    def mostrar(self):
        if self.rutinas:
            self.mostrar_rutina_individual()
        else:
            self.mostrar_mensaje_sin_rutinas()

    def mostrar_rutina_individual(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

        rutina, gif_path = self.rutinas[self.indice_rutina]

        background_label = tk.Label(self.ventana, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        etiqueta_rutina = tk.Label(self.ventana, text=rutina, bg="white", fg="black", font=("Arial", 18))
        etiqueta_rutina.pack(pady=10)

        if gif_path and os.path.exists(gif_path):
            self.gif_label = tk.Label(self.ventana)
            self.gif_label.pack(pady=10)

            self.gif_frames = self.cargar_gif_animado(gif_path, (300, 200))
            self.reproducir_gif(0)

        frame_navegacion = tk.Frame(self.ventana, bg="black")
        frame_navegacion.pack(side=tk.BOTTOM, pady=10)

        tk.Button(frame_navegacion, text="Anterior rutina", command=self.anterior_rutina, width=15).pack(side=tk.LEFT, padx=100)
        tk.Button(frame_navegacion, text="Siguiente rutina", command=self.siguiente_rutina, width=15).pack(side=tk.RIGHT, padx=100)

        tk.Button(self.ventana, text="Volver a grupos musculares", command=self.volver_a_grupos_musculares,
                  bg="white", fg="black", width=20, height=2).pack(pady=10)

    def cargar_gif_animado(self, gif_path, size):
        gif = Image.open(gif_path)
        frames = []
        for frame in ImageSequence.Iterator(gif):
            frame = frame.resize(size, Image.Resampling.LANCZOS)
            frames.append(ImageTk.PhotoImage(frame))
        return frames

    def reproducir_gif(self, frame_index):
        if self.gif_frames:
            frame = self.gif_frames[frame_index]
            self.gif_label.config(image=frame)
            self.ventana.after(100, self.reproducir_gif, (frame_index + 1) % len(self.gif_frames))

    def anterior_rutina(self):
        if self.indice_rutina > 0:
            self.indice_rutina -= 1
            self.mostrar_rutina_individual()

    def siguiente_rutina(self):
        if self.indice_rutina < len(self.rutinas) - 1:
            self.indice_rutina += 1
            self.mostrar_rutina_individual()

    def mostrar_mensaje_sin_rutinas(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

        etiqueta = tk.Label(self.ventana, text=f"No hay rutinas disponibles para {self.grupo_muscular}",
                            bg="white", fg="black", font=("Arial", 18))
        etiqueta.pack(pady=20)

        tk.Button(self.ventana, text="Volver a grupos musculares", command=self.volver_a_grupos_musculares,
                  bg="black", fg="white", width=20, height=2).pack(pady=10)

    def volver_a_grupos_musculares(self):
        GruposMusculares(self.ventana, self.db, self.background_image, self.categoria).mostrar()
