import csv
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gio, GObject, Gtk, Gdk, GdkPixbuf, GLib
import matplotlib
matplotlib.use('GTK4Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_gtk4agg import FigureCanvasGTK4Agg as FigureCanvas
import pandas as pd

def on_quit_action(self, _action):
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

        menu = Gio.Menu.new()

        self.popover = Gtk.PopoverMenu()
        self.popover.set_menu_model(menu)

        self.menu_popover = Gtk.MenuButton()
        self.menu_popover.set_popover(self.popover)
        self.menu_popover.set_icon_name("open-menu-symbolic")

        header_bar.pack_end(self.menu_popover)


        # Create action group
        action_group = Gio.SimpleActionGroup.new()
        self.insert_action_group("win", action_group)

        # Add an about dialog
        about_menu = Gio.SimpleAction.new("about", None)
        about_menu.connect("activate", self.show_about_dialog)
        action_group.add_action(about_menu)
        menu.append("Acerca de", "win.about")

        action = Gio.SimpleAction.new("quit", None)
        action.connect("activate", on_quit_action)
        action_group.add_action(action)
        menu.append("Salir", "win.quit") 

        #Boton para el header bar
        self.boton_guardar = Gtk.Button()
        self.boton_guardar.set_label("Guardar catastro")
        self.boton_guardar.connect("clicked", self.on_clicked_guardar_archivo)
        header_bar.pack_start(self.boton_guardar)


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


    def  generar_csv(self,dias, sanos, infectados, inmunes):

        with open("Datos_infectados.csv", mode = 'w', newline = '') as file:

            writer = csv.writer(file)

            writer.writerow(["Dias","Personas Sanas", "Personas Infectadas", "Personas Inmunes"])

            for dia, sano, infectado, inmune in zip(dias,sanos,infectados,inmunes):
                writer.writerow([dia,sano,infectado,inmune])



        # print(f"\n\n El largo del arreglo dias es: {len(dias)}\nEl largo del arreglo sanos es: {len(sanos)}\nEl largo del arreglo infectados es:{len(infectados)}\nEl largo del areglo inmunes es: {len(inmunes)}")
        #Se crea el dataframe, pandas trabaja con dataframe
        # data = {
        #         "Dias": dias, 
        #         "Personas Sanas": sanos,
        #         "Personas Infectadas": infectados,
        #         "Personas Inmunes": inmunes
        # }
        # df = pd.DataFrame(data)

        # #Guarda el archivo en un archivo csv
        # df.to_csv(nombre_archivo, index = False)


    def show_about_dialog(self, action, param):
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
