import numpy as np
import bokeh
from bokeh.plotting import Figure, output_file, show
from bokeh.io import export_png
output_file('sin.html')
x = np.linspace(-10,10,500)
y = np.sin(x)

f = Figure(title='sin(x)',toolbar_location=None)
f.line(x=x,y=y,line_width=3,line_color='red')
f.xaxis.axis_label='x'
f.yaxis.axis_label = 'y'

export_png(f, filename='sinfunction.png')
