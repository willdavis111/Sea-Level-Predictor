import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(x, y)

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    years_extended = np.arange(1880, 2051, 1)
    line = [slope * xi + intercept for xi in years_extended]
    ax.plot(years_extended, line, 'r', linewidth=1)
    # Create second line of best fit
    years_extended2 = np.arange(2000, 2051, 1)
    df2000 = df[df['Year'] >= 2000]
    x2 = df2000['Year']
    y2 = df2000['CSIRO Adjusted Sea Level']
    slope2, intercept2, r_value, p_value, std_err = linregress(x2, y2)
    line2 = [slope2 * xi + intercept2 for xi in years_extended2]
    ax.plot(years_extended2, line2, 'g', linewidth=1)
    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()