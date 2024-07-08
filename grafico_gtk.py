import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
import matplotlib
matplotlib.use('GTK4Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_gtk4agg import FigureCanvasGTK4Agg as FigureCanvas

class MatplotlibGTKWindow(Gtk.Window):
    def __init__(self, adipd, adnpo,ads):
        super().__init__(title="Grafica de infecciones/inmunes/sanos")

        self.set_default_size(800, 600)

        # Crear una figura de Matplotlib
        self.fig, self.ax = plt.subplots()

        # Dibujar en el gráfico
        self.dibujar_grafico(adipd, adnpo, ads)

        # Crear un widget de Matplotlib y añadirlo a la ventana
        self.canvas = FigureCanvas(self.fig)
        self.set_child(self.canvas)

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
