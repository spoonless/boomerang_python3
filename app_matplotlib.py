"""
Incorporation de matplotlib dans une interface graphique avec tkinter.

Cf. la documentation officielle de matplotblib :

https://matplotlib.org/gallery/user_interfaces/embedding_in_tk_canvas_sgskip.html

"""
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np


root = tkinter.Tk()
root.title("Embedding in Tk")

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def quit_app():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tkinter.Button(master=root, text="Quit", command=quit_app)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
