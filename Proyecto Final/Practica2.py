import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class MantenimientoArticulos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mantenimiento de artículos")

        # Conexión a la base de datos
        self.conexion = sqlite3.connect("articulos.db")
        self.cursor = self.conexion.cursor()

        # Crear la tabla si no existe
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS articulos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descripcion TEXT NOT NULL,
            precio REAL NOT NULL
        )
        ''')
        self.conexion.commit()

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')

        self.crear_tab_carga()
        self.crear_tab_consulta()
        self.crear_tab_listado()

    def crear_tab_carga(self):
        self.tab_carga = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_carga, text='Carga de artículos')

        tk.Label(self.tab_carga, text="Artículo:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.entry_articulo_carga = tk.Entry(self.tab_carga)
        self.entry_articulo_carga.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

        tk.Label(self.tab_carga, text="Precio:").grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.entry_precio_carga = tk.Entry(self.tab_carga)
        self.entry_precio_carga.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

        btn_confirmar_carga = tk.Button(self.tab_carga, text="Confirmar", command=self.registrar_articulo)
        btn_confirmar_carga.grid(row=3, column=0, columnspan=2, pady=10)

        self.tab_carga.columnconfigure(1, weight=1)  # Hacer que la columna del Entry se expanda

    def registrar_articulo(self):
        descripcion = self.entry_articulo_carga.get()
        precio = self.entry_precio_carga.get()

        if descripcion and precio:
            try:
                precio = float(precio)  # Validar que el precio sea un número
                # Insertar el artículo en la base de datos
                self.cursor.execute("INSERT INTO articulos (descripcion, precio) VALUES (?, ?)", (descripcion, precio))
                self.conexion.commit()

                # Obtener el ID del artículo recién insertado
                articulo_id = self.cursor.lastrowid

                messagebox.showinfo("Éxito", f"Artículo registrado correctamente. Código único: {articulo_id}")
                
                # Limpiar los campos de entrada
                self.entry_articulo_carga.delete(0, tk.END)
                self.entry_precio_carga.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Error", "El precio debe ser un número válido.")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")

    def crear_tab_consulta(self):
        self.tab_consulta = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_consulta, text='Consulta por código')

        tk.Label(self.tab_consulta, text="Código:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.entry_codigo_consulta = tk.Entry(self.tab_consulta)
        self.entry_codigo_consulta.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

        tk.Label(self.tab_consulta, text="Descripción:").grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.entry_descripcion_consulta = tk.Entry(self.tab_consulta)
        self.entry_descripcion_consulta.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

        tk.Label(self.tab_consulta, text="Precio:").grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.entry_precio_consulta = tk.Entry(self.tab_consulta)
        self.entry_precio_consulta.grid(row=3, column=1, padx=5, pady=5, sticky='ew')

        btn_consultar = tk.Button(self.tab_consulta, text="Consultar", command=self.consultar_por_codigo)
        btn_consultar.grid(row=4, column=0, columnspan=2, pady=10)

        self.tab_consulta.columnconfigure(1, weight=1)  # Hacer que la columna del Entry se expanda

    def consultar_por_codigo(self):
        codigo = self.entry_codigo_consulta.get()

        if codigo:
            try:
                codigo = int(codigo)  # Validar que el código sea un número entero
                # Consultar el artículo en la base de datos
                self.cursor.execute("SELECT descripcion, precio FROM articulos WHERE id = ?", (codigo,))
                articulo = self.cursor.fetchone()

                if articulo:
                    descripcion, precio = articulo
                    self.entry_descripcion_consulta.delete(0, tk.END)
                    self.entry_descripcion_consulta.insert(0, descripcion)

                    self.entry_precio_consulta.delete(0, tk.END)
                    self.entry_precio_consulta.insert(0, f"{precio:.2f}")
                else:
                    messagebox.showinfo("Sin resultados", "No se encontró un artículo con ese código.")
            except ValueError:
                messagebox.showerror("Error", "El código debe ser un número entero válido.")
        else:
            messagebox.showerror("Error", "El campo de código no puede estar vacío.")

    def crear_tab_listado(self):
        self.tab_listado = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_listado, text='Listado completo')

        tk.Label(self.tab_listado, text="Artículo").pack(padx=5, pady=5, anchor='w')  # Etiqueta "Artículo"
        self.listbox_articulos = tk.Listbox(self.tab_listado)
        self.listbox_articulos.pack(padx=5, pady=5, fill='both', expand=True)

        btn_listar_completo = tk.Button(self.tab_listado, text="Listado completo", command=self.listar_todos_los_articulos)
        btn_listar_completo.pack(pady=10)

    def listar_todos_los_articulos(self):
        # Limpiar la lista antes de mostrar los artículos
        self.listbox_articulos.delete(0, tk.END)

        # Consultar todos los artículos en la base de datos
        self.cursor.execute("SELECT id, descripcion, precio FROM articulos")
        articulos = self.cursor.fetchall()

        if articulos:
            for articulo in articulos:
                codigo, descripcion, precio = articulo
                self.listbox_articulos.insert(tk.END, f"Código: {codigo}, Descripción: {descripcion}, Precio: {precio:.2f}")
        else:
            self.listbox_articulos.insert(tk.END, "No hay artículos registrados.")

    def __del__(self):
        # Cerrar la conexión a la base de datos al finalizar
        self.conexion.close()

if __name__ == "__main__":
    app = MantenimientoArticulos()
    app.mainloop()