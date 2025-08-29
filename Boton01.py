import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.valor = 1
        self.ventana01 = tk.Tk()
        self.ventana01.title("Botones")
        self.ventana01.geometry("600x400")

        # Label que muestra el valor
        self.label01 = tk.Label(self.ventana01, text=self.valor, foreground="red", font=("Arial", 14))
        self.label01.pack(pady=10)

        # Frame para centrar los botones
        frame_botones = tk.Frame(self.ventana01)
        frame_botones.pack(pady=10)

        # Botón Sumar
        self.boton01 = tk.Button(frame_botones, text="Sumar", command=self.sumar, width=10)
        self.boton01.pack(side="left", padx=5)

        # Botón Restar
        self.boton02 = tk.Button(frame_botones, text="Restar", command=self.restar, width=10)
        self.boton02.pack(side="left", padx=5)

        self.ventana01.mainloop()

    def sumar(self):
        self.valor += 1
        self.label01.config(text=self.valor)

    def restar(self):
        self.valor -= 1
        self.label01.config(text=self.valor)

ejecutar = Aplicacion()



