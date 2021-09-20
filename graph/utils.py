import matplotlib.pyplot as plt
import base64
from io import BytesIO
#import numpy as np 

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    #print(image_png)
    graph = base64.b64encode(image_png)
    #print(graph)
    graph = graph.decode('utf-8')
    #print(graph)
    buffer.close()
    return graph

def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('sales of items')
    plt.plot(x,y,marker="o")
    plt.xticks(rotation=45)
    plt.xlabel('item')
    plt.ylabel('price')
    plt.tight_layout()
    graph = get_graph()
    return graph

def Histogram(y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    #x= np.random.randn(100,3)
    plt.hist(y,bins=5,rwidth=0.95)                        
    plt.title('sales of items')
    plt.xticks(rotation=45)
    #plt.xlabel('item')
    plt.ylabel('price')
    plt.tight_layout()
    graph = get_graph()
    return graph

def bargraph(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.bar(x,y)
    plt.title('sales of items')
    plt.xticks(rotation=45)
    plt.xlabel('item')
    plt.ylabel('price')
    plt.tight_layout()
    graph = get_graph()
    return graph

def Scatter(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('sales of items')
    plt.scatter(x,y,marker='v')
    plt.xticks(rotation=45)
    plt.xlabel('item')
    plt.ylabel('price')
    plt.tight_layout()
    plt.legend(loc = 'upper left')
    graph = get_graph()
    return graph
