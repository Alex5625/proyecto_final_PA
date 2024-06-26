import gi
import pandas as pd



#Probando como usar pandas con gtk grid

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

class CSVViewer(Gtk.Application):
    def __init__(self, dataframe):
        super().__init__()
        self.dataframe = dataframe

    def do_activate(self):
        # Crear la ventana principal
        window = Gtk.ApplicationWindow(application=self)
        window.set_title("CSV Viewer")
        window.set_default_size(800, 600)

        # Crear un ScrolledWindow
        scrolled_window = Gtk.ScrolledWindow()
        window.set_child(scrolled_window)

        # Crear un Grid
        grid = Gtk.Grid()
        scrolled_window.set_child(grid)

        # Añadir encabezados
        for col_num, column in enumerate(self.dataframe.columns):
            label = Gtk.Label(label=column)
            grid.attach(label, col_num, 0, 1, 1)

        # Añadir celdas de datos
        for row_num, row in enumerate(self.dataframe.itertuples(), start=1):
            for col_num, value in enumerate(row[1:]):  # omitir el primer elemento que es el índice
                label = Gtk.Label(label=str(value))
                grid.attach(label, col_num, row_num, 1, 1)

        # Mostrar la ventana
        window.present()

# Cargar el DataFrame
df = pd.read_csv('./nombres_apellidos.csv')

# Crear una instancia de la aplicación y pasarle el DataFrame
app = CSVViewer(df)
app.run(None)
