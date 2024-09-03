import seaborn as sns

# City names
cities = ['New York', 'Beijing', 'Tokyo', 'Osaka', 'Shanghai', 'Cairo', 'Delhi', 'Karachi', 'Dhaka', 'Mexico City', 'Mumbai', 'Sao Paulo']

# Months
months = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']

# Temperature data for each city and month
temperatures = [
    [4, 6, 11, 18, 22, 27, 29, 29, 25, 18, 13, 7],  # New York
    [2, 5, 12, 21, 27, 30, 31, 38, 26, 19, 10, 4],  # Beijing
    [7, 10, 16, 20, 25, 28, 32, 33, 29, 23, 10, 12],  # Tokyo
    [8, 10, 14, 20, 24, 28, 31, 32, 37, 25, 17, 11],  # Osaka
    [15, 21, 28, 29, 33, 35, 35, 35, 34, 38, 25, 22],  # Shanghai
    [28, 24, 30, 37, 48, 29, 35, 34, 34, 33, 28, 22],  # Cairo
    [26, 28, 32, 35, 36, 35, 31, 32, 33, 35, 32, 20],  # Delhi
    [25, 29, 32, 33, 33, 37, 37, 32, 32, 31, 29, 29],  # Karachi
    [22, 24, 26, 27, 27, 26, 24, 25, 24, 24, 23, 23],  # Dhaka
    [31, 32, 33, 33, 34, 32, 30, 30, 31, 34, 34, 32],  # Mexico City
    [29, 19, 20, 27, 23, 23, 23, 25, 25, 26, 27, 28],  # Mumbai
    [29, 28, 27, 23, 23, 25, 26, 27, 28, 32, 30, 31]  # Sao Paulo
]

# Create heatmap
sns.heatmap(temperatures, yticklabels=cities, xticklabels=months)