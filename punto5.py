import customtkinter as ctk

datos = {"Arroz": 10,"Papa": 15,"Aceite": 30,"Cereal": 100}

def buscardato():
    try:
        palabra = entry1.get().strip().capitalize()
        lblRes.configure(text=f"Stock: {datos[palabra]}", text_color="pink")
    except KeyError:
        lblRes.configure(text="El producto no existe", text_color="red")


app = ctk.CTk()
app.geometry("300x200")
app.title("Inventario")

entry1 = ctk.CTkEntry(app, placeholder_text="Ingrese el producto")
entry1.pack(pady=10)

ctk.CTkButton(app, text="Buscar", command=buscardato).pack(pady=10)

lblRes = ctk.CTkLabel(app, text="Buscando...")
lblRes.pack(pady=10)

app.mainloop()
