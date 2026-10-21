import customtkinter as ctk

def validar_puerto():
    try:
        puerto = int(entry1.get())
        if puerto < 1 or puerto > 65535:
            lblRes.configure(text="Puerto fuera de rango", text_color="red")
        else:
            lblRes.configure(text=f"Puerto valido: {puerto}", text_color="pink")
    except ValueError:
        lblRes.configure(text="Ingrese un puerto valido", text_color="red")


app = ctk.CTk()
app.geometry("300x200")
app.title("Verificar puerto")

entry1 = ctk.CTkEntry(app, placeholder_text="Ingrese el puerto")
entry1.pack(pady=10)

ctk.CTkButton(app, text="Verificar", command=validar_puerto).pack(pady=10)

lblRes = ctk.CTkLabel(app, text="Espera...")
lblRes.pack(pady=10)

app.mainloop()
