'''
Why Build Visuals?

1) Conduct exploratory data analysis
2) Communicate data clearly
3) Share unbiased representation of data
4) Support recommendations to stakeholders

Less is more effective, attractive, and impactive

http://www.darkhorseanalytics.com/

Matplotlib Architecture
1) Backend - FigureCanvas, Renderer, Event
2) Artist - Artist
3) Scripting - pyplot

matplotlib.backend_bases.FigureCanvas
  encompasses the area onto which the figure is drawn

matplotlib.backend_bases.Renderer
  knows how to draw on the FigureCanvas
  
matplotlib.backend_bases.Event
  handles user inputs such as keyboard strokes and mouse clicks
  
Artist
  knows how to use the Renderer to draw on the canvase
  (examples: title, lines, tick labels, and images all correspond to
             an invdividual Artist instance)
  
  two types of Artist objects -
    1) Primitive: Line2D, Rectangle, Circle, and Text
    2) Composite: Axis, Tick, Axes, and Figure
  
  each composite artist may contain other composite artists as well as
    primitive artists
    
Scipting Layer
  comprised mainly of pyplot - a scripting interface that syntactically
    lighter than the Artist layer
  automates the definition of a Canvas and Figure Artist instance and
    connecting these two instances together
    
http://www.aosabook.org/en/matplotlib.html
'''

# Rendering a histogram using the Artist layer
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import numpy as np

fig = Figure()
canvas = FigureCanvas(fig)

x = np.random.randn(10000)

ax = fig.add_subplot(111)

ax.hist(x, 100)
ax.set_title('Normal Distribution with $\mu = 0, \sigma = 1$')
fig.savefig('matplotlib_histogram.png')

# Rendering the same histogram as above using the Scripting layer
import matplotlib.pyplot as plt
plt.hist(x, 100)
plt.title(r'Normal Distribution with $\mu = 0, \sigma - 1$')
plt.savefig('matplotlib_histogram2.png')
plt.show()