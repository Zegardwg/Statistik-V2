import matplotlib.pyplot as plt

labels = ['Vanilla', 'Coklat', 'Stobery', 'Mango', 'Maccha']
sizes = [26.2, 28.6, 16.7, 19.0, 9.5]
colors = ['#ffcc99', '#cc99ff', '#ff9999', '#ffcc00', '#99ff99']

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Flavor Distribution')
plt.show()
