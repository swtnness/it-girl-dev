import customtkinter as ctk

def convertir_binario():
    try:
        binario = entry1.get()
        resultado = int(binario, 2)
        lblRes.configure(text=f"Resultado: {resultado}", text_color="pink")
    except ValueError:
        lblRes.configure(text="Ingrese un binario valido", text_color="red")

app = ctk.CTk()
app.geometry("300x200")
app.title("Convertidor binario")

entry1 = ctk.CTkEntry(app, placeholder_text="Ingrese codigo binario")
entry1.pack(pady=10)

ctk.CTkButton(app, text="Convertir", command=convertir_binario).pack(pady=10)

lblRes = ctk.CTkLabel(app, text="Espera...")
lblRes.pack(pady=10)

app.mainloop()
