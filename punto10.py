import customtkinter as ctk
import math

def calcular_logaritmo():
    try:
        numero = float(entry1.get())

        resultado = math.log(numero)

        lblRes.configure(text=f"Resultado: {resultado:.2f}", text_color="pink")

    except ValueError:
        lblRes.configure(text="Ingrese un numero mayor a cero", text_color="red")


app = ctk.CTk()
app.geometry("300x200")
app.title("Logaritmo natural")

entry1 = ctk.CTkEntry(app, placeholder_text="Ingrese un numero")
entry1.pack(pady=10)

ctk.CTkButton(app, text="Calcular", command=calcular_logaritmo).pack(pady=10)

lblRes = ctk.CTkLabel(app, text="Espera...")
lblRes.pack(pady=10)

app.mainloop()
