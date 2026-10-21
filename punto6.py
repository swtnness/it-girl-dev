import customtkinter as ctk

def cargar_configuracion():
    try:
        archivo = open("config.txt", "r")
        contenido = archivo.read()
        archivo.close()

        lblRes.configure(text=f"Configuracion: {contenido}", text_color="pink")

    except FileNotFoundError:
        lblRes.configure(text="El archivo no existe", text_color="red")


app = ctk.CTk()
app.geometry("350x250")
app.title("Configuracion")

ctk.CTkButton(app, text="Cargar Configuracion", command=cargar_configuracion).pack(pady=10)

lblRes = ctk.CTkLabel(app, text="Espera...")
lblRes.pack(pady=10)

app.mainloop()
