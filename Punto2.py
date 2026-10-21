import customtkinter as ctk

def validar_email():
    try:
        email = entry1.get()
        if "@" in email and "." in email:
            print("Correo valido")
        else:
            print("Correo invalido")
        lblRes.configure(text=f"Email valido", text_color="pink")

    except EmailInvalidoError:
    lblRes.configure(text="Correo invalido", text_color="red")
        
app = ctk.CTk()
app.geometry("300x200")
app.title("Validacion email")

entry1 = ctk.CTkEntry(app, placeholder_text="Ingrese su email")
entry1.pack(pady=10)

ctk.CTkButton(app, text="Validacion email", command=validar_email).pack(pady=10)
lblRes = ctk.CTkLabel(app, text="Espera...")
lblRes.pack(pady=10)
app.mainloop()