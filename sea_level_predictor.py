import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    fig, ax = plt.subplots(figsize=(12, 6))

    sizes = df['CSIRO Adjusted Sea Level'] * np.pi * 3
    colors = df['CSIRO Adjusted Sea Level']  
    scatter = ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], 
                         c=colors, s=sizes, cmap='viridis', edgecolor='k', alpha=0.7)

    
    regression_periods = [
        (df['Year'].min(), 'red'),   
        (2000, 'green')              #
    ]

    for start_year, line_color in regression_periods:
        data_subset = df[df['Year'] >= start_year]
        slope, intercept, *_ = linregress(data_subset['Year'], data_subset['CSIRO Adjusted Sea Level'])
        years_range = np.arange(start_year, 2051)
        sea_level_fit = slope * years_range + intercept
        ax.plot(years_range, sea_level_fit, color=line_color, linewidth=2)

    ax.set_title("Rise in Sea Level", fontsize=16)
    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("Sea Level (inches)", fontsize=12)
    ax.set_xticks([1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075])
    ax.grid(True, linestyle='--', alpha=0.5)

    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Sea Level (inches)')

    plt.savefig('sea_level_plot.png')

    return ax