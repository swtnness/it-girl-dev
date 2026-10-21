import customtkinter as ctk

def validar_contrasena():
    try:
        contrasena = entry1.get()
        if len(contrasena) < 8:
            lblRes.configure(text="Contraseña muy corta", text_color="red")
        else:
            lblRes.configure(text="Contraseña valida", text_color="pink")
    except ValueError:
        lblRes.configure(text="Ingrese datos validos", text_color="red")

app = ctk.CTk()
app.geometry("300x200")
app.title("Validar contraseña")

entry1 = ctk.CTkEntry(app, placeholder_text="Ingrese contraseña")
entry1.pack(pady=10)

ctk.CTkButton(app, text="Validar", command=validar_contrasena).pack(pady=10)

lblRes = ctk.CTkLabel(app, text="Espera...")
lblRes.pack(pady=10)

app.mainloop()
