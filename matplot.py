import matplotlib.pyplot as plt

# Datos para el gráfico de líneas
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Datos para el gráfico de barras
categories = ['A', 'B', 'C', 'D']
values = [25, 45, 60, 15]

# Datos para el gráfico de pastel
sizes = [30, 15, 45, 10]
labels = ['A', 'B', 'C', 'D']

# Crear una figura y subtramas para los gráficos
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

# Gráfico de Líneas
axes[0, 0].plot(x, y)
axes[0, 0].set_xlabel('X')
axes[0, 0].set_ylabel('Y')
axes[0, 0].set_title('Gráfico de Líneas')

# Gráfico de Barras
axes[0, 1].bar(categories, values)
axes[0, 1].set_xlabel('Categorías')
axes[0, 1].set_ylabel('Valores')
axes[0, 1].set_title('Gráfico de Barras')

# Gráfico de Pastel
axes[1, 0].pie(sizes, labels=labels)
axes[1, 0].set_title('Gráfico de Pastel')

# Eliminar la cuarta subtrama
fig.delaxes(axes[1, 1])

# Ajustar el espaciado entre los gráficos
plt.tight_layout()

# Mostrar el gráfico
plt.show()