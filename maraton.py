import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Cargar los datos históricos del maratón
data = pd.read_csv('./data/marathon.csv')

# Dividir los datos en características (X) y etiquetas (y)
X = data[['Distance', 'Avg_Pace']]
y = data['Time']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Obtener los datos del corredor actual
distance = float(input("Distancia del maratón (en km): "))
pace = float(input("Ritmo promedio del corredor (en minutos/km): "))

# Predecir el tiempo del corredor actual
time = model.predict([[distance, pace]])

# Imprimir el tiempo estimado del corredor
print("Tiempo estimado del corredor: {:.2f} horas".format(time[0]))