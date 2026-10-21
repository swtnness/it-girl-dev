import customtkinter as ctk

estudiantes = ["Vannesa", "Jorge", "Kyungsoo", "Baekhyun", "Daniel"]

def buscardato():
    try:
        idX = int(entry1.get())
        if idX < 0:
            lblRes.configure(text="Dato no existe", text_color="red")
        else:
            lblRes.configure(text=f"Estudiante: {estudiantes[idX]}", text_color="pink")
    except IndexError:
        lblRes.configure(text="Dato no existe", text_color="red")
    except ValueError:
        lblRes.configure(text="Ingrese un indice valido", text_color="red")

app = ctk.CTk()
app.geometry("300x200")
app.title("Buscar estudiantes")

entry1 = ctk.CTkEntry(app, placeholder_text="Ingrese el indice")
entry1.pack(pady=10)

ctk.CTkButton(app, text="Buscar", command=buscardato).pack(pady=10)

lblRes = ctk.CTkLabel(app, text="Buscando...")
lblRes.pack(pady=10)

app.mainloop()

