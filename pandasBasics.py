import pandas as pd

data = {
    'Name': ['Juan', 'María', 'Pedro', 'Ana', 'Luis', 'Elena'],
    'Age': [25, 30, 21, 28, 35, 27],
    'City': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia', 'Bilbao', 'Málaga'],
    'Job': ['Ingeniero', 'Abogada', 'Estudiante', 'Médica', 'Programador', 'Arquitecta'],
    'Salary': [4000, 3000, 2000, 4500, 5000, 3500]
}
df = pd.DataFrame(data)

print("DataFrame original:")
print(df)

bigSalaries = df['Salary'] > 3000
filteredDF = df[bigSalaries]

print("\nDataFrame ordered:")
print(filteredDF)

averageAge = df['Edad'].mean()
averageSalary = df['Salario'].mean()

print("\nAverage Age:", averageAge)
print("Average Salary:", averageSalary)