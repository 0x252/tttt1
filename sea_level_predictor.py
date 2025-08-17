import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    fig, ax = plt.subplots(figsize=(12,6))
    sizes = df['CSIRO Adjusted Sea Level'] * np.pi*3
    colors = df['CSIRO Adjusted Sea Level']
    sc = ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], c=colors, s=sizes)
    for start, color in [(df['Year'].min(), 'red'), (2000, 'green')]:
        d = df[df['Year'] >= start]
        s, i, *_ = linregress(d['Year'], d['CSIRO Adjusted Sea Level'])
        ax.plot(np.arange(start, 2051), s*np.arange(start, 2051)+i, color=color)

    ax.set(title="Rise in Sea Level", xlabel="Year", ylabel="Sea Level (inches)")
    ax.set_xticks([1850,1875,1900,1925,1950,1975,2000,2025,2050,2075])
    cbar = plt.colorbar(sc, ax=ax)
    cbar.set_label('Sea Level (inches)')
    plt.savefig('sea_level_plot.png')
    return ax