import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function for plot styling
def plot_styling():
    plt.style.use('dark_background')
    plt.gca().yaxis.grid(True, color='gray')
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = 'Ubuntu'
    plt.rcParams['font.monospace'] = 'Ubuntu Mono'
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.labelsize'] = 10
    plt.rcParams['axes.labelweight'] = 'bold'
    plt.rcParams['xtick.labelsize'] = 8
    plt.rcParams['ytick.labelsize'] = 8
    plt.rcParams['legend.fontsize'] = 10
    plt.rcParams['figure.titlesize'] = 12
    for spine in plt.gca().spines.values():
        spine.set_visible(False)
    plt.xlabel('Hour')
    plt.ylabel('Watts indicator [Adimensional]')
    plt.ylim((0, 30))
    plt.xlim(0,24)

# Read the CSV file
csv_reader = open('C:\\Users\\Diogo Sá\\Desktop\\perkier tech\\Energy\\CODE\\Google API\\Consumption.txt', 'rb')
csv_read = pd.read_csv(csv_reader, encoding='latin1', header=None)
csv_reader.close()

# Loop for polynomial regression
for degree in range(1, 16):
    plt.clf()  # Clear the plot at the beginning of each iteration
    x = np.array(csv_read.loc[:, 0])
    y = np.array(csv_read.loc[:, 1])
    plot_styling()
    plt.plot(x, y, marker='o', markersize=3, label='Data')
    z = np.polyfit(x, y, degree)  # Perform polynomial regression
    p = np.poly1d(z)
    xp = np.linspace(x.min(), x.max())
    plt.plot(xp, p(xp), '-', color='mediumseagreen', alpha=0.4, linewidth=4, ls='-', label=f'Polynomial Regression (Degree {degree})')
    plt.legend()
    plt.title(f'Duck Curve Function - Polynomial Regression (Degree {degree})')
    plt.savefig(f'polynomial_regression_degree_{degree}.png')

# Calculate load profile
hours = np.arange(24)
Watts_Ad = p(hours)
sum_original = Watts_Ad.sum()
sum_inverse = 1 / sum_original
Watts_Ad *= sum_inverse

# Assuming remaining part of your code is correct
# You can use Watts_Ad for further calculations.
