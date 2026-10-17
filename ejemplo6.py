
import customtkinter as ctk

datos = {"Coca cola":2000, "Cereza": 3000, "Chicle": 700, "Melon": 1000 }

def buscardato():
    try:
        palabra = entryClave.get().capitalize().strip()
        lblRes.configure(text=f"Precio: ${datos[palabra]:.2f}")
    except KeyError:
        lblRes.configure(text="La clave no existe",text_color="red")
    except IndexError:
        lblRes.configure(text="Dato no existe",text_color="red")
    except ValueError:
        lblRes.configure(text="Ingrese un dato válido",text_color="red")


app = ctk.CTk()
app.geometry("350x250")
app.title("Buscar datos")
entryClave = ctk.CTkEntry(app,placeholder_text="Ingrese nombres",width=250)
entryClave.pack(pady=10)

ctk.CTkButton(app,text="Buscar",command=buscardato).pack(pady=5)

lblRes = ctk.CTkLabel(app,text="Buscando...")
lblRes.pack(pady=10)

app.mainloop()
