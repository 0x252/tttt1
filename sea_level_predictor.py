import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Загрузка данных
    df = pd.read_csv('epa-sea-level.csv')

    # Настройка фигуры
    fig, ax = plt.subplots(figsize=(12, 6))

    # Настройка размеров и цветов точек
    sizes = df['CSIRO Adjusted Sea Level'] * np.pi * 25
    colors = df['CSIRO Adjusted Sea Level']

    # Отрисовка scatter plot
    scatter = ax.scatter(
        df['Year'], df['CSIRO Adjusted Sea Level'],
        c=colors, s=sizes, cmap='viridis', edgecolor='k', alpha=0.7
    )

    # --- Линия тренда для всего периода ---
    slope_all, intercept_all, *_ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = np.arange(df['Year'].min(), 2051)
    sea_level_all = slope_all * years_all + intercept_all
    ax.plot(years_all, sea_level_all, color='red', linewidth=2, label='Trend (all years)')

    # --- Линия тренда с 2000 года ---
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, *_ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = np.arange(2000, 2051)
    sea_level_recent = slope_recent * years_recent + intercept_recent
    ax.plot(years_recent, sea_level_recent, color='green', linewidth=2, label='Trend (2000 onwards)')

    # Настройка подписей и сетки
    ax.set_title("Rise in Sea Level", fontsize=16)
    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("Sea Level (inches)", fontsize=12)
    ax.set_xticks([1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075])
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend()

    # Цветовая шкала
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Sea Level (inches)')

    # Сохранение графика
    plt.savefig('sea_level_plot.png')

    return ax