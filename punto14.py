import customtkinter as ctk

inscritos = [0]

def inscribir():
    try:
        if inscritos[0] >= 30:
            lblRes.configure(text="CupoAgotadoError: Aula llena", text_color="red")
        else:
            inscritos[0] += 1
            lblRes.configure(text=f"Inscritos: {inscritos[0]}", text_color="pink")

    except ValueError:
        lblRes.configure(text="Error al inscribir", text_color="red")


app = ctk.CTk()
app.geometry("300x200")
app.title("Capacidad del aula")

ctk.CTkButton(app, text="Inscribir", command=inscribir).pack(pady=10)

lblRes = ctk.CTkLabel(app, text="Inscritos: 0")
lblRes.pack(pady=10)

app.mainloop()
