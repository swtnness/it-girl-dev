import customtkinter as ctk

def sumar_numeros():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        resultado = num1 + num2
        lblRes.configure(text=f"Resultado: {resultado}", text_color="pink")
    except ValueError:
        lblRes.configure(text="Ingrese numeros validos", text_color="red")
app = ctk.CTk()
app.geometry("300x250")
app.title("Sumar numeros")

entry1 = ctk.CTkEntry(app, placeholder_text="Primer numero")
entry1.pack(pady=10)

entry2 = ctk.CTkEntry(app, placeholder_text="Segundo numero")
entry2.pack(pady=10)

ctk.CTkButton(app, text="Sumar", command=sumar_numeros).pack(pady=10)

lblRes = ctk.CTkLabel(app, text="Espera...")
lblRes.pack(pady=10)

app.mainloop()
