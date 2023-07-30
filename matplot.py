import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

categories = ['A', 'B', 'C', 'D']
values = [25, 45, 60, 15]

sizes = [30, 15, 45, 10]
labels = ['A', 'B', 'C', 'D']

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

axes[0, 0].plot(x, y)
axes[0, 0].set_xlabel('X')
axes[0, 0].set_ylabel('Y')
axes[0, 0].set_title('Line')

axes[0, 1].bar(categories, values)
axes[0, 1].set_xlabel('Categories')
axes[0, 1].set_ylabel('Values')
axes[0, 1].set_title('Bars')

axes[1, 0].pie(sizes, labels=labels)
axes[1, 0].set_title('Cercle')

fig.delaxes(axes[1, 1])

plt.tight_layout()

plt.show()