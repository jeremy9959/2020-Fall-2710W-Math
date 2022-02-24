import numpy as np
from bokeh.plotting import figure
from bokeh.io import show, output_file

x = np.array(np.arange(10))
y = x**2

f=figure(title="Test")
f.line(x=x,y=y)
output_file('my_picture.html')
show(f)