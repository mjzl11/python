import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    'Nombre': ['Juan', 'María', 'Pedro', 'Ana', 'Luis', 'Elena'],
    'Edad': [25, 30, 21, 28, 35, 27],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia', 'Bilbao', 'Málaga'],
    'Profesión': ['Ingeniero', 'Abogada', 'Estudiante', 'Médica', 'Programador', 'Arquitecta'],
    'Salario': [4000, 3000, 2000, 4500, 5000, 3500]
}
df = pd.DataFrame(data)

# Mostrar el DataFrame
print("DataFrame original:")
print(df)

# Filtrar el DataFrame por salario
filtro_salario = df['Salario'] > 3000
df_filtrado = df[filtro_salario]

# Mostrar el DataFrame filtrado
print("\nDataFrame filtrado por salario:")
print(df_filtrado)

# Calcular la media de edad y salario
media_edad = df['Edad'].mean()
media_salario = df['Salario'].mean()

# Mostrar la media de edad y salario
print("\nMedia de edad:", media_edad)
print("Media de salario:", media_salario)