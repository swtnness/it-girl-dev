import customtkinter as ctk

nombres = ["Vannesa", "Jorge", "Kyungsoo", "Baekhyun"]

def buscardato():
    try:
        idX = int(entry.get())
        lblRes.configure(text=f"Dato: {nombres[idX]}", text_color="pink")
    except IndexError:
        lblRes.configure(text=f"Dato no existe", text_color="red")
    except ValueError:
            lblRes.configure(text=f"Ingrese un dato valido", text_color="red")    

app = ctk.CTk()
app.geometry("300x200")
entry = ctk.CTkEntry(app, placeholder_text="Ingrese el numero de indice a buscar")
entry.pack(pady=10)
ctk.CTkButton(app, text="Buscar", command=buscardato).pack(pady=5)
lblRes = ctk.CTkLabel(app, text="Buscando...")
lblRes.pack()
app.mainloop()

