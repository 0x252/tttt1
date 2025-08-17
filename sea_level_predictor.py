import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    fig, ax = plt.subplots(figsize=(10,6))

    plt.scatter(df['Year'], df['NOAA Adjusted Sea Level'], color='blue')

    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['NOAA Adjusted Sea Level'])
    years_extended = np.arange(df['Year'].min(), 2051, 1)
    line = slope * years_extended + intercept
    ax.plot(years_extended, line, color='red')

    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.set_xticks([1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075])

    plt.savefig('sea_level_plot.png')
    return plt.gca()