import seaborn as sns
import matplotlib.pyplot as plt

cities = ['New York', 'Beijing', 'Tokyo', 'Osaka', 'Shanghai', 'Cairo', 'Delhi', 'Karachi', 'Dhaka', 'Mexico City', 'Mumbai', 'Sao Paulo']
months = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']
temperatures = [
    [4, 6, 11, 18, 22, 27, 29, 29, 25, 18, 13, 7],  # New York
    [2, 5, 12, 21, 27, 30, 31, 30, 26, 19, 10, 4],  # Beijing
    [10, 10, 14, 19, 23, 26, 30, 31, 27, 22, 17, 12],  # Tokyo
    [9, 10, 14, 20, 25, 28, 32, 33, 29, 23, 18, 12],  # Osaka
    [8, 10, 14, 20, 24, 28, 32, 32, 27, 23, 17, 11],  # Shanghai
    [19, 21, 24, 29, 33, 35, 35, 35, 34, 30, 25, 21],  # Cairo
    [20, 24, 30, 37, 40, 39, 35, 34, 34, 33, 28, 22],  # Delhi
    [26, 28, 32, 35, 36, 35, 33, 32, 33, 35, 32, 28],  # Karachi
    [25, 29, 32, 33, 33, 32, 32, 32, 32, 31, 29, 26],  # Dhaka
    [22, 24, 26, 27, 27, 26, 24, 25, 24, 24, 23, 23],  # Mexico City
    [31, 32, 33, 33, 34, 32, 30, 30, 31, 34, 34, 32],  # Mumbai
    [29, 29, 28, 27, 23, 23, 23, 25, 25, 26, 27, 28],  # Sao Paulo
]

sns.heatmap(temperatures, yticklabels=cities, xticklabels=months, cmap='coolwarm')
plt.title('Average Monthly Temperatures in Major Cities')
plt.xlabel('Month')
plt.ylabel('City')
plt.show()