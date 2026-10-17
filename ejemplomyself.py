import customtkinter as ctk

# Validaciones numéricas
def calcular_cuadrado():
    try:
        dividendo = float(entry.get())
        divisor = float(entry2.get())
        division = dividendo / divisor
        lblRes.configure(
            text=f"Resultado: {division}",
            text_color="pink"
        )
    except ValueError:
        lblRes.configure(
            text="Ingrese un valor válido",
            text_color="red"
        )
    except ZeroDivisionError:
         lblRes.configure(
             text="No se puede dividir entre cero",
             texto_color="red"
         )

# Crear ventana
app = ctk.CTk()
# Dimensionar la ventana
app.geometry("400x400")
# Crear el Entry
entry = ctk.CTkEntry(app)
entry.pack(pady=10)

entry2 = ctk.CTkEntry(app)
entry2.pack(pady=10)
# Crear el botón
ctk.CTkButton(
    app,
    text="Calcular",
    command=calcular_cuadrado
).pack(pady=10)
# Crear etiqueta de respuesta
lblRes = ctk.CTkLabel(
    app,
    text="Espera..."
)
lblRes.pack(pady=10)
# Mantener la ventana abierta
app.mainloop()
