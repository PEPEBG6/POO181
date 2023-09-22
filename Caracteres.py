import tkinter as tk

def findMajorityElement(data):
    d = {}
    for char in data:
        d[char] = d.get(char, 0) + 1
        for key, value in d.items():
            if value > len(data) / 2:
                return key
    return -1

def find_majority_element():
    data = data_entry.get()
    
    if not data:
        result_label.config(text="Por favor, ingrese datos")
    else:
        result = findMajorityElement(data)
        if result != -1:
            result_label.config(text=f"El elemento mayoritario es '{result}'")
        else:
            result_label.config(text="El elemento mayoritario no existe")

# Crear la ventana
window = tk.Tk()
window.title("Encontrar Elemento Mayoritario")

# Etiqueta para ingresar los datos
data_label = tk.Label(window, text="Ingrese los datos:")
data_label.pack()

# Cuadro de texto para ingresar los datos
data_entry = tk.Entry(window)
data_entry.pack()

# Botón para encontrar el elemento mayoritario
find_button = tk.Button(window, text="Encontrar Elemento Mayoritario", command=find_majority_element)
find_button.pack()

# Etiqueta para mostrar el resultado
result_label = tk.Label(window, text="")
result_label.pack()

# Iniciar la aplicación
window.mainloop()