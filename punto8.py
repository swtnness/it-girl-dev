import customtkinter as ctk

def validar_temperatura():
    try:
        temperatura = float(entry1.get())
        if temperatura < -273.15:
            lblRes.configure(text="TemperaturaImposibleError", text_color="red")
        else:
            lblRes.configure(text=f"Temperatura valida: {temperatura} °C", text_color="pink")
    except ValueError:
        lblRes.configure(text="Ingrese un numero valido", text_color="red")

app = ctk.CTk()
app.geometry("300x200")
app.title("Validar temperatura")

entry1 = ctk.CTkEntry(app, placeholder_text="Ingrese temperatura en C")
entry1.pack(pady=10)

ctk.CTkButton(app, text="Validar", command=validar_temperatura).pack(pady=10)

lblRes = ctk.CTkLabel(app, text="Espera...")
lblRes.pack(pady=10)

app.mainloop()
