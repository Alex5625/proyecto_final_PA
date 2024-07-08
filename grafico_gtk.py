import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gio, GObject, Gtk, Gdk, GdkPixbuf, GLib
import matplotlib
matplotlib.use('GTK4Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_gtk4agg import FigureCanvasGTK4Agg as FigureCanvas

def on_quit_action(self, _action):
    quit()


class MatplotlibGTKWindow(Gtk.Window):
    def __init__(self, adipd, adnpo,ads):
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
        # Crear una figura de Matplotlib
        self.fig, self.ax = plt.subplots()

        # Dibujar en el gráfico
        self.dibujar_grafico(adipd, adnpo, ads)

        # Crear un widget de Matplotlib y añadirlo a la ventana
        self.canvas = FigureCanvas(self.fig)
        self.set_child(self.canvas)

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


    def dibujar_grafico(self, adipd, adnpo, ads):
        longitud_x = len(adipd)
        arreglo_eje_x = list(range(1, longitud_x + 1))

        # ejes X e Y
        self.ax.plot(arreglo_eje_x, adipd, label='Contagiados por dia')
        self.ax.plot(arreglo_eje_x, adnpo, label='Inmunes por dia')
        self.ax.plot(arreglo_eje_x, ads, label = 'Sanos por dia')
        # Título del gráfico
        self.ax.set_title("Grafica de contagiados/inmunes")

        # Etiquetas de los ejes
        self.ax.set_xlabel("Dia")
        self.ax.set_ylabel("Numero de personas")

        # Mostrar la leyenda
        self.ax.legend()
