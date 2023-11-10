import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset from a CSV file
data = pd.read_csv('L2RogateDailyMet.csv')

# Convert the 'date' column to a datetime object with the correct format
data['date'] = pd.to_datetime(data['date'], format='%d/%m/%Y')

# Function to create a line plot
def create_line_plot(data, x_col, y_col, title, x_label, y_label):
    plt.figure(figsize=(10, 6))
    for col in data[y_col].unique():
        subset = data[data[y_col] == col]
        plt.plot(subset[x_col], subset['mean/sum'], label=col)
    
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to create a scatter plot
def create_scatter_plot(data, x_col, y_col, title, x_label, y_label):
    plt.figure(figsize=(10, 6))
    plt.scatter(data[x_col], data[y_col], c=data['mean/sum'], cmap='viridis')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.colorbar(label='Mean/Sum')
    plt.grid(True)
    plt.show()

# Function to create a histogram
def create_histogram(data, col, title, x_label, y_label):
    plt.figure(figsize=(10, 6))
    plt.hist(data[col], bins=15, edgecolor='k', alpha=0.7)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.show()

# Create line plot
create_line_plot(data, 'date', 'met type', 'Air Temperature Over Time', 'Date', 'Air Temperature')

# Create scatter plot
create_scatter_plot(data, 'mean/sum', 'max', 'Scatter Plot of Maximum Temperature vs. Mean/Sum', 'Mean/Sum', 'Max Temperature')

# Create histogram
create_histogram(data, 'mean/sum', 'Histogram of Mean/Sum of Air Temperature', 'Mean/Sum', 'Frequency')
