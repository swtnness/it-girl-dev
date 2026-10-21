import customtkinter as ctk

def convertir_moneda():
    try:
        dinero = float(entry1.get())
        tasa = 0.85

        if dinero < 0:
            lblRes.configure(text="No se permiten negativos", text_color="red")
        else:
            resultado = dinero * tasa
            lblRes.configure(text=f"Resultado: {resultado:.2f} EUR", text_color="pink")

    except ValueError:
        lblRes.configure(text="Ingrese un monto valido", text_color="red")


app = ctk.CTk()
app.geometry("300x200")
app.title("Conversor de moneda")

entry1 = ctk.CTkEntry(app, placeholder_text="Ingrese dinero en USD")
entry1.pack(pady=10)

ctk.CTkButton(app, text="Convertir", command=convertir_moneda).pack(pady=10)

lblRes = ctk.CTkLabel(app, text="Espera...")
lblRes.pack(pady=10)

app.mainloop()
