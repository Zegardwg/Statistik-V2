import matplotlib.pyplot as plt

# Lemon data
lemon_diameter = [6.44, 6.87, 7.7, 8.85, 8.15, 9.96, 7.21, 10.04, 10.2, 11.06]
lemon_weight = [112.05, 114.58, 116.71, 117.4, 128.93, 132.93, 138.92, 145.98, 148.44, 152.81]

# Lime data
lime_diameter = [6.15, 7.0, 7.0, 7.69, 7.95, 7.51, 10.46, 8.72, 9.53, 10.09]
lime_weight = [112.76, 125.16, 131.36, 132.41, 138.08, 142.55, 155.86, 158.67, 163.28, 166.74]

# Create scatter plot
plt.scatter(lemon_diameter, lemon_weight, label='Lemons')
plt.scatter(lime_diameter, lime_weight, label='Limes')

# Set title and labels
plt.title('Lemons vs Limes')
plt.xlabel('Diameter (cm)')
plt.ylabel('Weight (g)')

# Add legend
plt.legend()

# Show the plot
plt.show()