import numpy as np
from bokeh.layouts import row
from  bokeh.plotting import figure, output_file
from bokeh.io import export_png

x=np.arange(0,10,1)
y = np.random.choice(x,size=5*x.shape[0],replace=True)
x = np.random.choice(x,size=5*x.shape[0],replace=True)

f=figure(title='A Relation',toolbar_location=None)
f.axis.ticker=[0,1,2,3,4,5,6,7,8,9]
f.scatter(x,y,size=10, color='red')


g = figure(title='A Function',toolbar_location=None) 
g.axis.ticker=[0,1,2,3,4,5,6,7,8,9]
x=np.arange(0,10,1)
y = np.random.choice(x,size=x.shape[0],replace=True)
g.scatter(x,y,size=10,color='green')
export_png(row(f,g),filename='relfunction.png')
