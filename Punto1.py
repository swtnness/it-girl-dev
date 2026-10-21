import customtkinter as ctk

def calcular_imc():
    try:
        peso = float(entry1.get())
        altura = float(entry2.get())
        
        resultado = peso / altura**2
        
        lblRes.configure(text=f"Su ICM es: {resultado}", text_color="pink")

    except ValueError:
        lblRes.configure(text="Ingrese datos validos", text_color="red")
        
    except ZeroDivisionError:
        lblRes.configure(text="No se puede dividir entre cero", text_color="red")

app = ctk.CTk()
app.geometry("300x200")
app.title("Calculadora de IMC")

entry1 = ctk.CTkEntry(app, placeholder_text="Ingrese el peso (Kg)")
entry1.pack(pady=10)

entry2 = ctk.CTkEntry(app, placeholder_text="Ingrese su altura (m)")
entry2.pack(pady=10)

ctk.CTkButton(app, text="Calcular IMC", command=calcular_imc).pack(pady=10)
lblRes = ctk.CTkLabel(app, text="Espera...")
lblRes.pack(pady=10)
app.mainloop()