import customtkinter as ctk

def calcular_descuento():
    try:
        precio = float(entry1.get())
        descuento = float(entry2.get())

        resultado = precio - (precio * descuento / 100)

        lblRes.configure(text=f"Precio final: ${resultado:.2f}", text_color="pink")

    except ValueError:
        lblRes.configure(text="Ingrese datos validos", text_color="red")

    finally:
        entry1.delete(0, "end")
        entry2.delete(0, "end")


app = ctk.CTk()
app.geometry("300x250")
app.title("Calculadora de descuentos")

entry1 = ctk.CTkEntry(app, placeholder_text="Ingrese el precio")
entry1.pack(pady=10)

entry2 = ctk.CTkEntry(app, placeholder_text="Ingrese descuento (%)")
entry2.pack(pady=10)

ctk.CTkButton(app, text="Calcular", command=calcular_descuento).pack(pady=10)

lblRes = ctk.CTkLabel(app, text="Espera...")
lblRes.pack(pady=10)

app.mainloop()
