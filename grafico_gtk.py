import csv
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gio, GObject, Gtk, Gdk, GdkPixbuf, GLib
import matplotlib
matplotlib.use('GTK4Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_gtk4agg import FigureCanvasGTK4Agg as FigureCanvas
import pandas as pd

def on_quit_action(self):
    quit()


class MatplotlibGTKWindow(Gtk.Window):
    def __init__(self, infectados, inmunes,sanos):
        #Guardar las variables dentro de la clase
        self.infectados = infectados
        self.inmunes = inmunes
        self.sanos = sanos

        super().__init__()

        self.set_default_size(800, 600)
        #Crear HeaderBar        
        header_bar = Gtk.HeaderBar.new()
        self.set_titlebar(titlebar = header_bar)
        self.set_title("Grafica de infecciones/inmunes/sanos")

        #Botones para el header bar
        self.boton_guardar = Gtk.Button()
        self.boton_guardar.set_label("Guardar catastro")
        self.boton_guardar.connect("clicked", self.on_clicked_guardar_archivo)
        header_bar.pack_start(self.boton_guardar)

        self.boton_leer = Gtk.Button()
        self.boton_leer.set_label("Leer archivo")
        self.boton_leer.connect("clicked", self.on_clicked_leer_archivo)
        header_bar.pack_start(self.boton_leer)

        self.boton_salir = Gtk.Button()
        self.boton_salir.set_label("Salir")
        self.boton_salir.connect("clicked", on_quit_action)
        header_bar.pack_end(self.boton_salir)

        self.boton_info = Gtk.Button()
        self.boton_info.set_label("Acerca De")
        self.boton_info.connect("clicked", self.show_about_dialog)
        header_bar.pack_end(self.boton_info)

        # Crear una figura de Matplotlib
        self.fig, self.ax = plt.subplots()

        # Dibujar en el gráfico
        self.dibujar_grafico(infectados, inmunes, sanos)

        # Crear un widget de Matplotlib y añadirlo a la ventana
        self.canvas = FigureCanvas(self.fig)
        self.set_child(self.canvas)

    def on_clicked_guardar_archivo(self, button):
        dias = list(range(0, len(self.infectados)))
        self.generar_csv(dias, self.sanos, self.infectados, self.inmunes)

        # ------crear mensaje de dialogo ---------
        dialog = Gtk.MessageDialog(title="Ventana de Guardado",
                                   transient_for=self,
                                   modal=True,
                                   default_width=300,
                                   default_height=50)

        # ----- añade texto debajo de titulo
        dialog.set_property("secondary-text","Se ha guardado el archivo correctamente")
        dialog.set_deletable(True)
        dialog.set_visible(True)

    def  generar_csv(self,dias, sanos, infectados, inmunes):

        with open("Datos_infectados.csv", mode = 'w', newline = '') as file:

            writer = csv.writer(file)

            writer.writerow(["Dias","Personas Sanas", "Personas Infectadas", "Personas Inmunes"])

            for dia, sano, infectado, inmune in zip(dias,sanos,infectados,inmunes):
                writer.writerow([dia,sano,infectado,inmune])


    def on_clicked_leer_archivo(self, button):
        # Leer el archivo CSV y mostrarlo en una nueva ventana
        self.df = pd.read_csv("Datos_infectados.csv")
        self.show_csv_window()

    def show_csv_window(self):
        window = Gtk.Window()
        window.set_title("CSV Viewer")
        window.set_default_size(800, 600)

        # Crear un ScrolledWindow
        scrolled_window = Gtk.ScrolledWindow()
        window.set_child(scrolled_window)

        # Crear un ListStore y TreeView
        liststore = Gtk.ListStore(*[str] * len(self.df.columns))
        treeview = Gtk.TreeView(model=liststore)

        # Habilitar las líneas de cuadrícula
        treeview.set_grid_lines(Gtk.TreeViewGridLines.BOTH)
        
        # Añadir encabezados y columnas al TreeView
        for i, column in enumerate(self.df.columns):
            renderer = Gtk.CellRendererText()
            tvcolumn = Gtk.TreeViewColumn(column, renderer, text=i)
            treeview.append_column(tvcolumn)

        # Añadir filas al ListStore
        for row in self.df.itertuples(index=False, name=None):
            liststore.append([str(value) for value in row])

        # Añadir el TreeView al ScrolledWindow
        scrolled_window.set_child(treeview)

        # Mostrar la ventana
        window.show()

    def show_about_dialog(self, action):
        self.about = Gtk.AboutDialog()
        self.about.set_transient_for(self)
        self.about.set_modal(self)

        self.about.set_authors(["Alexis Hernandez"])
        self.about.set_copyright("Copyright 2024 Elexs69")
        self.about.set_license_type(Gtk.License.GPL_3_0)
        self.about.set_website("https://github.com/Alex5625")
        self.about.set_website_label("My Github")
        self.about.set_version("1.0")
        self.about.set_logo_icon_name("org.example.example")
        self.about.set_visible(True)


    def dibujar_grafico(self, infectados, inmunes, sanos):
        longitud_x = len(infectados)
        arreglo_eje_x = list(range(1, longitud_x + 1))

        # ejes X e Y
        self.ax.plot(arreglo_eje_x, infectados, label='Contagiados por dia')
        self.ax.plot(arreglo_eje_x, inmunes, label='Inmunes por dia')
        self.ax.plot(arreglo_eje_x, sanos, label = 'Sanos por dia')
        # Título del gráfico
        self.ax.set_title("Grafica de contagiados/inmunes")

        # Etiquetas de los ejes
        self.ax.set_xlabel("Dia")
        self.ax.set_ylabel("Numero de personas")

        # Mostrar la leyenda
        self.ax.legend()
