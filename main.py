# prompt: Diseña una interfáz gráfica para una aplicación de escritorio usando los campos del bloque anterior

import tkinter as tk
from tkinter import ttk,messagebox

import matplotlib.pyplot as plt

from logic import RRF_def, get_score


def crear_interfaz():
  """Crea la interfaz gráfica de usuario."""
  root = tk.Tk()
  root.title("Aplicación de Crédito")

  # Crear un frame principal para organizar los widgets
  main_frame = ttk.Frame(root, padding="10")
  main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

  # Labels y Entries para los campos numéricos
  ttk.Label(main_frame, text="Edad del solicitante:").grid(row=1, column=0, sticky=tk.W, pady=5)
  edad_entry = ttk.Entry(main_frame)
  edad_entry.insert(0, "30")
  edad_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

  ttk.Label(main_frame, text="Calificación crediticia (puntaje):").grid(row=2, column=0, sticky=tk.W, pady=5)
  calificacion_crediticia_entry = ttk.Entry(main_frame)
  calificacion_crediticia_entry.insert(0, "800")
  calificacion_crediticia_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)

  ttk.Label(main_frame, text="Obligaciones financieras (en millones):").grid(row=3, column=0, sticky=tk.W, pady=5)
  obligaciones_financieras_entry = ttk.Entry(main_frame)
  obligaciones_financieras_entry.insert(0, "1000000")
  obligaciones_financieras_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)

  ttk.Label(main_frame, text="Ingresos mensuales (en millones):").grid(row=4, column=0, sticky=tk.W, pady=5)
  ingresos_entry = ttk.Entry(main_frame)
  ingresos_entry.insert(0, "6000000")
  ingresos_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5)

  ttk.Label(main_frame, text="Años de antigüedad laboral:").grid(row=5, column=0, sticky=tk.W, pady=5)
  antiguedad_entry = ttk.Entry(main_frame)
  antiguedad_entry.insert(0, "20")
  antiguedad_entry.grid(row=5, column=1, sticky=(tk.W, tk.E), pady=5)

  ttk.Label(main_frame, text="Número de personas a cargo:").grid(row=6, column=0, sticky=tk.W)
  personas_cargo_entry = ttk.Entry(main_frame)
  personas_cargo_entry.insert(0, "1")
  personas_cargo_entry.grid(row=6, column=1, sticky=(tk.W, tk.E))

  # Separador
  ttk.Separator(main_frame, orient='horizontal').grid(row=7, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

  # Labels y Comboboxes para los campos de lista desplegable
  ttk.Label(main_frame, text="Tipo de contrato:").grid(row=8, column=0, sticky=tk.W)
  contrato_var = tk.StringVar()
  contrato_combobox = ttk.Combobox(main_frame, textvariable=contrato_var, values=["Indefinido", "Fijo", "Prestación de Servicios", "Desempleado"], state="readonly")
  contrato_combobox.grid(row=8, column=1, sticky=(tk.W, tk.E))
  contrato_combobox.set("Indefinido") # Valor por defecto

  ttk.Label(main_frame, text="Estado Civil:").grid(row=9, column=0, sticky=tk.W)
  estado_civil_var = tk.StringVar()
  estado_civil_combobox = ttk.Combobox(main_frame, textvariable=estado_civil_var, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a", "Unión Libre"], state="readonly")
  estado_civil_combobox.grid(row=9, column=1, sticky=(tk.W, tk.E))
  estado_civil_combobox.set("Soltero/a") # Valor por defecto

  ttk.Label(main_frame, text="Condición Médica:").grid(row=10, column=0, sticky=tk.W)
  condicion_medica_var = tk.StringVar()
  condicion_medica_combobox = ttk.Combobox(main_frame, textvariable=condicion_medica_var, values=["Ninguna", "Crónica", "Discapacidad"], state="readonly")
  condicion_medica_combobox.grid(row=10, column=1, sticky=(tk.W, tk.E))
  condicion_medica_combobox.set("Ninguna") # Valor por defecto

  ttk.Label(main_frame, text="Nivel de Estudios:").grid(row=11, column=0, sticky=tk.W)
  nivel_estudios_var = tk.StringVar()
  nivel_estudios_combobox = ttk.Combobox(main_frame, textvariable=nivel_estudios_var, values=["Ninguno", "Primaria", "Secundaria", "Técnico", "Tecnólogo", "Universitario", "Posgrado"], state="readonly")
  nivel_estudios_combobox.grid(row=11, column=1, sticky=(tk.W, tk.E))
  nivel_estudios_combobox.set("Universitario") # Valor por defecto

  # Función para obtener los valores (esto es un ejemplo, puedes añadir la lógica de tu aplicación aquí)
  def obtener_valores():
    edad = int(edad_entry.get())
    calificacion_crediticia = int(calificacion_crediticia_entry.get())
    obligaciones_financieras = float(obligaciones_financieras_entry.get())/1000000
    ingresos = float(ingresos_entry.get())/1000000
    antiguedad = int(antiguedad_entry.get())
    personas_cargo = int(personas_cargo_entry.get())
    contrato = contrato_var.get()
    estado_civil = estado_civil_var.get()
    condicion_medica = condicion_medica_var.get()
    nivel_estudios = nivel_estudios_var.get()

    print("--- Valores ingresados ---")
    print(f"Edad: {edad}")
    print(f"Calificación Crediticia: {calificacion_crediticia}")
    print(f"Obligaciones Financieras: {obligaciones_financieras}")
    print(f"Ingresos: {ingresos}")
    print(f"Antiguedad: {antiguedad}")
    print(f"Personas a Cargo: {personas_cargo}")
    print(f"Contrato: {contrato}")
    print(f"Estado Civil: {estado_civil}")
    print(f"Condición Médica: {condicion_medica}")
    print(f"Nivel de Estudios: {nivel_estudios}")

    RRF = RRF_def( contrato, estado_civil, condicion_medica, nivel_estudios)
    score = get_score(ingresos, calificacion_crediticia, obligaciones_financieras, antiguedad, edad, personas_cargo, RRF)
    tk.messagebox.showinfo("Resultado", f"El puntaje obtenido es: {score}")
  # Botón para procesar los datos
  process_button = ttk.Button(main_frame, text="Procesar", command=obtener_valores)
  process_button.grid(row=12, column=0, columnspan=2, pady=10)

  # Configurar el comportamiento de expansión de las columnas y filas
  root.columnconfigure(0, weight=1)
  root.rowconfigure(0, weight=1)
  main_frame.columnconfigure(1, weight=1)

  root.mainloop()

# Ejecutar la función para crear la interfaz
crear_interfaz() # Descomentar esta línea para ejecutar la interfaz gráfica

