import plotly.graph_objects as go # to make a graph
import numpy as np # to generate test data

N = 100 # data size
x = np.linspace(0, 20, N)
y = np.random.rand(N)


fig = go.FigureWidget()
fig.add_scatter(x=x, y=y)

# let's update both title and the y data at the same time
FRAME = 10000 # how many times which update the graph
first_scatter_plot = fig.data[0] # getting reference from the graph


for i in range(FRAME):
    first_scatter_plot.y = np.random.rand(N) # updating y data
    fig.update_layout(title=f'FRAME: {i + 1}');