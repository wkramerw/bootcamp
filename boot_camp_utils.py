import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#settings for plots

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

def ecdf(data):
    """defining ecdf function"""
#defining x and y
    x = np.sort(data)
    y = np.arange(1, len(data)+1)/ len(data)
    return x, y
