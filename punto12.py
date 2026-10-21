import customtkinter as ctk

datos = ["Vannesa", "Jorge", "Kyungsoo"]

def buscar_atributo():
    try:
        resultado = datos.buscar()
        lblRes.configure(text=f"Resultado: {resultado}", text_color="pink")
    except AttributeError:
        lblRes.configure(text="El metodo no existe", text_color="red")


app = ctk.CTk()
app.geometry("300x200")
app.title("Buscar atributo")

ctk.CTkButton(app, text="Buscar", command=buscar_atributo).pack(pady=10)

lblRes = ctk.CTkLabel(app, text="Espera...")
lblRes.pack(pady=10)

app.mainloop()
