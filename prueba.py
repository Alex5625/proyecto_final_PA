import gi
import pandas as pd

# Probando cómo usar pandas con Gtk.TreeView

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio

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

        # Crear un ListStore y TreeView
        liststore = Gtk.ListStore(*[str] * len(self.dataframe.columns))
        treeview = Gtk.TreeView(model=liststore)


        # Habilitar las lineas de cuadriculas

        treeview.set_grid_lines(Gtk.TreeViewGridLines.BOTH)
        
        # Añadir encabezados y columnas al TreeView
        for i, column in enumerate(self.dataframe.columns):
            renderer = Gtk.CellRendererText()
            tvcolumn = Gtk.TreeViewColumn(column, renderer, text=i)
            treeview.append_column(tvcolumn)

        # Añadir filas al ListStore
        for row in self.dataframe.itertuples(index=False, name=None):
            liststore.append([str(value) for value in row])

        # Añadir el TreeView al ScrolledWindow
        scrolled_window.set_child(treeview)

        # Mostrar la ventana
        window.present()

# Cargar el DataFrame
df = pd.read_csv('./nombres_apellidos.csv')

# Crear una instancia de la aplicación y pasarle el DataFrame
app = CSVViewer(df)
app.run(None)
